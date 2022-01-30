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


class CMVCondition1TestCase(unittest.TestCase):
    def test_points_inside_circle(self):
        # center is (2,2), all points inside circle with radius 3
        points = [(1, 2), (4, 2), (1, 2)] 
        self.assertFalse(cmv_condition_1(points, 3))
    def test_points_outside_circle(self):
        # center is (2,2), point (4,2) lies outside circle with radius 1
        points = [(1, 2), (4, 2), (1, 2)] 
        self.assertTrue(cmv_condition_1(points, 1))
    def test_points_on_circle(self):
        # center is (2,2), point (4,2) lies on the circle with radius 2
        points = [(1, 2), (4, 2), (1, 2)] 
        self.assertFalse(cmv_condition_1(points, 2))
    def test_10_points_inside_circle(self):
         points = [(1, 2), (1, 2), (3, 4), (1, 2), (2, 1), (1, 2), (3, 3), (1, 2), (1, 2), (3, 1)]
         self.assertFalse(cmv_condition_1(points, 10))
    def test_10_points_outside_circle(self):
         points = [(1, 2), (1, 2), (3, 4), (1, 2), (2, 1), (1, 2), (3, 3), (1, 2), (1, 2), (3, 1)]
         self.assertTrue(cmv_condition_1(points, 1))
    

class CMVCondition3TestCase(unittest.TestCase):
    def test_area1_bigger_than_area(self):
        """
        Internal area of 3 consecutive datapoints 
        are smaller than than AREA1.
        """
        points = [(2, 4), (1, -6), (5, 8)]
        self.assertFalse(cmv_condition_3(points, 20))

    def test_area1_smaller_than_area(self):
        """
        Internal area of 3 consecutive datapoints 
        are bigger than than AREA1.
        """
        points = [(2, 4), (1, -6), (5, 8)]
        self.assertTrue(cmv_condition_3(points, 5))

    def test_area1_equals_zero(self):
        """
        AREA1 should not be 0 or negative
        """
        points = [(2, 4), (1, -6), (5, 8)]
        self.assertFalse(cmv_condition_3(points, 0))


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

class CMVCondition9TestCase(unittest.TestCase):

    # angle falls outside the excluded range
    def test_outside_angle(self):
        points = [(3, 0) , (2, -1), (0, 0), (-1, -1), (3, -8), (0, 7), (20, 0)]
        self.assertTrue(check_condition_9(points, 1, 2, (math.pi * 3)/4))

    # angle falls inside the excluded range
    def test_inside_angle(self):
        points = [(3, 0) , (2, -1), (0, 0), (-1, -1), (3, -8), (0, 7), (-2, 0)]
        self.assertFalse(check_condition_9(points, 1, 2, (math.pi * 3)/4))

    # points have coincidence
    def test_points_coincidence(self):
        points = [(0, 0), (-3, 9), (0, 2), (-3, 9), (0, 2), (-1, -2)]
        self.assertFalse(check_condition_9(points, 1, 1, math.pi/2))

    # points are not enough to be seperate by C_PTS points and D_PTS points
    def test_points_not_enough(self):
        points = [(0, 0), (0, 2), (3, 1), (4, 5)]
        self.assertFalse(check_condition_9(points, 1, 1, math.pi/2))
        

if __name__ == '__main__':
    unittest.main()