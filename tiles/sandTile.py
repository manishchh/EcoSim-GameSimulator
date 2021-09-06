

from tiles.tile import Tile


class Sand(Tile):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)
