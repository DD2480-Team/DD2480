import unittest
from main import *


class CMVCondition8TestCase(unittest.TestCase):

    """[summary]
    """

    def test_points_pass_with_distance_2_begining(self):
        """
        The 3 first points should pass the test. Distances 2 and 2 are exceeding radius 1 and 2
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertTrue(cmv_condition_8(points, 2, 2, 1.5, 1))

    def test_points_fail_with_distance_2_begining(self):
        """
        The 3 first points should fail. Distances are contained by radius 5 and 6.
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 5, 6))

    def test_points_fail_on_radius1(self):
        """
        Radius 1 should make the test fail
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 5, 1))

    def test_points_fail_on_radius2(self):
        """
        Radius 2 should make the test fail
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 1, 12))

    def test_not_enough_points(self):
        points = [(1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 1.5, 1))

    def test_radius2_is_zero(self):
        points = [(1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 1.5, 0))
