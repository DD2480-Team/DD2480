import math


def cmv_condition_8(points, a_pts, b_pts, radius1, numpoints):
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
    if numpoints < 5:
        return False

    if (a_pts < 1 or b_pts < 1):
        return False
    if ((a_pts + b_pts) > len(points)-3):
        return False

    """
    explanation of indices:
    take array of length 6: [1,0,1,0,0,1], A_PTS = 1, B_PTS = 2
    need to check the points at index i, i+A_PTS+1, and i+A_PTS+1+B_PTS+1
    the last value for i you can check in this example is 0 which is numpoints - A_PTS - B_PTS - 3
    """
    for i in range(numpoints - a_pts - b_pts - 3):
        p1 = points[i]
        p2 = points[i+a_pts+1]
        p3 = points[i+a_pts+b_pts+2]

        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        x3, y3 = p3[0], p3[1]

        # Same as calculations as cmv_1
        center = [(x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3]

        def distance_exceeds_radius(x, y):
            squared_distance = (x - center[0]) ** 2 + \
                (y - center[1]) ** 2

            if squared_distance > radius1 ** 2:
                # True if the point cannot be contained
                return True
            return False
        if distance_exceeds_radius(x1, y1) or distance_exceeds_radius(x2, y2) or distance_exceeds_radius(x3, y3):
            return True
    # Both conditions failed
    return False
