import math

def main():
    if __name__ == "__main__":
        main()


def check_condition_0(point_array, length1):
    """ Checks if there is a set of consecutive data points
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


#TODO: skriv test till denna!
def check_condition_10(point_array, e_pts, f_pts, area1, num_points):
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
    input_con1 = num_points > 5   #NUMPOINTS < 5 should return False
    input_con2 = e_pts >= 1 and f_pts >= 1
    input_con3 = e_pts + f_pts <= num_points - 3
    if(not(input_con1 and input_con2 and input_con3)):
        return False

    for i in range(len(point_array)):
        vertex1 = point_array[i]
        vertex2 = point_array[i + e_pts + 1]
        vertex3 = point_array[i + e_pts + 1 + f_pts + 1]
        #use triangle coord formula
        area = (vertex1[0] * (vertex2[1] - vertex3[1])
            +   vertex2[0] * (vertex3[1] - vertex1[1])
            +   vertex3[0] * (vertex1[1] - vertex2[1]) ) /2
        if (area > area1):
            return True
    return False