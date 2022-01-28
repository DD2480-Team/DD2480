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
