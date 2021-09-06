
from animals.wombat import Wombat
from tiles.dirtTile import Dirt
from tiles.sandTile import Sand
from plants.grass import Grass
from plants.berrybush import BerryBush
from game import *
import random

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
        self.generateWombats()
    
    def getDirtTiles(self):
        return self.__listOfDirtTiles

    def generateWombats(self):
        generatedPositions = []
        x =0
        while x !=8:
            randomXCoordinate = random.randint(0,11)*64
            randomYCoordinate = random.randint(0,9)*64
            if self.checkPositionExistsInArray(generatedPositions,Vector2D(randomXCoordinate,randomYCoordinate)) == False:
                wombat = Wombat(Vector2D(randomXCoordinate,randomYCoordinate),64,64,ImageLibrary.get('wombat1'),self,20,15)
                generatedPositions.append(Vector2D(randomXCoordinate,randomYCoordinate))
                x+=1
    
    def checkPositionExistsInArray(self,array, position):
        for item in array:
            exists = item.x == position.x and item.y == position.y
            if exists:
                return True
        return False

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