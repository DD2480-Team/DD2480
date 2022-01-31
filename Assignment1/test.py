from importlib.metadata import entry_points
import unittest
from main import *


class CMVCondition0TestCase(unittest.TestCase):
    # must exist one set of two consecutive data points that are further than length1
    # pass two points with dist 5 and and length1 4.5, should return True
    def test1_check_condition_0(self):
        points = [(0, 0), (4, 3)]  # dist is 5
        length1 = 4.5
        self.assertTrue(cmv_condition_0(points, length1))

    # must exist one set of two consecutive data points that are further than length1
    # pass two points with dist 5 and and length1 5.5, should return False
    def test2_check_condition_0(self):
        points = [(0, 0), (4, 3)]  # dist is 5
        length1 = 5.5
        self.assertFalse(cmv_condition_0(points, length1))

    # must exist one set of two consecutive data points that are further than length1
    # pass only one point, should return False
    def test3_check_condition_0(self):
        points = [(0, 0)]  # dist undefined
        length1 = 0
        self.assertFalse(cmv_condition_0(points, length1))

    # must exist one set of two consecutive data points that are further than length1
    # pass negative distance, should return False
    def test4_check_condition_0(self):
        points = [(0, 0), (4, 3)]  # dist is 5
        length1 = -1
        self.assertFalse(cmv_condition_0(points, length1))


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
        points = [
            (1, 2),
            (1, 2),
            (3, 4),
            (1, 2),
            (2, 1),
            (1, 2),
            (3, 3),
            (1, 2),
            (1, 2),
            (3, 1),
        ]
        self.assertFalse(cmv_condition_1(points, 10))

    def test_10_points_outside_circle(self):
        points = [
            (1, 2),
            (1, 2),
            (3, 4),
            (1, 2),
            (2, 1),
            (1, 2),
            (3, 3),
            (1, 2),
            (1, 2),
            (3, 1),
        ]
        self.assertTrue(cmv_condition_1(points, 1))


class CMVCondition2TestCase(unittest.TestCase):
    # if the first point of the angle is the same point as the vertex, return false
    def test_same_points(self):
        points = [(0, 0), (0, 0), (1, 1)]
        epsilon = 0
        self.assertFalse(cmv_condition_2(points, epsilon))

    # if the third point of the angle is the same point as the vertex, return false
    def test_same_points_2(self):
        points = [(0, 1), (25 / 3, 0.0007 / 233003), (25 / 3, 0.0007 / 233003)]
        epsilon = math.pi
        self.assertFalse(cmv_condition_2(points, epsilon))

    # test points form pi/2 rad angle, which falls outside the excluded range [3pi/4, 5pi/4]
    def test_reasonable_epsilon(self):
        points = [(1, 0), (0, 0), (0, 1)]
        epsilon = math.pi / 4
        self.assertTrue(cmv_condition_2(points, epsilon))

    # test points form pi/2 rad angles, which fall inside the excluded range [pi/2, 3pi/2]
    def test_reasonable_epsilon_2(self):
        points = [(1, 0), (0, 0), (0, 1), (-1, 1)]
        epsilon = math.pi / 2
        self.assertFalse(cmv_condition_2(points, epsilon))


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


class CMVCondition4TestCase(unittest.TestCase):
    # points lie in more than QUADS quadrants.
    def test_more_than_quad(self):
        points = [(0, 0), (4, 3), (-1, -1), (2, -3)]
        self.assertTrue(check_condition_4(points, 3, 3))

    # points lie in less than QUADS quadrants.
    def test_less_than_quad(self):
        points = [(0, 0), (-2, 3), (6, 3), (2, 3)]
        self.assertFalse(check_condition_4(points, 2, 3))

    # points lie on axis.
    def test_on_axis(self):
        points = [(1, 0), (0, -1), (-1, 0)]
        self.assertTrue(check_condition_4(points, 3, 3))


""" Must exist at least one set of consecutive data points
    where x-coord of first is larger than x-coord of latter """


class CMVCondition5TestCase(unittest.TestCase):
    # pass list where last element is smaller than second to last, should return True
    def test1_check_condition_5(self):
        points = [(0, 0), (4, 3), (6, 3), (2, 3)]
        self.assertTrue(check_condition_5(points))

    # pass list where x values only grow, should return False
    def test2_check_condition_5(self):
        points = [(0, 0), (4, 3), (6, 3), (40, 3), (50, 3), (60, 3)]
        self.assertFalse(check_condition_5(points))

    # pass list where all x values are the same, should return False
    def test3_check_condition_5(self):
        points = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.assertFalse(check_condition_5(points))

    # pass only one point, should return False
    def test4_check_condition_5(self):
        points = [(0, 0)]  # dist undefined
        self.assertFalse(check_condition_5(points))


