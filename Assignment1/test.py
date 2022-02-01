import unittest
from cmv import *
from parser import *


class CMVCondition0TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # must exist one set of two consecutive data points that are further than length1
    # pass two points with dist 5 and and length1 4.5, should return True
    def test1_check_condition_0(self):
        self.CMV.POINTS = [(0, 0), (4, 3)]  # dist is 5
        self.CMV.LENGTH1 = 4.5
        self.assertTrue(self.CMV.cmv_condition_0())

    # must exist one set of two consecutive data points that are further than length1
    # pass two points with dist 5 and and length1 5.5, should return False
    def test2_check_condition_0(self):
        self.CMV.POINTS = [(0, 0), (4, 3)]  # dist is 5
        self.CMV.LENGTH1 = 5.5
        self.assertFalse(self.CMV.cmv_condition_0())

    # must exist one set of two consecutive data points that are further than length1
    # pass only one point, should return False
    def test3_check_condition_0(self):
        self.CMV.POINTS = [(0, 0)]  # dist undefined
        self.CMV.LENGTH1 = 0
        self.assertFalse(self.CMV.cmv_condition_0())


class CMVCondition1TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_points_inside_circle(self):
        # center is (2,2), all points inside circle with radius 3
        self.CMV.POINTS = [(1, 2), (4, 2), (1, 2)]
        self.CMV.RADIUS1 = 3
        self.assertFalse(self.CMV.cmv_condition_1())

    def test_points_outside_circle(self):
        # center is (2,2), point (4,2) lies outside circle with radius 1
        self.CMV.POINTS = [(1, 2), (4, 2), (1, 2)]
        self.CMV.RADIUS1 = 1
        self.assertTrue(self.CMV.cmv_condition_1())

    def test_points_on_circle(self):
        # center is (2,2), point (4,2) lies on the circle with radius 2
        self.CMV.POINTS = [(1, 2), (4, 2), (1, 2)]
        self.CMV.RADIUS1 = 2
        self.assertFalse(self.CMV.cmv_condition_1())

    def test_10_points_inside_circle(self):
        self.CMV.POINTS = [
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
        self.CMV.RADIUS1 = 10
        self.assertFalse(self.CMV.cmv_condition_1())

    def test_10_points_outside_circle(self):
        self.CMV.POINTS = [
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
        self.CMV.RADIUS1 = 1
        self.assertTrue(self.CMV.cmv_condition_1())


class CMVCondition2TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # if the first point of the angle is the same point as the vertex, return false
    def test_same_points(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (1, 1)]
        self.CMV.EPSILON = 0
        self.assertFalse(self.CMV.cmv_condition_2())

    # if the third point of the angle is the same point as the vertex, return false
    def test_same_points_2(self):
        self.CMV.POINTS = [(0, 1), (25 / 3, 0.0007 / 233003), (25 / 3, 0.0007 / 233003)]
        self.CMV.EPSILON = math.pi
        self.assertFalse(self.CMV.cmv_condition_2())

    # test points form pi/2 rad angle, which falls outside the excluded range [3pi/4, 5pi/4]
    def test_reasonable_epsilon(self):
        self.CMV.POINTS = [(1, 0), (0, 0), (0, 1)]
        self.CMV.EPSILON = math.pi / 4
        self.assertTrue(self.CMV.cmv_condition_2())

    # test points form pi/2 rad angles, which fall inside the excluded range [pi/2, 3pi/2]
    def test_reasonable_epsilon_2(self):
        self.CMV.POINTS = [(1, 0), (0, 0), (0, 1), (-1, 1)]
        self.CMV.EPSILON = math.pi / 2
        self.assertFalse(self.CMV.cmv_condition_2())


class CMVCondition3TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_area1_bigger_than_area(self):
        """
        Internal area of 3 consecutive datapoints
        are smaller than than AREA1.
        """
        self.CMV.POINTS = [(2, 4), (1, -6), (5, 8)]
        self.CMV.AREA1 = 20
        self.assertFalse(self.CMV.cmv_condition_3())

    def test_area1_smaller_than_area(self):
        """
        Internal area of 3 consecutive datapoints
        are bigger than than AREA1.
        """
        self.CMV.POINTS = [(2, 4), (1, -6), (5, 8)]
        self.CMV.AREA1 = 5
        self.assertTrue(self.CMV.cmv_condition_3())


class CMVCondition4TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # points lie in more than QUADS quadrants.
    def test_more_than_quad(self):
        self.CMV.POINTS = [(0, 0), (4, 3), (-1, -1), (2, -3)]
        self.CMV.Q_PTS = 3
        self.CMV.QUADS = 3
        self.assertTrue(self.CMV.cmv_condition_4())

    # points lie in less than QUADS quadrants.
    def test_less_than_quad(self):
        self.CMV.POINTS = [(0, 0), (-2, 3), (6, 3), (2, 3)]
        self.CMV.Q_PTS = 2
        self.CMV.QUADS = 3
        self.assertFalse(self.CMV.cmv_condition_4())

    # points lie on axis.
    def test_on_axis(self):
        self.CMV.POINTS = [(1, 0), (0, -1), (-1, 0)]
        self.CMV.Q_PTS = 3
        self.CMV.QUADS = 3
        self.assertTrue(self.CMV.cmv_condition_4())


""" Must exist at least one set of consecutive data points
    where x-coord of first is larger than x-coord of latter """


class CMVCondition5TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # pass list where last element is smaller than second to last, should return True
    def test1_check_condition_5(self):
        self.CMV.POINTS = [(0, 0), (4, 3), (6, 3), (2, 3)]
        self.assertTrue(self.CMV.cmv_condition_5())

    # pass list where x values only grow, should return False
    def test2_check_condition_5(self):
        self.CMV.POINTS = [(0, 0), (4, 3), (6, 3), (40, 3), (50, 3), (60, 3)]
        self.assertFalse(self.CMV.cmv_condition_5())

    # pass list where all x values are the same, should return False
    def test3_check_condition_5(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.assertFalse(self.CMV.cmv_condition_5())

    # pass only one point, should return False
    def test4_check_condition_5(self):
        self.CMV.POINTS = [(0, 0)]  # dist undefined
        self.assertFalse(self.CMV.cmv_condition_5())


class CMVCondition6TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # point (4,2) lies distance 3 away from line
    def test_same_begin_end_true_1(self):
        self.CMV.POINTS = [(1, 2), (4, 2), (1, 2)]
        self.CMV.N_PTS = 3
        self.CMV.DIST = 2
        self.assertTrue(self.CMV.cmv_condition_6())

    def test_same_begin_end_false_1(self):
        self.CMV.POINTS = [(1, 2), (4, 2), (1, 2)]
        self.CMV.N_PTS = 3
        self.CMV.DIST = 3
        self.assertFalse(self.CMV.cmv_condition_6())

    def test_same_begin_end_false_2(self):
        self.CMV.POINTS = [(1, 2), (4, 2), (1, 2)]
        self.CMV.N_PTS = 3
        self.CMV.DIST = 4
        self.assertFalse(self.CMV.cmv_condition_6())

    # the distance between any set of 3 consecutive points is 1.0
    # i.e. (3, 3) lies 1 away from the line between (1,2) and (4,2)
    def test_different_begin_end_true_1(self):
        self.CMV.POINTS = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)]
        self.CMV.N_PTS = 3
        self.CMV.DIST = 0.5
        self.assertTrue(self.CMV.cmv_condition_6())

    def test_different_begin_end_false_1(self):
        self.CMV.POINTS = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)]
        self.CMV.N_PTS = 3
        self.CMV.DIST = 1
        self.assertFalse(self.CMV.cmv_condition_6())

    def test_different_begin_end_false_2(self):
        self.CMV.POINTS = [(1, 2), (3, 3), (4, 2), (6, 3), (1, 2)]
        self.CMV.N_PTS = 3
        self.CMV.DIST = 1.5
        self.assertFalse(self.CMV.cmv_condition_6())


