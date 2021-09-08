from animals.wombat import Wombat
from animals.animal import *


class Snake(Animal):
   __defaultSpeed = 0
   __speedWhenHungry = 45
   def __init__(self, position, width, height, sourceImage, game, speed, energy):
        super().__init__(position, width, height, sourceImage, game,speed,energy)
        self.__defaultSpeed = speed
        self._energyIncrementValue = 15

   def update(self, timeElapsed):
      self._lifeSpan += timeElapsed
      if(self._lifeSpan >=32):
            self.breedNewSnake()
      closestWombat = self.getClosestWombat()
      isHungry = self.isHungry()
      if(isHungry and closestWombat!=None):
         print("wombat Hungry")
         self.target = closestWombat.get_position()
         if self.checkIfTargetReached():
            print("closest wombat reached")
            self.get_game()._remove_game_obj(closestWombat)
            self.restoreEnergy()
      else:
         try:
               if self.checkIfTargetReached():
                  self.target = self.getRandomLocation()
                  if self.isOutsideBound(self.target):
                     raise OutOfBoundException
         except OutOfBoundException:
               print("target out of bound for wombat")
               self.target = self.getRandomValidLocation()

      trajectory = self.target.subtract(self.get_position())
      if isHungry:
         trajectory = trajectory.normalize().scale( self.__speedWhenHungry * timeElapsed)
      else:
          trajectory = trajectory.normalize().scale( self.__defaultSpeed * timeElapsed)
      self.move_by(trajectory.x, trajectory.y)
      self.reduceEnergy(timeElapsed)
   
   def breedNewSnake(self):
        position = self.get_position()
        x = int(position.x)
        y = int(position.y)
        Snake(Vector2D(x,y),64,64,self.get_image(),self.get_game(),20,15)
        self._lifeSpan=0

   def checkIfTargetReached(self):
      currentDistance = self.get_position().distance(self.target)
      if(currentDistance < 32):
         print("distance", currentDistance)
         return True
      return False

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