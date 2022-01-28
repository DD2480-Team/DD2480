import unittest
from main import *


class CMVCondition8TestCase(unittest.TestCase):
    def test_points_pass_with_distance_2_begining(self):
        """
        The 3 first points should pass the test.
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertTrue(cmv_condition_8(points, 2, 2, 1.5))

    def test_points_pass_with_distance_2_end(self):
        """
        The list is processed and the 3 last points should pass the test.
        """
        points = [(-1, -2), (2, 1), (2, 2), (3, 3), (-2, -2),
                  (1, 1), (-1, -1), (1, 0), (3, 0), (5, 0)]
        self.assertTrue(cmv_condition_8(points, 2, 2, 1.5))

    def test_points_contained_by_radius1(self):
        """
        Even if a_pts and b_pts work, the radius1 can contain said points.
        """
        points = [(-1, -2), (2, 1), (2, 2), (3, 3), (-2, -2),
                  (1, 1), (-1, -1), (1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 9))

    def test_points_pass_with_distance_2_on_y_axis(self):
        """
        The list is processed and the a and b pts are checked on y axis
        """
        points = [(-1, -2), (2, 1), (2, 2), (3, 3), (-2, -2),
                  (1, 1), (-1, -1), (0, 1), (0, 3), (0, 5)]
        self.assertTrue(cmv_condition_8(points, 2, 2, 1.5))

    def test_list_too_short(self):
        """
        The list has less than 5 points
        """
        points = [(-1, -2), (2, 1), (2, 2)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 1.5))

    def test_points_contained_by_large_radius(self):
        """
        The points should be contained by a radius 15 pts
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_8(points, 2, 2, 15))

    def test_a_pts_b_pts_too_small(self):
        """
        It should be 1≤A PTS, 1≤B PTS
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_8(points, 0, 0, 5))

    def test_a_pts_b_pts_too_small(self):
        """
        It should be A PTS+B PTS ≤ (NUMPOINTS−3)
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_8(points, 15, 19, 5))
