from game import GameObject

#plant class inherits Game Object
class Plant(GameObject):
    def __init__(self, position, width, height , sourceImage, game):
        super().__init__(position, width, height, sourceImage, game)
    
    def update(self,timelapsed):
        pass
   