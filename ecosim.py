from game import *

class Tile(GameObject):
    def __init__(self, position, width, height, sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)


    def update(self, timeElapsed):
        print('Time Elapsed =', timeElapsed)

# from tile import *

class DirtTile(Tile):
    def __init__(self, position, width, height, sourceImage, game,gridPositionRow, GridPositionColumn, plant):
        super().__init__(position, width, height, sourceImage, game)
        self.gridPositionRow = gridPositionRow
        self.gridPositionColumn = GridPositionColumn
        self.plant = plant

    def update(self, timeElapsed):
        #grow plants;
        print("DirtTile")


class EcoSim(Game):
    def __init__(self):
        super().__init__()
       

    
def main():
    ImageLibrary.load('images')
    ecosim = EcoSim()
    tile = DirtTile(Vector2D(0,0), 96, 96, ImageLibrary.get('dirt_tile'), ecosim, 0,0,0)
    ecosim.run()

if __name__ == '__main__':
    main()