import unittest
from main import *

class CMVCondition6TestCase(unittest.TestCase):
    # point (4,2) lies distance 3 away from line
    def test_same_begin_end_true_1(self):
        points = [(1, 2), (4, 2), (1, 2)] 
        self.assertTrue(cmv_condition_6(points, N_PTS = 3, dist = 2))
    def test_same_begin_end_false_1(self):
        points = [(1, 2), (4, 2), (1, 2)] 
        self.assertFalse(cmv_condition_6(points, N_PTS = 3, dist = 3))
    def test_same_begin_end_false_2(self):
        points = [(1, 2), (4, 2), (1, 2)] 
        self.assertFalse(cmv_condition_6(points, N_PTS = 3, dist = 4))
    # the distance between any set of 3 consecutive points is 1.0
    # i.e. (3, 3) lies 1 away from the line between (1,2) and (4,2)
    def test_different_begin_end_true_1(self):
        points = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)] 
        self.assertTrue(cmv_condition_6(points, N_PTS = 3, dist = 0.5))
    def test_different_begin_end_false_1(self):
        points = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)] 
        self.assertFalse(cmv_condition_6(points, N_PTS = 3, dist = 1))
    def test_different_begin_end_false_2(self):
        points = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)] 
        self.assertFalse(cmv_condition_6(points, N_PTS = 3, dist = 1.5))

if __name__ == '__main__':
    unittest.main()