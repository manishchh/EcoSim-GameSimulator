
from plants.plant import Plant


class BerryBush(Plant):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    def update(self, seconds):
        return super().update(seconds)
