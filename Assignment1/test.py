import unittest
from main import *

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
    
if __name__ == '__main__':
    unittest.main()

