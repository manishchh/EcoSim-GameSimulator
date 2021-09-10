
from plants.plant import Plant

#Carrot inhertist from Plant class and is eaten by mongoose.
class Carrot(Plant):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)

    def __str__(self):
        return f'Carrot is at position ({self.get_position().x},{self.get_position().y})'

    def __repr__(self):
        return f'Carrot({self.get_position().x},{self.get_position().y})'
