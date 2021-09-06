from game import GameObject, Vector2D
import random

class Animal(GameObject):

    _lifeSpan =0
    _maxEnergy =0

    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game)
        self.target = Vector2D(random.randint(self.get_x()-20, self.get_x()+20), 
        random.randint(self.get_y()-20, self.get_y()+20)) 
        self.speed = speed
        self.energy = energy
    
    def update(self,timeElapsed):
        self.energy -= timeElapsed
        if self.energy <0:
            self.destroy()
        else:
            trajectory = self.target.subtract(self.get_position())
            trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
            self.move_by(trajectory.x, trajectory.y)
    