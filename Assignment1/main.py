import numpy as np
"""
Returns True if there exists at least one set of N PTS consecutive data points such that at least one of the
points lies a distance greater than DIST from the line joining the first and last of these N PTS
points. If first and last points are the same and distance from intermediate point to first/last point
exceeds dist, return True
"""
def cmv_condition_6(points, N_PTS, dist):
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
                print(beginPoint, endPoint, midPoint, distance_from_line)
                if distance_from_line > dist:
                    return True
    return False
    
if __name__ == "__main__":
    pass

