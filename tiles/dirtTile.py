from tiles.tile import Tile


class Dirt(Tile):

    def __init__(self, position, width, height, sourceImage, game,plant):
        super().__init__(position, width, height, sourceImage, game)
        self.__plant = plant

    def getPlant(self):
        return self.__plant

    def setPlant(self,plant):
        self.__plant = plant
    def update(self, timeElapsed):
        pass