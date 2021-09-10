from random import randint
from animals.animal import Animal, OutOfBoundException
from game import Vector2D
from plants.grass import Grass

#Wombat class inherits Animal Class
class Wombat(Animal):
    target= Vector2D(46,46)

    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game,speed,energy)
        self._energyIncrementValue = 10

    #function to update Wombat 
    def update(self,timeElapsed):
        self._lifeSpan += timeElapsed #increase lifespan in every loop, used for breeding logic
        if(self._lifeSpan >=18):#if lifespan exceeds 18 seconds, wombats will reproduce
            self.breedNewWombat()
        self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()# get closes dirt tile with grass
        if(self.isHungry() and self.closestDirtTileWithGrass!=None): #if wombat is hugry and grass available
            self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()
            self.target = self.closestDirtTileWithGrass.getPlant().get_position()# get plants position as the target
            if self.checkIfTargetReached(): # if targe position reached
                self.get_game()._remove_game_obj(self.closestDirtTileWithGrass.getPlant())# remove grass from game
                self.restoreEnergy()# restore energy
                # if(self.closestDirtTileWithGrass == None):# 
                #     return
                # else:  
                self.closestDirtTileWithGrass.setPlant(None) # remove plant from corresponding dirt tile
        else:# when wombat is not hungry, or no grass available, move to random location
            try:
                if self.checkIfTargetReached():
                    self.target = self.getRandomLocation()
                    if self.isOutsideBound(self.target):#if animal reaches out of boundary throw exception
                        raise OutOfBoundException
            except OutOfBoundException:
                print("target out of bound for wombat")
                self.target = self.getRandomValidLocation()# get a valid location within the boundary

        trajectory = self.target.subtract(self.get_position())
        trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
        self.move_by(trajectory.x, trajectory.y)
        self.reduceEnergy(timeElapsed)# reduce energy on each cycle

    #breed wombat in its current location
    def breedNewWombat(self):
        position = self.get_position()
        x = int(position.x)
        y = int(position.y)
        Wombat(Vector2D(x,y),64,64,self.get_image(),self.get_game(),20,15)
        self._lifeSpan=0# when a breeding happens life span is reset to wait for next regeneration cycle

    #check if target reached
    def checkIfTargetReached(self):
        currentDistance = self.get_position().distance(self.target)
        if(currentDistance<32):
            print("distance", currentDistance)
            return True
        return False

    #get closes dirt tile with grass
    def getClosestDirTileWithGrass(self):
        dirtTiles = self.get_game().getDirtTiles()# gets all dirt tiles in game
        closestDirtTileWithGrass = None
        shortestDistance =  None
        for x in dirtTiles:#loop through each dirt tile and find the closes one.
            grass = x.getPlant()
            if isinstance(grass,Grass):# if  plant on the dirt tile is grass
                if grass != None:
                    currentShortestDistance =  self.get_position().distance(grass.get_position())
                    if shortestDistance==None or currentShortestDistance< shortestDistance:
                        shortestDistance = currentShortestDistance
                        closestDirtTileWithGrass = x
        return closestDirtTileWithGrass

    def __str__(self):
        return f'Wombat is at position ({self.get_position().x},{self.get_position().y}), energy and speed are {self.energy} and {self.speed} respectively'

    def __repr__(self):
        return f'Wombat({self.get_position().x},{self.get_position().y}): {self.energy}:{self.speed}'

