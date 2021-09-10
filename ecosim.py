import random

from animals.mongoose import Mongoose
from animals.snake import Snake
from animals.wombat import Wombat
from game import *
from plants.carrot import Carrot
from plants.grass import Grass
from tiles.dirtTile import Dirt
from tiles.sandTile import Sand

"""
Main EcoSimulation Class
Layouts and Tiles are based on 64px x 64px with 12 columns and 10 rows
"""
class EcoSim(Game):
    __listOfDirtTiles =[] # maintain the list of DirtTiles
    __maxSandTiles = 35 # number of sand tiles to generate
    def __init__(self):
        super().__init__()
        self.generateLayout()
        self.generatePlants()
        self.generateWombats()
        self.generateSnakes()
        self.generateMongoose()
    
    #Generates Dirt & Sand Tiles Layout
    def generateLayout(self):
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

    #Gets the saved generated Dirt Tiles which can be used from other code sections 
    def getDirtTiles(self):
        return self.__listOfDirtTiles

    #generates Wombat
    def generateWombats(self):
        generatedPositions = []
        x =0
        while x !=15:#number of wombats to generate
            randomXCoordinate = random.randint(0,11)*64# Main grid layout has 12 columns of size 64px
            randomYCoordinate = random.randint(0,9)*64# Main grid layout has 10 rows  of size 64px
            if self.checkPositionExistsInArray(generatedPositions,Vector2D(randomXCoordinate,randomYCoordinate)) == False:
                Wombat(Vector2D(randomXCoordinate,randomYCoordinate),64,64,ImageLibrary.get('wombat1'),self,24,15)
                generatedPositions.append(Vector2D(randomXCoordinate,randomYCoordinate))
                x+=1
    
    #Generate Snakes
    def generateSnakes(self):
        generatedPositions = []
        x =0
        while x !=3:#number of Snakes
            randomXCoordinate = random.randint(0,11)*64
            randomYCoordinate = random.randint(0,9)*64
            if self.checkPositionExistsInArray(generatedPositions,Vector2D(randomXCoordinate,randomYCoordinate)) == False:
                Snake(Vector2D(randomXCoordinate,randomYCoordinate),64,64,ImageLibrary.get('snake1'),self,20,25)
                generatedPositions.append(Vector2D(randomXCoordinate,randomYCoordinate))
                x+=1

    #generates Mongoose
    def generateMongoose(self):
        generatedPositions = []
        x =0
        while x !=3:#number of mongoose
            randomXCoordinate = random.randint(0,11)*64
            randomYCoordinate = random.randint(0,9)*64
            if self.checkPositionExistsInArray(generatedPositions,Vector2D(randomXCoordinate,randomYCoordinate)) == False:
                Mongoose(Vector2D(randomXCoordinate,randomYCoordinate),64,64,ImageLibrary.get('mongoose'),self,20,25)
                generatedPositions.append(Vector2D(randomXCoordinate,randomYCoordinate))
                x+=1

    # function to check if a Vector2D position exists in an Array of Vector2D Positions.
    def checkPositionExistsInArray(self,array, position):
        for item in array:
            exists = item.x == position.x and item.y == position.y #if both x and y co-ordinates match then they are equal
            if exists:
                return True
        return False

    #generate Plants
    def generatePlants(self):
        listDirtTiles = self.__listOfDirtTiles
        maximumNumberOfPlants = int(len(listDirtTiles)/1.5)# ratio of plants generation to the number of dirt tiles
        generatedNumberOfPlants =0
        while generatedNumberOfPlants < maximumNumberOfPlants:
            randomDirtTile = random.choice(listDirtTiles)
            if randomDirtTile.getPlant()==None: #check if plant is not already generated in the dirt tile.
                generatedNumberOfPlants+=1
                plantType = random.choice([Grass,Carrot]) # get random plant between grass and Carrot to generate in dirt tile
                if(plantType == Grass):
                    grass = Grass(randomDirtTile.get_position(),64,64,ImageLibrary.get('grass_tuft'),self)
                    randomDirtTile.setPlant(grass)
                else:
                    berry = Carrot(randomDirtTile.get_position(),64,64,ImageLibrary.get('carrot'),self)
                    randomDirtTile.setPlant(berry)

#main code execution start point
def main():
    ImageLibrary.load('images') 
    ecosim = EcoSim()
    ecosim.run()

if __name__ == '__main__':
    main()
