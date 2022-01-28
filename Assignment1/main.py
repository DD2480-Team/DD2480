import math


def cmv_condition_8(points, a_pts, b_pts, radius1, radius2):
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
        points (list): coordinates
        a_pts (int): distance A PTS
        b_pts (int): distance B PTS
        radius1 (float): circle radius
        radius2 (float): circle radius, must be 0 ≤ RADIUS2

    Returns:
        True if conditions are met
    """
    if len(points) < 5:
        return False
    if radius2 <= 0:
        return False
    radius1_contained = False
    radius2_contained = False
    total_points = len(points)
    for i in range(total_points-2):
        (x1, y1), (x2, y2), (x3, y3) = points[i], points[i+1], points[i+2]

        # The distances A PTS and B PTS are integers
        dist1 = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        dist2 = int(math.sqrt((x3 - x2)**2 + (y3 - y2)**2))

        if not (dist1 == a_pts and dist2 == b_pts):
            continue

        # Same as calculations as cmv_1
        center = [(x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3]

        def distance_exceeds_radius(x, y, radius):
            squared_distance = (x - center[0]) ** 2 + \
                (y - center[1]) ** 2

            if squared_distance > radius ** 2:
                # True if the point cannot be contained
                return True
            return False

        # If one
        if (distance_exceeds_radius(x1, y1, radius1) or distance_exceeds_radius(x2, y2, radius1) or distance_exceeds_radius(x3, y3, radius1)):
            radius1_contained = True
        if (distance_exceeds_radius(x1, y1, radius2) or distance_exceeds_radius(x2, y2, radius2) or distance_exceeds_radius(x3, y3, radius2)):
            radius2_contained = True

        if radius1_contained == True and radius2_contained == True:
            return True
    return False


points = [(1, 0), (3, 0), (5, 0), (-1, -2), (2, 1),
          (2, 2), (3, 3), (-2, -2), (1, 1), (-1, -1)]
r = cmv_condition_8(points, 2, 2, 1.5, 1)
print(r)
