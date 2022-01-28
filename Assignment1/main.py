import math

def main():
    return

# returns true if there are three consecutive points that form an angle greater than
# pi + epsilon or less than pi - epsilon
def cmv_condition_2(points, epsilon):

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

if __name__ == "__main__":
    main()
