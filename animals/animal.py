import abc
from game import GameObject, Vector2D
import random
from random import randint

class OutOfBoundException(Exception):
    """Base class for other exceptions"""
    pass

class Animal(GameObject):

    _lifeSpan =0
    _maxEnergy =0
    _energyIncrementValue =0

    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game)
        self.target = Vector2D(random.randint(self.get_x()-20, self.get_x()+20), 
        random.randint(self.get_y()-20, self.get_y()+20)) 
        self.speed = speed
        self.energy = energy
        self._maxEnergy = energy

    def reduceEnergy(self,timeElapsed):
        self.energy -= timeElapsed
        if self.energy<=0:
            self.destroy()  
    

    def restoreEnergy(self):
        if(self.energy + self._energyIncrementValue <= self._maxEnergy):
            self.energy += self._energyIncrementValue
    
    def isHungry(self):
        return self.energy<int(self._maxEnergy/2)
    
    def getRandomLocation(self):
        maxXWindowCoOrdinate = int(1152/64) -1
        maxYWindowCoOrdinate = int(984/64) -1
        randomX = randint(0,maxXWindowCoOrdinate)
        randomY = randint(0,maxYWindowCoOrdinate)
        return Vector2D(randomX*64,randomY*64)

    def isOutsideBound(self,vector2D):
        return vector2D.x > (64*12)  or vector2D.y > (640)

    def getRandomValidLocation(self):
        maxXWindowCoOrdinate = 11
        maxYWindowCoOrdinate = 9
        randomX = randint(0,maxXWindowCoOrdinate)
        randomY = randint(0,maxYWindowCoOrdinate)
        return Vector2D(randomX*64,randomY*64)


    @abc.abstractmethod
    def update(self, seconds): 
        '''Called automatically by the attached Game. 
        This may be used to change the objects position, image, etc.
        Must be implemented by subclasses.'''
        pass