class CMVCondition6TestCase(unittest.TestCase):
    # point (4,2) lies distance 3 away from line
    def test_same_begin_end_true_1(self):
        points = [(1, 2), (4, 2), (1, 2)]
        self.assertTrue(cmv_condition_6(points, N_PTS=3, dist=2))

    def test_same_begin_end_false_1(self):
        points = [(1, 2), (4, 2), (1, 2)]
        self.assertFalse(cmv_condition_6(points, N_PTS=3, dist=3))

    def test_same_begin_end_false_2(self):
        points = [(1, 2), (4, 2), (1, 2)]
        self.assertFalse(cmv_condition_6(points, N_PTS=3, dist=4))

    # the distance between any set of 3 consecutive points is 1.0
    # i.e. (3, 3) lies 1 away from the line between (1,2) and (4,2)
    def test_different_begin_end_true_1(self):
        points = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)]
        self.assertTrue(cmv_condition_6(points, N_PTS=3, dist=0.5))

    def test_different_begin_end_false_1(self):
        points = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)]
        self.assertFalse(cmv_condition_6(points, N_PTS=3, dist=1))

    def test_different_begin_end_false_2(self):
        points = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)]
        self.assertFalse(cmv_condition_6(points, N_PTS=3, dist=1.5))


class CMVCondition7TestCase(unittest.TestCase):
    def test_simple_true_case(self):
        points = [(0, 0), (0, 0), (0, 0), (0, 0), (24.5, 0)]
        K_PTS = 3
        length1 = 24.4
        self.assertTrue(cmv_condition_7(points, K_PTS, length1))

    # testing smallest case with three points
    def test_only_three_points(self):
        points = [(0, 0), (0, 0), (11, 0)]
        K_PTS = 1
        length1 = 10.0
        self.assertTrue(cmv_condition_7(points, K_PTS, length1))

    # false if the distance between points is not greater than length
    def test_equal_to_length(self):
        points = [(0, 0), (0, 0), (0, 0), (0, 0), (10, 0)]
        K_PTS = 3
        length1 = 10
        self.assertFalse(cmv_condition_7(points, K_PTS, length1))

    # false if the points aren't K_PTS apart in the array
    def test_not_K_PTS_away(self):
        points = [(0, 0), (0, 0), (0, 0), (100, 0), (0, 0)]
        K_PTS = 3
        length1 = 99.9
        self.assertFalse(cmv_condition_7(points, K_PTS, length1))


class CMVCondition8TestCase(unittest.TestCase):
    def test_points_pass_with_distance_2_begining(self):
        """
        False since all points should fall inside radius 10 circle
        """
        points = [
            (1, 0),
            (3, 0),
            (5, 0),
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
        ]
        self.assertFalse(cmv_condition_8(points, 2, 2, 10, 10))

    def test_points_contained_by_radius1(self):
        """
        Even if a_pts and b_pts work, the radius1 can contain said points.
        """
        points = [
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
            (1, 0),
            (3, 0),
            (5, 0),
        ]
        self.assertFalse(cmv_condition_8(points, 2, 2, 9, 10))

    def test_points_pass_with_distance_2_on_y_axis(self):
        """
        The list is processed and the a and b pts are checked on y axis
        """
        points = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        self.assertTrue(cmv_condition_8(points, 2, 2, 2.99999, 7))

    def test_list_too_short(self):
        """
        The list has less than 5 points
        """
        points = [(-1, -2), (2, 1), (2, 2), (3, 3)]
        self.assertFalse(cmv_condition_8(points, 1, 1, 1.5, 4))

    def test_a_pts_b_pts_too_small(self):
        """
        It should be 1≤A PTS, 1≤B PTS
        """
        points = [
            (1, 0),
            (3, 0),
            (5, 0),
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
        ]
        self.assertFalse(cmv_condition_8(points, 0, 0, 5, 10))

    def test_a_pts_b_pts_too_large(self):
        """
        It should be A PTS+B PTS ≤ (NUMPOINTS−3)
        """
        points = [
            (1, 0),
            (3, 0),
            (5, 0),
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
        ]
        self.assertFalse(cmv_condition_8(points, 15, 19, 5, 10))


