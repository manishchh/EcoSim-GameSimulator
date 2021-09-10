from tiles.tile import Tile

# Sand Tile class inherits from Tile Class
class Sand(Tile):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)
    
    def __str__(self):
        return f'Sand Tile is at position ({self.get_position().x},{self.get_position().y})'

    def __repr__(self):
        return f'SandTile({self.get_position().x},{self.get_position().y})'