from game import GameObject

class Tile(GameObject):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    def update(self, timeElapsed):
        pass
