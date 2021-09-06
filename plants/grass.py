
from game import ImageLibrary, Vector2D
from plants.plant import Plant


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
                
        