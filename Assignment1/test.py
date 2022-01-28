import unittest
from main import *

class CMVCondition11TestCase(unittest.TestCase):
    # begin and end points are the same, and are G_PTS = 2 apart
    def test_false_1(self):
        points = [(1, 2), (4, 2), (3, 1), (1, 2)] 
        self.assertFalse(cmv_condition_11(points, G_PTS=2))
    # increasing sequence of x-coordinates
    def test_false_2(self):
        points = [(1, 2), (2, 3), (3, 1), (4, 2), (5, 2)] 
        self.assertFalse(cmv_condition_11(points, G_PTS=2))
    # x-coordinate of (-1, 2) < (1, 2)
    def test_true_1(self):
        points = [(1, 2), (4, 2), (3, 1), (-1, 2)] 
        self.assertTrue(cmv_condition_11(points, G_PTS=2))
    # x -coordinate of (-1, 2) < (4, 2)
    def test_true_2(self):
        points = [(1, 2), (4, 2), (3, 1), (-1, 2)] 
        self.assertTrue(cmv_condition_11(points, G_PTS=1))