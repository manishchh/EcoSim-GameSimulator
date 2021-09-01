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
    

class Wombat(Animal):
    target= Vector2D(46,46)
    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game,speed,energy)
        
    def update(self,timeElapsed):

        self.closestGrass = self.getClosestGrass()
        self.target = self.closestGrass.get_position()
        if self.checkIfTargetReached():
            self.get_game()._remove_game_obj(self.closestGrass)
            self.closestGrass = self.getClosestGrass()
            self.target = self.closestGrass.get_position()
        
        trajectory = self.target.subtract(self.get_position())
        trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
        self.move_by(trajectory.x, trajectory.y)

    def checkIfTargetReached(self):
        currentDistance = self.get_position().distance(self.target)
        if(currentDistance<18):
            return True
        return False

    
    

    def getClosestGrass(self):
        gameObjects = self.get_game().get_game_objs()
        closestGrass = gameObjects[0]
        shortestDistance =  1000
        for gameObject in gameObjects:
            if isinstance(gameObject,Grass):
                currentShortestDistance =  self.get_position().distance(gameObject.get_position())
                if currentShortestDistance< shortestDistance:
                    shortestDistance = currentShortestDistance
                    closestGrass = gameObject
        return closestGrass




class Snake(Animal):
     def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game)

class Mongoose(Animal):
     def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game)

class Plant(GameObject):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

class Grass(Plant):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    def update(self, seconds):
        return super().update(seconds)

class EcoSim(Game):
    def __init__(self):
        super().__init__()
        list_of_tiles = [Dirt, Sand]
        dirtCount =0
        # list_of_plants = [Grass, BlueBerryBush]
        # list_of_animals = [Wombat, Snake]
        for i in range(12):
            for j in range(10):
                random_list = random.choice(list_of_tiles)
                if random_list == Dirt:
                    tile = Dirt(Vector2D(i*64,j*64), 64, 64, ImageLibrary.get('dirt_tile'), self)
                    dirtCount+=1
                    
                elif random_list == Sand:
                    tile = Sand(Vector2D(i*64,j*64), 64, 64, ImageLibrary.get('sand_tile'), self)
        dirtCount = dirtCount/2
        for x in self.get_game_objs():
            if isinstance(x,Dirt) and dirtCount>0: 
                Grass(x.get_position(),64, 64, ImageLibrary.get('grass_tuft'), self)
                dirtCount-=1

        Wombat(Vector2D(480, 0),48,48,ImageLibrary.get('wombat1'),self,50,300)

        # self.animal = Animal(Vector2D(96, 96), 96, 96, ImageLibrary.get('wombat1'), self, 10, 3)
    
    
    
def main():
    ImageLibrary.load('images') 
    ecosim = EcoSim()
    ecosim.run()

if __name__ == '__main__':
    main()