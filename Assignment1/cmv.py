import math
import numpy as np
from utils import *


class CMV:
    def __init__(
        self,
        NUMPOINTS,
        POINTS,
        LENGTH1,
        RADIUS1,
        EPSILON,
        AREA1,
        Q_PTS,
        QUADS,
        DIST,
        N_PTS,
        K_PTS,
        A_PTS,
        B_PTS,
        C_PTS,
        D_PTS,
        E_PTS,
        F_PTS,
        G_PTS,
        LENGTH2,
        RADIUS2,
        AREA2,
        LCM,
        PUV,
    ):
        self.NUMPOINTS = NUMPOINTS
        self.POINTS = POINTS
        self.LENGTH1 = LENGTH1
        self.RADIUS1 = RADIUS1
        self.EPSILON = EPSILON
        self.AREA1 = AREA1
        self.Q_PTS = Q_PTS
        self.QUADS = QUADS
        self.DIST = DIST
        self.N_PTS = N_PTS
        self.K_PTS = K_PTS
        self.A_PTS = A_PTS
        self.B_PTS = B_PTS
        self.C_PTS = C_PTS
        self.D_PTS = D_PTS
        self.E_PTS = E_PTS
        self.F_PTS = F_PTS
        self.G_PTS = G_PTS
        self.LENGTH2 = LENGTH2
        self.RADIUS2 = RADIUS2
        self.AREA2 = AREA2
        self.LCM = LCM
        self.PUV = PUV
        self.CMV_VECTOR = self.generate_vector()

    def generate_vector(self):
        return [
            self.cmv_condition_0(),
            self.cmv_condition_1(),
            self.cmv_condition_2(),
            self.cmv_condition_3(),
            self.cmv_condition_4(),
            self.cmv_condition_5(),
            self.cmv_condition_6(),
            self.cmv_condition_7(),
            self.cmv_condition_8(),
            self.cmv_condition_9(),
            self.cmv_condition_10(),
            self.cmv_condition_11(),
            self.cmv_condition_12(),
            self.cmv_condition_13(),
            self.cmv_condition_14(),
        ]

    def cmv_condition_0(self):
        """
        Checks if there is a set of consecutive data points
            with a distance greater than a set length apart

        Args:
            point_array (type: list of 2-tuples): contains (x,y) values
            length1 (type: float): minimum distance necessary

        Returns:
            (type: boolean) True if condition met, false otherwise
        """
        if len(self.POINTS) < 2:
            return False
        for i in range(len(self.POINTS) - 1):
            if (
                distance_between_points(self.POINTS[i], self.POINTS[i + 1])
                > self.LENGTH1
            ):
                return True
        return False

    def cmv_condition_1(self):
        """
        Returns true if there exists at least one set of three consecutive data points that cannot all be contained
        within or on a circle of given radius.

        Args:
            point_array (type: list of 2-tuples): contains (x,y) values
            radius (type: float): radius of the circle

        Returns:
            (type: boolean) True if condition met, false otherwise"""
        if len(self.POINTS) < 3:
            return False
        for i in range(len(self.POINTS) - 2):
            p1, p2, p3 = self.POINTS[i], self.POINTS[i + 1], self.POINTS[i + 2]
            center = calculate_center([p1, p2, p3])
            if (
                distance_exceeds_radius(p1, center, self.RADIUS1)
                or distance_exceeds_radius(p2, center, self.RADIUS1)
                or distance_exceeds_radius(p3, center, self.RADIUS1)
            ):
                return True
        return False

    def cmv_condition_2(self):
        """
        There exists at least one set of three consecutive data
            points that form an angle greater than pi + epsilon or less tha npi - epsilon

        Args:
            points (list): coordinates
            epsilon (float): angle

        Returns:
            True if condition is satisfied, false otherwise
        """

        # returns the angle formed by the line segments p1 -> p2 -> p3
        def get_angle(p1, p2, p3):  # p1, p2, p3 are points
            v12 = distance_between_points(p1, p2)
            v23 = distance_between_points(p2, p3)
            v31 = distance_between_points(p3, p1)
            return math.acos((v12**2 + v23**2 - v31**2) / (2 * v12 * v23))

        for i in range(len(self.POINTS) - 2):
            p1 = self.POINTS[i]
            p2 = self.POINTS[i + 1]
            p3 = self.POINTS[i + 2]

            if p1 == p2 or p2 == p3:
                continue

            angle = get_angle(p1, p2, p3)
            if angle < math.pi - self.EPSILON or angle > math.pi + self.EPSILON:
                return True
        return False

    def cmv_condition_3(self):
        """
        There exists at least one set of three consecutive data
            points that are the vertices of a triangle
            with area greater than AREA1. (0 ≤ AREA1)

        Args:
            points (list): coordinates
            area1 (float): area of a triangle

        Returns:
            True if a traingle with greater area than AREA1 exists
        """
        if len(self.POINTS) < 3:
            return False
        for i in range(len(self.POINTS) - 2):
            area = calculate_area_triangle(
                self.POINTS[i], self.POINTS[i + 1], self.POINTS[i + 2]
            )
            if area >= self.AREA1:
                return True
        return False

    def cmv_condition_4(self):
        """Checks if There exists at least one set of Q PTS consecutive data points that lie in more than QUADS
        quadrants.
        """

        def number_of_quad(points):
            in_quads = [0, 0, 0, 0]
            for pt in points:
                if pt[0] >= 0 and pt[1] >= 0:
                    in_quads[0] = 1
                elif pt[0] < 0 and pt[1] >= 0:
                    in_quads[1] = 1
                elif pt[0] <= 0 and pt[1] < 0:
                    in_quads[2] = 1
                elif pt[0] > 0 and pt[1] < 0:
                    in_quads[3] = 1

            return sum(in_quads)

        if len(self.POINTS) < self.Q_PTS:
            return False
        for i in range(len(self.POINTS) - self.Q_PTS + 1):
            if number_of_quad(self.POINTS[i : i + self.Q_PTS]) >= self.QUADS:
                return True
        return False

    def cmv_condition_5(self):
        """
        Checks if there are two consecutive x-coords such that
            the first subtracted from the second is less than 0

        Args:
            point_array (type: list of 2-tuples): contains (x,y) values

        Returns:
            (type: boolean) True if condition met, false otherwise
        """
        if len(self.POINTS) < 2:
            return False
        for i in range(len(self.POINTS) - 1):
            if self.POINTS[i + 1][0] - self.POINTS[i][0] < 0:
                return True
        return False

    def cmv_condition_6(self):
        """
        Checks if there exists at least one set of N PTS consecutive data points such that at least one of the
        points lies a distance greater than DIST from the line joining the first and last of these N PTS
        points.

        Args:
            point_array (type: list of 2-tuples): contains (x,y) values
            N_PTS (type: int): Number of consecutive data points
            dist: cut-off distance between the first and last of N_PTS

        Returns:
            (type: boolean) True if condition met, false otherwise
        """
        if len(self.POINTS) < 3 or len(self.POINTS) < self.N_PTS:
            return False
        for beginIdx in range(len(self.POINTS) - self.N_PTS + 1):
            endIdx = beginIdx + self.N_PTS - 1
            beginPoint, endPoint = self.POINTS[beginIdx], self.POINTS[endIdx]
            # Same begin and end point, return True if distance of middle points from beginPoint > dist
            if beginPoint == endPoint:
                for midIdx in range(beginIdx + 1, endIdx):
                    midPoint = self.POINTS[midIdx]
                    if distance_between_points(midPoint, beginPoint) > self.DIST:
                        return True
            # different begin and end point, calculate distance from midpoint to line formed
            else:
                beginPoint, endPoint = np.asarray(beginPoint), np.asarray(endPoint)
                for midIdx in range(beginIdx + 1, endIdx):
                    midPoint = np.asarray(self.POINTS[midIdx])
                    distance_from_line = np.abs(
                        np.cross(beginPoint - endPoint, endPoint - midPoint)
                    ) / np.linalg.norm(beginPoint - endPoint)
                    if distance_from_line > self.DIST:
                        return True
        return False

    def cmv_condition_7(self):
        """
        Checks if there are two points p1, p2, in the array seperated by K_PTS conscutive
        intervening points, and the distance between p1 and p2 is greater than length1

        Args:
            points (type: list of 2-tuples): contains (x,y) values
            K_PTS (type: int): number of intervening points
            length1 (type: float): minimum distance necessary

        Returns:
            (type: boolean) True if condition met, False, otherwise
        """

        if len(self.POINTS) < 3:
            return False

        for i in range(len(self.POINTS) - self.K_PTS - 1):
            p1 = self.POINTS[i]
            p2 = self.POINTS[i + self.K_PTS + 1]
            if distance_between_points(p1, p2) > self.LENGTH1:
                return True
        return False

    def cmv_condition_8(self):
        """
        There exists at least one set of three data points separated by exactly
        A PTS and B PTS consecutive intervening points, respectively, that cannot
        be contained within or on a circle of radius RADIUS1.

        The condition is not met when NUMPOINTS < 5.
        1≤A PTS,1≤B PTS
        A PTS+B PTS ≤ (NUMPOINTS−3)

        Args:
            points (list): coordinates
            a_pts (int): number of interevening points
            b_pts (int): number of inttervening points
            radius1 (float): circle radius

        Returns:
            True if conditions are met
        """
        if len(self.POINTS) < 5:
            return False

        for i in range(len(self.POINTS) - self.A_PTS - self.B_PTS - 2):
            p1 = self.POINTS[i]
            p2 = self.POINTS[i + self.A_PTS + 1]
            p3 = self.POINTS[i + self.A_PTS + self.B_PTS + 2]
            center = calculate_center([p1, p2, p3])
            if (
                distance_exceeds_radius(p1, center, self.RADIUS1)
                or distance_exceeds_radius(p2, center, self.RADIUS1)
                or distance_exceeds_radius(p3, center, self.RADIUS1)
            ):
                return True
        # Both conditions failed
        return False

    def cmv_condition_9(self):
        """Check if there exists at least one set of three data points separated by exactly C PTS and D PTS
        consecutive intervening points, respectively, that form an angle such that:
        angle < (PI−EPSILON)
            or
        angle > (PI+EPSILON)
        """

        if len(self.POINTS) < 5:
            return False

        for i in range(len(self.POINTS) - self.C_PTS - 1 - self.D_PTS - 1):
            if (
                self.POINTS[i] == self.POINTS[i + self.C_PTS + 1]
                or self.POINTS[i + self.C_PTS + 1]
                == self.POINTS[i + self.C_PTS + 1 + self.D_PTS + 1]
            ):
                continue
            angle = calculate_angle_between_points(
                self.POINTS[i],
                self.POINTS[i + self.C_PTS + 1],
                self.POINTS[i + self.C_PTS + 1 + self.D_PTS + 1],
            )
            if angle < math.pi - self.EPSILON or angle > math.pi + self.EPSILON:
                return True
        return False

    def cmv_condition_10(self):
        """Checks if there is a set of three data points, separated by
            e_pts and f_pts respectively, that form a triangle with an
            area greater than area1

        Args:
            point_array (list of 2-tuples): contains (x,y) values
            e_pts (int): amount of steps separating first and second vertex
            f_pts (int): amount of steps separating second and third vertex
            area1 (double): area which triangle must be larger than
            num_points (int): amount of points in the point_array

        Returns:
            (boolean): True if condition met, false otherwise
        """
        if len(self.POINTS) < 5:
            return False

        for i in range(len(self.POINTS)):
            if i + self.E_PTS + 1 + self.F_PTS + 1 >= len(
                self.POINTS
            ):  # looped as far as possible
                break
            # use triangle coord formula
            area = calculate_area_triangle(
                self.POINTS[i],
                self.POINTS[i + self.E_PTS + 1],
                self.POINTS[i + self.E_PTS + 1 + self.F_PTS + 1],
            )
            if area > self.AREA1:
                return True
        return False

    def cmv_condition_11(self):
        """
        Checks if there exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
        exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j )

        Args:
            points (type: list of 2-tuples): contains (x,y) values
            G_PTS (type: int): number of intervening points

        Returns:
            (type: boolean) True if condition met, False, otherwise
        """
        if self.G_PTS > len(self.POINTS) - 2 or len(self.POINTS) < 3:
            return False
        for beginIdx in range(len(self.POINTS) - self.G_PTS - 1):
            endIdx = beginIdx + self.G_PTS + 1
            x_begin, x_end = self.POINTS[beginIdx][0], self.POINTS[endIdx][0]
            if x_end - x_begin < 0:
                return True
        return False

    def cmv_condition_12(self):
        """
        Checks if there are two points separated by K_PTS intervening points that are > length1 apart
        as well as two points separated by K_PTS intervening points that are < length2 apart

        Args:
            points (type: list of 2-tuples): contains (x,y) values
            K_PTS (type: int): number of intervening points
            length1 (type: float): minimum distance necessary
            length2 (type: float): maximum distance between points
        """

        for i in range(len(self.POINTS) - self.K_PTS - 1):
            p1 = self.POINTS[i]
            p2 = self.POINTS[i + self.K_PTS + 1]
            if distance_between_points(p1, p2) < self.LENGTH2:
                return True and self.cmv_condition_7()
        return False

    def cmv_condition_13(self):
        """
        There exists at least one set of three data points, separated by exactly A PTS and B PTS
        consecutive intervening points, respectively, that cannot be contained within or on a
        circle of radius RADIUS1. In addition, there exists at least one set of three data points
        (which can be the same or different from the three data points just mentioned)
        separated by exactly A PTS and B PTS consecutive intervening points, respectively,
        that can be contained in or on a circle of radius RADIUS2.
        Both parts must be true for the LIC to be true.
        The condition is not met when NUMPOINTS < 5.


        Args:
            points (list): list of (x,y) coordinates
            a_pts (int): number of intervening points
            b_pts (int): number of intervening points
            radius1 (float): circle radius
            radius2 (float): circle radius, must be 0 ≤ RADIUS2

        Returns:
            True if conditions are met
        """
        if len(self.POINTS) < 5:
            return False

        for i in range(len(self.POINTS) - self.A_PTS - self.B_PTS - 2):
            p1 = self.POINTS[i]
            p2 = self.POINTS[i + self.A_PTS + 1]
            p3 = self.POINTS[i + self.A_PTS + self.B_PTS + 2]

            # Same as calculations as cmv_1
            center = calculate_center([p1, p2, p3])

            if (
                not distance_exceeds_radius(p1, center, self.RADIUS2)
                and not distance_exceeds_radius(p2, center, self.RADIUS2)
                and not distance_exceeds_radius(p3, center, self.RADIUS2)
            ):
                return self.cmv_condition_8()

        return False

    def cmv_condition_14(self):
        """Check if:
        (1) there exists at least one set of three data points, separated by exactly
            E PTS and F PTS consecutive intervening points, respectively, that are
            the vertices of a triangle with area greater than AREA1.
        (2) there exist three data points separated by exactly E PTS and F PTS consecutive
            intervening points, respectively, that are the vertices of a triangle with area
            less than AREA2.
        """

        if len(self.POINTS) < 5:
            return False

        conditions = [False, False]

        for i in range(len(self.POINTS) - self.E_PTS - 1 - self.F_PTS - 1):
            area = calculate_area_triangle(
                self.POINTS[i],
                self.POINTS[i + self.E_PTS + 1],
                self.POINTS[i + self.E_PTS + 1 + self.F_PTS + 1],
            )
            if area >= self.AREA1:
                conditions[0] = True
            if area <= self.AREA2:
                conditions[1] = True
            if conditions[0] and conditions[1]:
                return True
        return False


if __name__ == "__main__":
    pass
