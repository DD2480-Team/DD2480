import math

def check_condition_0(point_array, length1):
    """ 
    Checks if there is a set of consecutive data points
        with a distance greater than a set length apart

    Args:
        point_array (type: list of 2-tuples): contains (x,y) values
        length1 (type: float): minimum distance necessary

    Returns:
        (type: boolean) True if condition met, false otherwise
    """
    if(length1 < 0 or len(point_array) < 2): 
        return False
    for i in range(len(point_array) -1):
        xdist = abs(point_array[i][0] - point_array[i+1][0])
        ydist = abs(point_array[i][1] - point_array[i+1][1])
        if(math.sqrt(xdist**2 + ydist**2 ) > length1):
            return True
    return False

def cmv_condition_1(points, radius):
    """
    Returns true if there exists at least one set of three consecutive data points that cannot all be contained
    within or on a circle of given radius.

    Args:
        point_array (type: list of 2-tuples): contains (x,y) values
        radius (type: float): radius of the circle

    Returns:
        (type: boolean) True if condition met, false otherwise    
"""
    if len(points) < 3:
        return False
    for i in range(len(points) - 2):
        p1, p2, p3 = points[i], points[i + 1], points[i + 2]
        center = [(p1[0] + p2[0] + p3[0])/ 3, (p1[1] + p2[1] + p3[1])/ 3]
        def distance_exceeds_radius(p):
            squared_distance = (p[0] - center[0]) ** 2 + (p[1] - center[1]) ** 2
            if squared_distance > radius ** 2:
                return True
            return False
        if distance_exceeds_radius(p1) or distance_exceeds_radius(p2) or distance_exceeds_radius(p3):
            return True
    return False

def cmv_condition_3(points, area1):
    """ There exists at least one set of three consecutive data 
        points that are the vertices of a triangle
        with area greater than AREA1. (0 ≤ AREA1)

    Args:
        points (list): coordinates
        area1 (float): area of a triangle

    Returns:
        True if a traingle with greater area than AREA1 exists
    """
    if len(points) < 3:
        return False
    if area1 <= 0:
        return False
    total_points = len(points)
    for i in range(total_points-2):
        (x1, y1), (x2, y2), (x3, y3) = points[i], points[i+1], points[i+2]
        area = 0.5*(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
        if area >= area1:
            return True
    return False

def check_condition_4(point_array, Q_PTS, quad):
    """ Checks if There exists at least one set of Q PTS consecutive data points that lie in more than QUADS 
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


    if (len(point_array) < Q_PTS) :
        return False
    for i in range(len(point_array) - Q_PTS + 1):
        if number_of_quad(point_array[i: i + Q_PTS]) >= quad:
            return True 

    return False

def check_condition_5(point_array):
    """ Checks if there are two consecutive x-coords such that
        the first subtracted from the second is less than 0

    Args:
        point_array (type: list of 2-tuples): contains (x,y) values

    Returns:
        (type: boolean) True if condition met, false otherwise
    """
    if(len(point_array) < 2):
        return False
    for i in range(len(point_array) -1):
        if(point_array[i+1][0] - point_array[i][0] < 0 ):
            return True
    return False

if __name__ == "__main__":
    pass