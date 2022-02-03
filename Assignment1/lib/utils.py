import math


def distance_between_points(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def distance_exceeds_radius(p1, center, radius):
    distance_from_center = distance_between_points(p1, center)
    if distance_from_center > radius:
        return True
    return False


def calculate_center(points):
    x_sum, y_sum = 0, 0
    for p in points:
        x_sum += p[0]
        y_sum += p[1]
    return [x_sum / len(points), y_sum / len(points)]


def calculate_area_triangle(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))


def calculate_angle_between_points(p1, p2, p3):
    v12 = distance_between_points(p1, p2)
    v23 = distance_between_points(p2, p3)
    v31 = distance_between_points(p3, p1)
    return math.acos((v12**2 + v23**2 - v31**2) / (2 * v12 * v23))
