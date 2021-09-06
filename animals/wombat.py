from random import randint
from animals.animal import Animal
from game import Vector2D
from plants.grass import Grass

class OutOfBoundException(Exception):
    """Base class for other exceptions"""
    pass

class Wombat(Animal):
    target= Vector2D(46,46)

    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game,speed,energy)
        self._maxEnergy=energy

    def restoreEnergy(self,energyIncrementValue):
        if(self.energy + energyIncrementValue <= self._maxEnergy):
            self.energy += energyIncrementValue

    def reduceEnergy(self,timeElapsed):
        self.energy -= timeElapsed
        if self.energy<=0:
            self.destroy()       

    def update(self,timeElapsed):
        if(self.isHungry()):
            print("wombat Hungry")
            self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()
            if(self.closestDirtTileWithGrass == None):
                print("grass finsidhed")
            else:
                self.target = self.closestDirtTileWithGrass.getPlant().get_position()
                if self.checkIfTargetReached():
                    print("closest grass reached")
                    self.get_game()._remove_game_obj(self.closestDirtTileWithGrass.getPlant())
                    #self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()
                    self.restoreEnergy(10)
                    if(self.closestDirtTileWithGrass == None):
                        return
                    else:  
                        #self.target = self.closestDirtTileWithGrass.getPlant().get_position()
                        self.closestDirtTileWithGrass.setPlant(None) 
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
        trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
        self.move_by(trajectory.x, trajectory.y)
        self.reduceEnergy(timeElapsed)


    def checkIfTargetReached(self):
        currentDistance = self.get_position().distance(self.target)
        if(currentDistance<32):
            print("distance", currentDistance)
            return True
        return False

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
    
    def getClosestDirTileWithGrass(self):
        dirtTiles = self.get_game().getDirtTiles()
        closestDirtTileWithGrass = None
        shortestDistance =  10000
        for x in dirtTiles:
            grass = x.getPlant()
            if isinstance(grass,Grass):
                if grass != None:
                    currentShortestDistance =  self.get_position().distance(grass.get_position())
                    if currentShortestDistance< shortestDistance:
                        shortestDistance = currentShortestDistance
                        closestDirtTileWithGrass = x
        return closestDirtTileWithGrass

