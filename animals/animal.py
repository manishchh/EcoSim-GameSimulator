import abc
from game import GameObject, Vector2D
import random
from random import randint

#Custom Exception class to represent out of bound when animal crosses boundary
class OutOfBoundException(Exception):
    """Base class for other exceptions"""
    pass

#Animal class inherits from GameObject
class Animal(GameObject):
    
    _lifeSpan =0# protected variable to hold lifspan of an animal, can be used for breeding logic
    _maxEnergy =0# protected variable to hold maxenergy, as energy changes every second
    _energyIncrementValue =0# protectedd variable to hold energy increment value when a target is killed.

    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game)
        self.target = Vector2D(random.randint(self.get_x()-20, self.get_x()+20), 
        random.randint(self.get_y()-20, self.get_y()+20)) 
        self.speed = speed
        self.energy = energy
        self._maxEnergy = energy

    #common function for all animals to reduce energy for each update
    def reduceEnergy(self,timeElapsed):
        self.energy -= timeElapsed
        if self.energy<=0:# if energy reaches less than zero destroy animal
            self.destroy()  
    
    #common function to restore energy by energy increment value overriden in each animal sub class
    def restoreEnergy(self):
        if(self.energy + self._energyIncrementValue <= self._maxEnergy):
            self.energy += self._energyIncrementValue
    
    #common function to check if animal is hungry, provides default implementation but can be overriden in subclasses if necessary
    def isHungry(self):
        return self.energy<int(self._maxEnergy/2)#by default half the max energy makes animal hungry
    
    #common function to generate random location when animal is not hungry
    def getRandomLocation(self):
        maxXWindowCoOrdinate = int(1152/64) -1 #full screen width for random location
        maxYWindowCoOrdinate = int(984/64) -1 #full screen height for random location
        randomX = randint(0,maxXWindowCoOrdinate)
        randomY = randint(0,maxYWindowCoOrdinate)
        return Vector2D(randomX*64,randomY*64)

    # function to check if an animal is outside the tiles grid
    def isOutsideBound(self,vector2D):
        return vector2D.x > (64*12)  or vector2D.y > (640)

    # function to return a valid position inside the tiles grid
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