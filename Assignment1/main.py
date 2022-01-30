from argparse import ArgumentError
from cmath import pi
import math
import numpy as np
from pathlib import Path
import ast

def read_CMV_PUV_LCM_from_file(f = "input.txt"):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / f
    try:
        input_file = open(file_location, "r")
        input = input_file.read()
        input_array = input.split('\n')
    except:
        raise ArgumentError("name your file input.txt in the same directory and is line separated")

    try:
        input_array = list(map(lambda entry: entry.split('=')[1], input_array))
    except:
        raise ArgumentError("ensure that each line is formatted as PARAM=VALUE")

    assert len(input_array) == 23, "incorrect number of inputs"

    NUMPOINTS = int(input_array[0])
    POINTS = ast.literal_eval(input_array[1])

    assert len(POINTS) == NUMPOINTS, "incorrect number of points. ensure num_points is set correctly"

    LENGTH1 = float(input_array[2])
    assert LENGTH1 >= 0
    RADIUS1 = float(input_array[3])
    assert RADIUS1 >= 0
    EPSILON = float(input_array[4])
    assert pi > EPSILON >= 0 
    AREA1 = float(input_array[5])
    assert AREA1 >= 0
    Q_PTS = int(input_array[6])
    assert NUMPOINTS >= Q_PTS >= 2
    QUADS = int(input_array[7])
    assert 3 >= QUADS >= 1
    DIST = float(input_array[8])
    assert DIST >= 0
    N_PTS = int(input_array[9])
    assert NUMPOINTS >= N_PTS >= 3
    K_PTS = int(input_array[10])
    assert NUMPOINTS - 2 >= K_PTS >= 1
    A_PTS = int(input_array[11])
    assert A_PTS >= 1
    B_PTS = int(input_array[12])
    assert B_PTS >= 1
    assert A_PTS + B_PTS <= NUMPOINTS - 3
    C_PTS = int(input_array[13])
    assert C_PTS >= 1
    D_PTS = int(input_array[14])
    assert D_PTS >= 1
    assert C_PTS + D_PTS <= NUMPOINTS - 3
    E_PTS = int(input_array[15])
    assert E_PTS >= 1
    F_PTS = int(input_array[16])
    assert F_PTS >= 1
    assert E_PTS + F_PTS <= NUMPOINTS - 3
    G_PTS = int(input_array[17])
    assert 1 <= G_PTS <= NUMPOINTS - 2
    LENGTH2 = float(input_array[18])
    assert LENGTH2 >= 0
    RADIUS2 = float(input_array[19])
    assert RADIUS2 >= 0
    AREA2 = float(input_array[20])
    assert AREA2 >= 0   
    LCM = ast.literal_eval(input_array[21])
    assert len(LCM) == 15 and all([len(row) == 15 for row in LCM])
    PUV = ast.literal_eval(input_array[22])
    assert len(PUV) == 15
   

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
    read_CMV_PUV_LCM_from_file()
