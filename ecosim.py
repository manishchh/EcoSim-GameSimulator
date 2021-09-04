from game import *
import random

class Tile(GameObject):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)


    def update(self, timeElapsed):
        print('Time Elapsed =', timeElapsed)

# from tile import *

class Dirt(Tile):

    def __init__(self, position, width, height, sourceImage, game,plant):
        super().__init__(position, width, height, sourceImage, game)
        self.__plant = plant

    def getPlant(self):
        return self.__plant

    def setPlant(self,plant):
        self.__plant = plant
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
        if(self.closestGrass == None):
            print("grass finsidhed")
        else:
            self.target = self.closestGrass.get_position()
            if self.checkIfTargetReached():
                self.get_game()._remove_game_obj(self.closestGrass)
                self.closestGrass = self.getClosestGrass()
                if(self.closestGrass == None):
                    return
                else:  
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
        grassExists = False
        for gameObject in gameObjects:
            if isinstance(gameObject,Grass):
                grassExists =True
                currentShortestDistance =  self.get_position().distance(gameObject.get_position())
                if currentShortestDistance< shortestDistance:
                    shortestDistance = currentShortestDistance
                    closestGrass = gameObject
        if grassExists!= True:
            return None
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
    __lastUpdateTime =0
    __grassRegenerationTime = 15
    
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    def update(self, seconds):
        super().update(seconds)
        self.__lastUpdateTime+=seconds
        if(self.__lastUpdateTime >=self.__grassRegenerationTime):
            self.generateNewGrass()
            self.__lastUpdateTime = 0

    def generateNewGrass(self):
        dirtTiles = self.get_game().getDirtTiles()
        for x in dirtTiles:
            distance = Vector2D.distance(self.get_position(),x.get_position())
            if distance == 64 and x.getPlant()==None:
                grass = Grass(x.get_position(),64,64,ImageLibrary.get("grass_tuft"),self.get_game())
                x.setPlant(grass)
                break
                
           
class BerryBush(Plant):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    def update(self, seconds):
        return super().update(seconds)

class EcoSim(Game):
    __listOfDirtTiles =[]
    __maxSandTiles = 55
    def __init__(self):
        super().__init__()
        sandCount =0
        for i in range(12):
            for j in range(10):
                random_list = random.choice([Dirt,Sand])
                if random_list == Dirt or sandCount==self.__maxSandTiles:
                    tile = Dirt(Vector2D(i*64,j*64), 64, 64, ImageLibrary.get('dirt_tile'), self,None)
                    self.__listOfDirtTiles.append(tile)
                elif random_list == Sand:
                    tile = Sand(Vector2D(i*64,j*64), 64, 64, ImageLibrary.get('sand_tile'), self)
                    sandCount+=1
        self.generatePlants()
    
    def getDirtTiles(self):
        return self.__listOfDirtTiles

    def generatePlants(self):
        listDirtTiles = self.__listOfDirtTiles
        maximumNumberOfPlants = len(listDirtTiles)/2
        generatedNumberOfPlants =0
        while generatedNumberOfPlants < maximumNumberOfPlants:
            randomDirtTile = random.choice(listDirtTiles)
            if randomDirtTile.getPlant()==None:
                generatedNumberOfPlants+=1
                plantType = random.choice([Grass,BerryBush])
                if(plantType == Grass):
                    grass = Grass(randomDirtTile.get_position(),64,64,ImageLibrary.get('grass_tuft'),self)
                    randomDirtTile.setPlant(grass)
                else:
                    berry = BerryBush(randomDirtTile.get_position(),64,64,ImageLibrary.get('blueberry_bush'),self)
                    randomDirtTile.setPlant(berry)

def main():
    ImageLibrary.load('images') 
    ecosim = EcoSim()
    ecosim.run()

if __name__ == '__main__':
    main()