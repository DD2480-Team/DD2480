from importlib.metadata import entry_points
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

class CMVCondition10TestCase(unittest.TestCase):
    # must exist a set of three data points, separated by e_pts and f_pts respectively,
    # that form a triangle with an area greater than area1
    # pass triangle with area=1.0, area1=0.95, should return True
    def test1_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [(0,0), (0,0), (1,1), (-4,5), (2, 0), (3, 0)] #triangle: b=2, h=1 => a=1
        area1 = 0.95
        self.assertTrue(check_condition_10(points, e_pts, f_pts, area1, len(points)))
    # pass triangle with area=1.0, area1=0.95, should return True
    def test2_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [(0,0), (0,0), (1,1), (0,0), (2, 0), (0, 0)] #triangle: b=2, h=1 => a=1
        area1 = 1.05
        self.assertFalse(check_condition_10(points, e_pts, f_pts, area1, len(points)))
    # pass triangle with area=1.0, area1=1.0, should return False
    def test3_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [(0,0), (0,0), (1,1), (0,0), (2, 0), (0, 0)] #triangle: b=2, h=1 => a=1
        area1 = 1.00
        self.assertFalse(check_condition_10(points, e_pts, f_pts, area1, len(points)))
    # pass triangle with too few NUMPOINTS, should return False
    def test4_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [(0,0), (0,0), (1,1), (0,0), (2, 0)] #triangle: b=2, h=1 => a=1
        area1 = 0.95
        self.assertFalse(check_condition_10(points, e_pts, f_pts, area1, len(points)))

if __name__ == '__main__':
    unittest.main()
