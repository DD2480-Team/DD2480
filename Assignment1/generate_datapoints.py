# int numpoints
# list points
# double length1
# double radius1
# double epsilon
# double area1
# int Q_PTS
# int quads
# double dist
# int N_PTS
# int K_PTS
# int A_PTS
# int B_PTS
# int C_PTS
# int D_PTS
# int E_PTS
# int F_PTS
# int G_PTS
# double length2
# double radius2
# double area2
# list LCM
# list PUV


import random
import pickle


def generate_datatpoints(x):
    """Generating vectors with (x,y)
    Args:
        x(int): , number of points
    """
    datapoints = [(round(random.uniform(-10, 10), 3), round(random.uniform(-10, 10), 3))
                  for i in range(x)]
    data_file = open('./datapoints.dat', 'wb')
    pickle.dump(datapoints, data_file)
    data_file.close()


def generate_LCM_matrix():
    """Generating 15x15 matrix with values "ANDD", "ORR", "NOTUSED"
    """
    vals = ["ANDD", "ORR", "NOTUSED"]
    lcm = [["" for _ in range(15)] for _ in range(15)]
    for i in range(15):
        for j in range(15):
            choice = random.choice(vals)
            lcm[i][j] = choice
            lcm[j][i] = choice
    data_file = open('./datapoints.dat', 'ab')
    pickle.dump(lcm, data_file)
    data_file.close()
    # print(lcm)


def generate_puv():
    """Generating T/F vector
    """
    puv = [random.randint(0, 1) for _ in range(15)]
    data_file = open('./datapoints.dat', 'wb')
    pickle.dump(puv, data_file)
    data_file.close()


""" Unquote to generate the needed files """
# x = number of points
# generate_datatpoints(x=10)
# generate_LCM_matrix()
# generate_puv()
data_file = open("./datapoints.dat", "rb")
list_points = pickle.load(data_file)
print(list_points)
