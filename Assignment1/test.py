from main import check_condition_0

def main():
    if __name__ == "__main__":
        main()

#must exist one set of two consecutive data points that are further than length1
#pass two points with dist 5 and and length1 4.5, should return True
def test1_check_condition_0():
    points = [(0,0),(4,3)]  #dist is 5
    length1 = 4.5
    assert(check_condition_0(points, length1) == True)
    print("Success: test1_check_condition_0")

#must exist one set of two consecutive data points that are further than length1
#pass two points with dist 5 and and length1 5.5, should return False
def test2_check_condition_0():
    points = [(0,0),(4,3)]  #dist is 5
    length1 = 5.5
    assert(check_condition_0(points, length1) == False)
    print("Success: test2_check_condition_0")

#must exist one set of two consecutive data points that are further than length1
#pass only one point, should return False
def test3_check_condition_0():
    points = [(0,0)]  #dist undefined
    length1 = 0
    assert(check_condition_0(points, length1) == False)
    print("Success: test3_check_condition_0")

#must exist one set of two consecutive data points that are further than length1
#pass negative distance, should return False
def test4_check_condition_0():
    points = [(0,0),(4,3)]  #dist is 5
    length1 = -1
    assert(check_condition_0(points, length1) == False)
    print("Success: test4_check_condition_0")

test1_check_condition_0()
test2_check_condition_0()
test3_check_condition_0()
test4_check_condition_0()