import math
import numpy as np

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


def cmv_condition_2(points, epsilon):
    """ 
    There exists at least one set of three consecutive data 
        points that form an angle greater than pi + epsilon or less tha npi - epsilon

    Args:
        points (list): coordinates
        epsilon (float): angle

    Returns:
        True if condition is satisfied, false otherwise
    """

    #returns the Euclidean distance between two points 
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    #returns the angle formed by the line segments p1 -> p2 -> p3
    def get_angle(p1, p2, p3): #p1, p2, p3 are points 
        v12 = dist(p1,p2)
        v23 = dist(p2,p3)
        v31 = dist(p3,p1)
        return math.acos((v12 ** 2 + v23 ** 2 - v31 ** 2) / (2 * v12 * v23))

    for i in range(len(points) - 2):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]

        if p1 == p2 or p2 == p3:
            continue

        angle = get_angle(p1, p2, p3)
        if angle < math.pi - epsilon or angle > math.pi + epsilon:
            return True
    return False

def cmv_condition_3(points, area1):
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

def check_condition_5(point_array):
    """ 
    Checks if there are two consecutive x-coords such that
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


def cmv_condition_6(points, N_PTS, dist):
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
    def distance_between_points(p1, p2):
        return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    if len(points) < 3 or len(points) < N_PTS:
        return False
    for beginIdx in range(len(points) - N_PTS + 1):
        endIdx = beginIdx + N_PTS - 1
        beginPoint, endPoint = points[beginIdx], points[endIdx]
        # Same begin and end point, return True if distance of middle points from beginPoint > dist
        if beginPoint == endPoint:
            for midIdx in range(beginIdx + 1, endIdx):
                midPoint = points[midIdx]
                if distance_between_points(midPoint, beginPoint) > dist:
                    return True
       # different begin and end point, calculate distance from midpoint to line formed
        else:
            beginPoint, endPoint = np.asarray(beginPoint), np.asarray(endPoint)
            for midIdx in range(beginIdx + 1, endIdx):
                midPoint = np.asarray(points[midIdx])
                distance_from_line = np.abs(np.cross(beginPoint - endPoint, endPoint - midPoint)) / np.linalg.norm(beginPoint - endPoint)
                if distance_from_line > dist:
                    return True
    return False

def cmv_condition_7(points, K_PTS, length1):
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
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    if len(points) < 3: 
        return False
        
    for i in range(len(points) - K_PTS - 1):
        p1 = points[i]
        p2 = points[i + K_PTS + 1]
        if dist(p1, p2) > length1:
            return True
    return False


def cmv_condition_11(points, G_PTS):
    """
    Checks if there exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
    exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j )
    
    Args: 
        points (type: list of 2-tuples): contains (x,y) values
        G_PTS (type: int): number of intervening points

    Returns: 
        (type: boolean) True if condition met, False, otherwise
    """
    if G_PTS > len(points) - 2 or len(points) < 3:
        return False
    for beginIdx in range(len(points) - G_PTS - 1):
        endIdx = beginIdx + G_PTS + 1
        x_begin, x_end = points[beginIdx][0], points[endIdx][0]
        if x_end - x_begin < 0:
            return True
    return False
    
if __name__ == "__main__":
    pass

