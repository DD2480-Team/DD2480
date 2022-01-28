import unittest
from main import *

class CMVCondition7TestCase(unittest.TestCase):

    def test_simple_true_case(self):
        points = [(0,0), (0,0), (0,0), (0,0), (24.5,0)]
        K_PTS = 3
        length1 = 24.4
        self.assertTrue(cmv_condition_7(points, K_PTS, length1))
    
    #testing smallest case with three points 
    def test_only_three_points(self):
        points = [(0,0), (0,0), (11,0)]
        K_PTS = 1
        length1 = 10.0
        self.assertTrue(cmv_condition_7(points, K_PTS, length1))

    #false if the distance between points is not greater than length
    def test_equal_to_length(self):
        points = [(0,0), (0,0), (0,0), (0,0), (10,0)]
        K_PTS = 3
        length1 = 10
        self.assertFalse(cmv_condition_7(points, K_PTS, length1))
    
    #false if the points aren't K_PTS apart in the array
    def test_not_K_PTS_away(self):
        points = [(0,0), (0,0), (0,0), (100,0), (0,0)]
        K_PTS = 3
        length1 = 99.9
        self.assertFalse(cmv_condition_7(points, K_PTS, length1))

if __name__ == "__main__":
    unittest.main()