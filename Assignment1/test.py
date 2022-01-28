import unittest
from main import *

class CMVCondition0TestCase(unittest.TestCase):
    #must exist one set of two consecutive data points that are further than length1
    #pass two points with dist 5 and and length1 4.5, should return True
    def test1_check_condition_0(self):
        points = [(0,0),(4,3)]  #dist is 5
        length1 = 4.5
        self.assertTrue(check_condition_0(points, length1))

    #must exist one set of two consecutive data points that are further than length1
    #pass two points with dist 5 and and length1 5.5, should return False
    def test2_check_condition_0(self):
        points = [(0,0),(4,3)]  #dist is 5
        length1 = 5.5
        self.assertFalse(check_condition_0(points, length1))

    #must exist one set of two consecutive data points that are further than length1
    #pass only one point, should return False
    def test3_check_condition_0(self):
        points = [(0,0)]  #dist undefined
        length1 = 0
        self.assertFalse(check_condition_0(points, length1))

    #must exist one set of two consecutive data points that are further than length1
    #pass negative distance, should return False
    def test4_check_condition_0(self):
        points = [(0,0),(4,3)]  #dist is 5
        length1 = -1
        self.assertFalse(check_condition_0(points, length1))

""" Must exist at least one set of consecutive data points
    where x-coord of first is larger than x-coord of latter """
class CMVCondition5TestCase(unittest.TestCase):
    #pass list where last element is smaller than second to last, should return True
    def test1_check_condition_5(self):
        points = [(0,0),(4,3),(6,3),(2,3)]  
        self.assertTrue(check_condition_5(points))

    #pass list where x values only grow, should return False
    def test2_check_condition_5(self):
        points = [(0,0),(4,3),(6,3),(40,3),(50,3),(60,3)]  
        self.assertFalse(check_condition_5(points))

    #pass list where all x values are the same, should return False
    def test3_check_condition_5(self):
        points = [(0,0),(0,0),(0,0),(0,0),(0,0)]  
        self.assertFalse(check_condition_5(points))

    #pass only one point, should return False
    def test4_check_condition_5(self):
        points = [(0,0)]  #dist undefined
        self.assertFalse(check_condition_5(points))

if __name__ == '__main__':
    unittest.main()
