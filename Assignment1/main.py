def cmv_condition_1(points, radius):
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


if __name__ == "__main__":
    pass