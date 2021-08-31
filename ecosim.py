from game import *
import random

class Tile(GameObject):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)


    def update(self, timeElapsed):
        print('Time Elapsed =', timeElapsed)

# from tile import *

class Dirt(Tile):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)
      
        
    def update(self, timeElapsed):
        #grow plants;
        print("DirtTile")

class Sand(Tile):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)


class Animal(GameObject):
    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game)
        self.target = Vector2D(random.randint(self.get_x()-20, self.get_x()+20), 
        random.randint(self.get_y()-20, self.get_y()+20)) 
        self.speed = speed
        self.energy = energy
    
    def update(self,timeElapsed):
        self.energy -= timeElapsed
        if self.energy <0:
            self.destroy()
        else:
            trajectory = self.target.subtract(self.get_position())
            trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
            self.move_by(trajectory.x, trajectory.y)

class EcoSim(Game):
    def __init__(self):
        super().__init__()
        list_of_tiles = [Dirt, Sand]
        dirtCount =0
        # list_of_plants = [Grass, BlueBerryBush]
        # list_of_animals = [Wombat, Snake]
        for i in range(12):
            for g in range(10):
                random_list = random.choice(list_of_tiles)
                if random_list == Dirt:
                    tile = Dirt(Vector2D(i*64,g*64), 64, 64, ImageLibrary.get('dirt_tile'), self)
                    dirtCount+=1
                    
                elif random_list == Sand:
                    tile = Sand(Vector2D(i*64,g*64), 64, 64, ImageLibrary.get('sand_tile'), self)
        dirtCount = dirtCount/2
        for x in self.get_game_objs():
            if isinstance(x,Dirt) and dirtCount>0: 
                Animal(x.get_position(),64, 64, ImageLibrary.get('wombat1'), self, 10, 3)
                dirtCount-=1


        # self.animal = Animal(Vector2D(96, 96), 96, 96, ImageLibrary.get('wombat1'), self, 10, 3)
    
    
    
def main():
    ImageLibrary.load('images') 
    ecosim = EcoSim()
    ecosim.run()

if __name__ == '__main__':
    main()