class CMVCondition10TestCase(unittest.TestCase):
    # must exist a set of three data points, separated by e_pts and f_pts respectively,
    # that form a triangle with an area greater than area1
    # pass triangle with area=1.0, area1=0.95, should return True
    def test1_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [
            (0, 0),
            (0, 0),
            (1, 1),
            (-4, 5),
            (2, 0),
            (3, 0),
        ]  # triangle: b=2, h=1 => a=1
        area1 = 0.95
        self.assertTrue(cmv_condition_10(points, e_pts, f_pts, area1, len(points)))

    # pass triangle with area=1.0, area1=0.95, should return True
    def test2_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [
            (0, 0),
            (0, 0),
            (1, 1),
            (0, 0),
            (2, 0),
            (0, 0),
        ]  # triangle: b=2, h=1 => a=1
        area1 = 1.05
        self.assertFalse(cmv_condition_10(points, e_pts, f_pts, area1, len(points)))

    # pass triangle with area=1.0, area1=1.0, should return False
    def test3_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [
            (0, 0),
            (0, 0),
            (1, 1),
            (0, 0),
            (2, 0),
            (0, 0),
        ]  # triangle: b=2, h=1 => a=1
        area1 = 1.00
        self.assertFalse(cmv_condition_10(points, e_pts, f_pts, area1, len(points)))

    # pass triangle with too few NUMPOINTS, should return False
    def test4_check_condition_10(self):
        e_pts = 1
        f_pts = 1
        points = [(0, 0), (0, 0), (1, 1), (0, 0), (2, 0)]  # triangle: b=2, h=1 => a=1
        area1 = 0.95
        self.assertFalse(cmv_condition_10(points, e_pts, f_pts, area1, len(points)))


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


class CMVCondition12TestCase(unittest.TestCase):
    def test_simple_true_case(self):
        points = [(0, 0), (0, 0), (0, 0), (0, 0), (10, 0)]
        K_PTS = 3
        length1, length2 = 9.0, 11.01
        self.assertTrue(cmv_condition_12(points, K_PTS, length1, length2))

    # testing smallest case with three points
    def test_only_three_points(self):
        points = [(0, 0), (0, 0), (11, 0)]
        K_PTS = 1
        length1, length2 = 10.0, 12.0
        self.assertTrue(cmv_condition_12(points, K_PTS, length1, length2))

    # false if the distance between points is not less than length2
    def test_equal_to_length(self):
        points = [(0, 0), (0, 0), (0, 0), (0, 0), (10, 0)]
        K_PTS = 3
        length1, length2 = 9, 10
        self.assertFalse(cmv_condition_12(points, K_PTS, length1, length2))

    # false if the points aren't K_PTS apart in the array
    def test_not_K_PTS_away(self):
        points = [(0, 0), (0, 0), (0, 0), (90, 0), (100, 0)]
        K_PTS = 3
        length1, length2 = 99.9, 80
        self.assertFalse(cmv_condition_12(points, K_PTS, length1, length2))


class CMVCondition13TestCase(unittest.TestCase):
    def test_points_fail_with_distance_2_begining(self):
        """
        The 3 first points should fail. Distances are contained by radius 5 and 6.
        """
        points = [
            (1, 0),
            (3, 0),
            (5, 0),
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
        ]
        self.assertFalse(cmv_condition_13(points, 2, 2, 5, 6, len(points)))

    def test_points_fail_on_radius1(self):
        """
        Radius2 = 1 should make the test fail
        """
        points = [
            (1, 0),
            (3, 0),
            (5, 0),
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
        ]
        self.assertFalse(cmv_condition_13(points, 2, 2, 5, 1, len(points)))

    def test_points_fail_on_radius2(self):
        """
        no points aren't contained in radius 2 circle, but some do fall within radius 12
        """
        points = [
            (1, 0),
            (3, 0),
            (5, 0),
            (-1, -2),
            (2, 1),
            (2, 2),
            (3, 3),
            (-2, -2),
            (1, 1),
            (-1, -1),
        ]
        self.assertTrue(cmv_condition_13(points, 2, 2, 2, 12, len(points)))

    def test_not_enough_points(self):
        points = [(1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_13(points, 1, 1, 1.5, 1, len(points)))

    def test_radius2_is_zero(self):
        points = [(1, 0), (3, 0), (5, 0)]
        self.assertFalse(cmv_condition_13(points, 1, 1, 1.5, 0, len(points)))


class CMVCondition14TestCase(unittest.TestCase):
    def test_area_fullfill_condition(self):

        # areas bigger than area1 and smaller than area2

        points = [(2, 4), (1, -6), (5, 8), (0, 0), (2, 9), (-1, 0)]
        self.assertTrue(check_condition_14(points, 1, 1, 5, 7))

    def test_area_smaller_than_area1(self):

        # area bigger than area1 not exists

        points = [(2, 4), (1, -6), (3, 1), (0, 0), (2, 9), (-1, 0)]
        self.assertFalse(check_condition_14(points, 1, 1, 5, 10))

    def test_area_bigger_than_area2(self):

        # area smaller than area2 not exists

        points = [(2, 4), (1, -6), (10, 8), (0, 0), (2, 9), (-10, 0)]
        self.assertFalse(check_condition_14(points, 1, 1, 5, 10))

    def test_area1_or_area2_invalid(self):

        # area1 and area2 should not be 0 or negative

        points = [(2, 4), (1, 1), (1, -6), (5, 8), (2, 2)]
        self.assertFalse(check_condition_14(points, 1, 1, 0, 5))
        self.assertFalse(check_condition_14(points, 1, 1, 5, -1))


if __name__ == "__main__":
    unittest.main()
