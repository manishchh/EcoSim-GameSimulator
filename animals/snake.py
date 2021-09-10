from animals.wombat import Wombat
from animals.animal import *

#snake inherits from animal
class Snake(Animal):
   __defaultSpeed = 0
   __speedWhenHungry = 45
   target = Vector2D(0,0)
   def __init__(self, position, width, height, sourceImage, game, speed, energy):
        super().__init__(position, width, height, sourceImage, game,speed,energy)
        self.__defaultSpeed = speed
        self._energyIncrementValue = 15

   #override is hungry method to implement its own logic
   def isHungry(self):
        return self.energy<int(self._maxEnergy/3)


   def update(self, timeElapsed):
      self._lifeSpan += timeElapsed# increment life span, useful for breeding logic
      if(self._lifeSpan >=32):# snake reproduce in 32 seconds
            self.breedNewSnake()
      closestWombat = self.getClosestWombat()
      isHungry = self.isHungry()
      if(isHungry and closestWombat!=None):
         self.target = closestWombat.get_position()
         if self.checkIfTargetReached():
            self.get_game()._remove_game_obj(closestWombat)
            self.restoreEnergy()
      else:
         try:
               if self.checkIfTargetReached():
                  self.target = self.getRandomLocation()
                  if self.isOutsideBound(self.target):
                     raise OutOfBoundException
         except OutOfBoundException:
               self.target = self.getRandomValidLocation()

      trajectory = self.target.subtract(self.get_position())
      if isHungry:
         trajectory = trajectory.normalize().scale( self.__speedWhenHungry * timeElapsed)
      else:
          trajectory = trajectory.normalize().scale( self.__defaultSpeed * timeElapsed)
      self.move_by(trajectory.x, trajectory.y)
      self.reduceEnergy(timeElapsed)
   
   #reproduce new snake in current location
   def breedNewSnake(self):
        position = self.get_position()
        x = int(position.x)
        y = int(position.y)
        Snake(Vector2D(x,y),64,64,self.get_image(),self.get_game(),20,15)
        self._lifeSpan=0# reset lifespan to reset breeding time

   #method to check if target is reached.
   def checkIfTargetReached(self):
      currentDistance = self.get_position().distance(self.target)
      if(currentDistance < 32):
         return True
      return False

   #method to get closes wombat
   def getClosestWombat(self):
      gameObjects = self.get_game().get_game_objs()
      closestWombat= None
      closestDistance = None
      for object in gameObjects:
         if isinstance(object,Wombat):
            if closestWombat == None:
               closestWombat = object
               closestDistance = self.get_position().distance(object.get_position())
            elif self.get_position().distance(object.get_position()) < closestDistance:
               closestWombat = object
               closestDistance =self.get_position().distance(object.get_position())
      return closestWombat

   def __str__(self):
      return f'Snake is at position ({self.get_position().x},{self.get_position().y}), energy and speed are {self.energy} and {self.speed} respectively'

   def __repr__(self):
        return f'Snake({self.get_position().x},{self.get_position().y}): {self.energy}:{self.speed}'