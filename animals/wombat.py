from random import randint
from animals.animal import Animal, OutOfBoundException
from game import Vector2D
from plants.grass import Grass

class Wombat(Animal):
    target= Vector2D(46,46)

    def __init__(self, position, width, height , sourceImage, game,speed, energy):
        super().__init__(position, width, height, sourceImage, game,speed,energy)
        self._energyIncrementValue = 10

    def update(self,timeElapsed):
        self._lifeSpan += timeElapsed

        if(self._lifeSpan >=18):
            self.breedNewWombat()
        self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()
        if(self.isHungry() and self.closestDirtTileWithGrass!=None):
            print("wombat Hungry")
            self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()
            self.target = self.closestDirtTileWithGrass.getPlant().get_position()
            if self.checkIfTargetReached():
                print("closest grass reached")
                self.get_game()._remove_game_obj(self.closestDirtTileWithGrass.getPlant())
                #self.closestDirtTileWithGrass = self.getClosestDirTileWithGrass()
                self.restoreEnergy()
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


    def breedNewWombat(self):
        position = self.get_position()
        x = int(position.x)
        y = int(position.y)
        Wombat(Vector2D(x,y),64,64,self.get_image(),self.get_game(),20,15)
        self._lifeSpan=0

    def checkIfTargetReached(self):
        currentDistance = self.get_position().distance(self.target)
        if(currentDistance<32):
            print("distance", currentDistance)
            return True
        return False

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

