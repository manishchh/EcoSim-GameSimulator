
from game import GameObject


class Plant(GameObject):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)
   