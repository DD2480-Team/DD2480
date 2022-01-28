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
