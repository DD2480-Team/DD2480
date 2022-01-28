import unittest
from main import *

class CMVCondition2TestCase(unittest.TestCase):
    # if the first point of the angle is the same point as the vertex, return false
    def test_same_points(self):
        points = [(0,0),(0,0),(1,1)]
        epsilon = 0
        self.assertFalse(cmv_condition_2(points, epsilon))

    #if the third point of the angle is the same point as the vertex, return false
    def test_same_points_2(self):
        points = [(0,1),(25/3,.0007/233003),(25/3,.0007/233003)]
        epsilon = math.pi
        self.assertFalse(cmv_condition_2(points, epsilon))
    
    #test points form pi/2 rad angle, which falls outside the excluded range [3pi/4, 5pi/4]
    def test_reasonable_epsilon(self):
        points = [(1,0), (0,0), (0,1)]
        epsilon = math.pi/4
        self.assertTrue(cmv_condition_2(points, epsilon))
    
     #test points form pi/2 rad angles, which fall inside the excluded range [pi/2, 3pi/2]
    def test_reasonable_epsilon_2(self):
        points = [(1,0), (0,0), (0,1), (-1,1)]
        epsilon = math.pi/2
        self.assertFalse(cmv_condition_2(points, epsilon))

if __name__ == "__main__":
    unittest.main()
