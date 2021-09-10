from animals.snake import Snake
from plants.carrot import Carrot
from animals.animal import OutOfBoundException
from animals.animal import Animal

#Mongoose inherits from Animal Class
#mongoose can have two targets Snake, Or Carrot
class Mongoose(Animal):
   def __init__(self, position, width, height, sourceImage, game, speed, energy):
      super().__init__(position, width, height, sourceImage, game,speed,energy)
      self._energyIncrementValue = 10
   
   def update(self,timeElapsed):
      self.closestTarget = self.getClosestTarget()
      if(self.isHungry() and self.closestTarget!=None):
         self.target = self.closestTarget.get_position()
         if self.checkIfTargetReached():
               self.get_game()._remove_game_obj(self.closestTarget)
               if isinstance(self.closestTarget,Carrot):#if carrot need to remove from dirt tile as well.
                  self.removeFromDirtTile(self.closestTarget)
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
      trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
      self.move_by(trajectory.x, trajectory.y)
      self.reduceEnergy(timeElapsed)

   #remove carror from dirt tile
   def removeFromDirtTile(self,plant):
      dirtTiles = self.get_game().getDirtTiles()
      for tile in dirtTiles:
         if tile.getPlant() !=None and tile.getPlant()== plant:
            tile.setPlant(None)

   #method to check if target is reached
   def checkIfTargetReached(self):
      currentDistance = self.get_position().distance(self.target)
      if(currentDistance<32):# if distance is less than half the tile size which is 64px
         return True
      return False

   #method to get closes targt
   def getClosestTarget(self):
      gameObjects = self.get_game().get_game_objs()
      closestTarget = None
      closestDistance = None
      for object in gameObjects:
         if isinstance(object,Carrot) or isinstance(object,Snake):# if the target is carrot or snake
            if closestTarget == None:
               closestTarget = object
               closestDistance = self.get_position().distance(object.get_position())
            elif self.get_position().distance(object.get_position()) < closestDistance:
               closestTarget = object
               closestDistance =self.get_position().distance(object.get_position())
      return closestTarget

   def __str__(self):
      return f'Mongoose is at position ({self.get_position().x},{self.get_position().y}), energy and speed are {self.energy} and {self.speed} respectively'

   def __repr__(self):
      return f'Mongoose({self.get_position().x},{self.get_position().y}): {self.energy}:{self.speed}'


