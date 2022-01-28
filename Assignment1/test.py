import unittest
from main import *


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
