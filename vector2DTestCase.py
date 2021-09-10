import unittest
from game import *

class vector2dTest(unittest.TestCase):

    def testAdd(self):
        vec1 = Vector2D(10,10)
        vec2 = Vector2D(20,10)
        result = vec1.add(vec2)
        self.assertEqual(result, Vector2D(30,20))

    #negative test case
    def testAddNotEqual(self):
        vec1 = Vector2D(10,10)
        vec2 = Vector2D(20,10)
        result = vec1.add(vec2)
        self.assertNotEqual(result, Vector2D(30,10))
    
    def testSubstract(self):
        vec1 = Vector2D(10,10)
        vec2 = Vector2D(20,10)
        result = vec1.subtract(vec2)
        self.assertEqual(result, Vector2D(-10,0))

    def testSubstractNotEqual(self):
        vec1 = Vector2D(10,10)
        vec2 = Vector2D(20,10)
        result = vec1.subtract(vec2)
        self.assertNotEqual(result, Vector2D(10,0))

    def testScale(self):
        vec1 = Vector2D(10,10)
        result = vec1.scale(2)
        self.assertEqual(result, Vector2D(20,20))
    
    def testScaleNotEqual(self):
        vec1 = Vector2D(10,10)
        result = vec1.scale(2)
        self.assertNotEqual(result, Vector2D(10,20))
    
    def testLength(self):
        vec1 = Vector2D(4,3)
        result = vec1.length()
        self.assertEqual(result, 5.0)
    
    def testLengthNotEqual(self):
        vec1 = Vector2D(4,3)
        result = vec1.length()
        self.assertNotEqual(result, 4)
    
    def testDistance(self):
        vec1 = Vector2D(4,1)
        vec2 = Vector2D(8,4)
        result = vec1.distance(vec2)
        self.assertEqual(result, 5.0)

    def testDistanceNotEqual(self):
        vec1 = Vector2D(4,1)
        vec2 = Vector2D(8,4)
        result = vec1.distance(vec2)
        self.assertNotEqual(result, 4)

    def testNormalize(self):
        vec1 = Vector2D(0,192)
        result = vec1.normalize()
        self.assertEqual(result.x, 0.0)
        self.assertEqual(result.y, 1.0)
    
    def testNormalizeNotEqual(self):
        vec1 = Vector2D(0,192)
        result = vec1.normalize()
        self.assertEqual(result.x, 0.0)
        self.assertNotEqual(result.y, 2.0)
    
unittest.main()