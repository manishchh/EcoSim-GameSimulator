from tiles.tile import Tile

# Dirt Tile class inherits from Tile Class
class Dirt(Tile):

    def __init__(self, position, width, height, sourceImage, game,plant):
        super().__init__(position, width, height, sourceImage, game)
        self.__plant = plant

    #getter to expose private __plant object in dirt tile
    def getPlant(self):
        return self.__plant

    #setter to update private __plant object in dirt tile
    def setPlant(self,plant):
        self.__plant = plant

    def __str__(self):
        return f'Dirt Tile is at position ({self.get_position().x},{self.get_position().y})'

    def __repr__(self):
        return f'DirtTile({self.get_position().x},{self.get_position().y})'