class CMVCondition7TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_simple_true_case(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (0, 0), (24.5, 0)]
        self.CMV.K_PTS = 3
        self.CMV.LENGTH1 = 24.4
        self.assertTrue(self.CMV.cmv_condition_7())

    # testing smallest case with three points
    def test_only_three_points(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (11, 0)]
        self.CMV.K_PTS = 1
        self.CMV.LENGTH1 = 10.0
        self.assertTrue(self.CMV.cmv_condition_7())

    # false if the distance between points is not greater than length
    def test_equal_to_length(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (0, 0), (10, 0)]
        self.CMV.K_PTS = 3
        self.CMV.LENGTH1 = 10
        self.assertFalse(self.CMV.cmv_condition_7())

    # false if the points aren't K_PTS apart in the array
    def test_not_K_PTS_away(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (100, 0), (0, 0)]
        self.CMV.K_PTS = 3
        self.CMV.LENGTH1 = 99.9
        self.assertFalse(self.CMV.cmv_condition_7())


class CMVCondition8TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_points_pass_with_distance_2_begining(self):
        """
        False since all points should fall inside radius 10 circle
        """
        self.CMV.POINTS = [
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

        self.CMV.A_PTS = 2
        self.CMV.B_PTS = 2
        self.CMV.RADIUS1 = 10
        self.assertFalse(self.CMV.cmv_condition_8())

    def test_points_contained_by_radius1(self):
        """
        Even if a_pts and b_pts work, the radius1 can contain said points.
        """
        self.CMV.POINTS = [
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
        self.CMV.A_PTS = 2
        self.CMV.B_PTS = 2
        self.CMV.RADIUS1 = 9
        self.assertFalse(self.CMV.cmv_condition_8())

    def test_points_pass_with_distance_2_on_y_axis(self):
        """
        The list is processed and the a and b pts are checked on y axis
        """
        self.CMV.POINTS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        self.CMV.A_PTS = 2
        self.CMV.B_PTS = 2
        self.CMV.RADIUS1 = 2.99999
        self.assertTrue(self.CMV.cmv_condition_8())

    def test_list_too_short(self):
        """
        The list has less than 5 points
        """
        self.CMV.POINTS = [(-1, -2), (2, 1), (2, 2), (3, 3)]
        self.CMV.A_PTS = 1
        self.CMV.B_PTS = 1
        self.CMV.RADIUS1 = 1.5
        self.assertFalse(self.CMV.cmv_condition_8())


class CMVCondition9TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # angle falls outside the excluded range
    def test_outside_angle(self):
        self.CMV.POINTS = [(3, 0), (2, -1), (0, 0), (-1, -1), (3, -8), (0, 7), (20, 0)]
        self.CMV.C_PTS = 1
        self.CMV.D_PTS = 2
        self.CMV.EPSILON = (math.pi * 3) / 4
        self.assertTrue(self.CMV.cmv_condition_9())

    # angle falls inside the excluded range
    def test_inside_angle(self):
        self.CMV.POINTS = [(3, 0), (2, -1), (0, 0), (-1, -1), (3, -8), (0, 7), (-2, 0)]
        self.CMV.C_PTS = 1
        self.CMV.D_PTS = 2
        self.CMV.EPSILON = (math.pi * 3) / 4
        self.assertFalse(self.CMV.cmv_condition_9())

    # points have coincidence
    def test_points_coincidence(self):
        self.CMV.POINTS = [(0, 0), (-3, 9), (0, 2), (-3, 9), (0, 2), (-1, -2)]
        self.CMV.C_PTS = 1
        self.CMV.D_PTS = 1
        self.CMV.EPSILON = math.pi / 2
        self.assertFalse(self.CMV.cmv_condition_9())

    # points are not enough to be seperate by C_PTS points and D_PTS points
    def test_points_not_enough(self):
        self.CMV.POINTS = [(0, 0), (0, 2), (3, 1), (4, 5)]
        self.CMV.C_PTS = 1
        self.CMV.D_PTS = 1
        self.CMV.EPSILON = math.pi / 2
        self.assertFalse(self.CMV.cmv_condition_9())


class CMVCondition10TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # must exist a set of three data points, separated by e_pts and f_pts respectively,
    # that form a triangle with an area greater than area1
    # pass triangle with area=1.0, area1=0.95, should return True
    def test1_check_condition_10(self):
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        self.CMV.POINTS = [
            (0, 0),
            (0, 0),
            (1, 1),
            (-4, 5),
            (2, 0),
            (3, 0),
        ]  # triangle: b=2, h=1 => a=1
        self.CMV.AREA1 = 0.95
        self.assertTrue(self.CMV.cmv_condition_10())

    # pass triangle with area=1.0, area1=0.95, should return True
    def test2_check_condition_10(self):
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        points = [
            (0, 0),
            (0, 0),
            (1, 1),
            (0, 0),
            (2, 0),
            (0, 0),
        ]  # triangle: b=2, h=1 => a=1
        self.CMV.AREA1 = 1.05
        self.assertTrue(self.CMV.cmv_condition_10())

    # pass triangle with area=1.0, area1=1.0, should return False
    def test3_check_condition_10(self):
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        self.CMV.POINTS = [
            (0, 0),
            (0, 0),
            (1, 1),
            (0, 0),
            (2, 0),
            (0, 0),
        ]  # triangle: b=2, h=1 => a=1
        self.CMV.AREA1 = 1.00
        self.assertFalse(self.CMV.cmv_condition_10())

    # pass triangle with too few NUMPOINTS, should return False
    def test4_check_condition_10(self):
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        self.CMV.POINTS = [(0, 0), (0, 0), (1, 1), (2, 0)]  # triangle: b=2, h=1 => a=1
        self.CMV.AREA1 = 0.95
        self.assertFalse(self.CMV.cmv_condition_10())


class CMVCondition11TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    # begin and end points are the same, and are G_PTS = 2 apart
    def test_false_1(self):
        self.CMV.POINTS = [(1, 2), (4, 2), (3, 1), (1, 2)]
        self.CMV.G_PTS = 2
        self.assertFalse(self.CMV.cmv_condition_11())

    # increasing sequence of x-coordinates
    def test_false_2(self):
        self.CMV.POINTS = [(1, 2), (2, 3), (3, 1), (4, 2), (5, 2)]
        self.CMV.G_PTS = 2
        self.assertFalse(self.CMV.cmv_condition_11())

    # x-coordinate of (-1, 2) < (1, 2)
    def test_true_1(self):
        self.CMV.POINTS = [(1, 2), (4, 2), (3, 1), (-1, 2)]
        self.CMV.G_PTS = 2
        self.assertTrue(self.CMV.cmv_condition_11())

    # x -coordinate of (-1, 2) < (4, 2)
    def test_true_2(self):
        self.CMV.POINTS = [(1, 2), (4, 2), (3, 1), (-1, 2)]
        self.CMV.G_PTS = 1
        self.assertTrue(self.CMV.cmv_condition_11())


class CMVCondition12TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_simple_true_case(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (0, 0), (10, 0)]
        self.CMV.K_PTS = 3
        self.CMV.LENGTH1, self.CMV.LENGTH2 = 9.0, 11.01
        self.assertTrue(self.CMV.cmv_condition_12())

    # testing smallest case with three points
    def test_only_three_points(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (11, 0)]
        self.CMV.K_PTS = 1
        self.CMV.LENGTH1, self.CMV.LENGTH2 = 10.0, 12.0
        self.assertTrue(self.CMV.cmv_condition_12())

    # false if the distance between points is not less than length2
    def test_equal_to_length(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (0, 0), (10, 0)]
        self.CMV.K_PTS_PTS = 3
        self.CMV.LENGTH1, self.CMV.LENGTH2 = 9, 10
        self.assertFalse(self.CMV.cmv_condition_12())

    # false if the points aren't K_PTS apart in the array
    def test_not_K_PTS_away(self):
        self.CMV.POINTS = [(0, 0), (0, 0), (0, 0), (90, 0), (100, 0)]
        self.CMV.K_PTS = 3
        self.CMV.LENGTH1, self.CMV.LENGTH2 = 99.9, 80
        self.assertFalse(self.CMV.cmv_condition_12())


class CMVCondition13TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_points_fail_with_distance_2_begining(self):
        """
        The 3 first points should fail. Distances are contained by radius 5 and 6.
        """
        self.CMV.POINTS = [
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
        self.CMV.A_PTS = 2
        self.CMV.B_PTS = 2
        self.CMV.RADIUS1 = 5
        self.CMV.RADIUS2 = 6
        self.assertFalse(self.CMV.cmv_condition_13())

    def test_points_fail_on_radius1(self):
        """
        Radius2 = 1 should make the test fail
        """
        self.CMV.POINTS = [
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
        self.CMV.A_PTS = 2
        self.CMV.B_PTS = 2
        self.CMV.RADIUS1 = 5
        self.CMV.RADIUS2 = 1
        self.assertFalse(self.CMV.cmv_condition_13())

    def test_points_fail_on_radius2(self):
        """
        no points aren't contained in radius 2 circle, but some do fall within radius 12
        """
        self.CMV.POINTS = [
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
        self.CMV.A_PTS = 2
        self.CMV.B_PTS = 2
        self.CMV.RADIUS1 = 2
        self.CMV.RADIUS2 = 12
        self.assertTrue(self.CMV.cmv_condition_13())

    def test_not_enough_points(self):
        self.CMV.POINTS = [(1, 0), (3, 0), (5, 0)]
        self.CMV.A_PTS = 1
        self.CMV.B_PTS = 1
        self.CMV.RADIUS1 = 1.5
        self.CMV.RADIUS2 = 1
        self.assertFalse(self.CMV.cmv_condition_13())

    def test_radius2_is_zero(self):
        self.CMV.POINTS = [(1, 0), (3, 0), (5, 0)]
        self.CMV.A_PTS = 1
        self.CMV.B_PTS = 1
        self.CMV.RADIUS1 = 1.5
        self.CMV.RADIUS2 = 0
        self.assertFalse(self.CMV.cmv_condition_13())


class CMVCondition14TestCase(unittest.TestCase):
    def setUp(self):
        self.CMV = read_CMV_PUV_LCM_from_file()

    def test_area_fullfill_condition(self):

        # areas bigger than area1 and smaller than area2

        self.CMV.POINTS = [(2, 4), (1, -6), (5, 8), (0, 0), (2, 9), (-1, 0)]
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        self.CMV.AREA1 = 5
        self.CMV.AREA2 = 7
        self.assertTrue(self.CMV.cmv_condition_14())

    def test_area_smaller_than_area1(self):

        # area bigger than area1 not exists

        self.CMV.POINTS = [(2, 4), (1, -6), (3, 1), (0, 0), (2, 9), (-1, 0)]
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        self.CMV.AREA1 = 5
        self.CMV.AREA2 = 10
        self.assertFalse(self.CMV.cmv_condition_14())

    def test_area_bigger_than_area2(self):

        # area smaller than area2 not exists

        self.CMV.POINTS = [(2, 4), (1, -6), (10, 8), (0, 0), (2, 9), (-10, 0)]
        self.CMV.E_PTS = 1
        self.CMV.F_PTS = 1
        self.CMV.AREA1 = 5
        self.CMV.AREA2 = 10
        self.assertFalse(self.CMV.cmv_condition_14())


if __name__ == "__main__":
    unittest.main()
