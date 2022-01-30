import unittest
from main import *


class CMVCondition13TestCase(unittest.TestCase):

    def test_points_fail_with_distance_2_begining(self):
        """
        The 3 first points should fail. Distances are contained by radius 5 and 6.
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_13(points, 2, 2, 5, 6, len(points)))

    def test_points_fail_on_radius1(self):
        """
        Radius2 = 1 should make the test fail
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertFalse(cmv_condition_13(points, 2, 2, 5, 1, len(points)))

    def test_points_fail_on_radius2(self):
        """
        no points aren't contained in radius 2 circle, but some do fall within radius 12
        """
        points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
                  (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
        self.assertTrue(cmv_condition_13(points, 2, 2, 2, 12, len(points)))

    def test_not_enough_points(self):
        points = [(1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_13(points, 1, 1, 1.5, 1, len(points)))

    def test_radius2_is_zero(self):
        points = [(1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_13(points, 1, 1, 1.5, 0, len(points)))

if __name__ == "__main__":
    unittest.main()
