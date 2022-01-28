import math

def main():
    return

#returns True if there are two points p1, p2, in the array seperated by K_PTS conscutive
#intervening points, and the distance between p1 and p2 is greater than length1
def cmv_condition_7(points, K_PTS, length1):

    #TODO refactor, and make utility functions global
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    if len(points) < 3: 
        return False

    #check distances of values that are separted K_PTS points in the points list
    for i in range(len(points) - K_PTS - 1):
        p1 = points[i]
        p2 = points[i + K_PTS + 1]
        if dist(p1, p2) > length1:
            return True
    return False

if __name__ == "__main__":
   main()
