
from game import ImageLibrary, Vector2D
from plants.plant import Plant

#Grass inherits Plant Object and Grass is eaten by wombats
class Grass(Plant):
    __lastUpdateTime =0# variable to hold last update time for regeneration of grass
    __grassRegenerationTime = 7# interval in number of seconds for grass regeneration
    
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    #update method is used for grass regeneration at certain interval
    def update(self, seconds):
        super().update(seconds)
        self.__lastUpdateTime+=seconds# add time elapsed to this variable until it reaches grass regeneration time
        if(self.__lastUpdateTime >=self.__grassRegenerationTime): #if grass regeneration time is exceeded
            self.generateNewGrass()# generate new grass
            self.__lastUpdateTime = 0# reset last update time.

    #function to generate New grass
    def generateNewGrass(self):
        dirtTiles = self.get_game().getDirtTiles() # get all dirt tiles
        for x in dirtTiles:
            distance = Vector2D.distance(self.get_position(),x.get_position()) # get distance from current position to make sure it is adjacent tile
            if distance == 64 and x.getPlant()==None:# if distance is 64px which is one tile unit, it is adjacent tile
                grass = Grass(x.get_position(),64,64,ImageLibrary.get("grass_tuft"),self.get_game())# generate grass
                x.setPlant(grass)# set grass on the dirt tile
                break #once a grass is regenerated exit loop
    
    def __str__(self):
        return f'Grass is at position ({self.get_position().x},{self.get_position().y})'

    def __repr__(self):
        return f'Grass({self.get_position().x},{self.get_position().y})'
                
        