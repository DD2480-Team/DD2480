from argparse import ArgumentError
import random
import pickle
from turtle import pu


def generate_datatpoints(x):
    """Generating vectors with (x,y)
    Args:
        x(int): , number of points
    """
    return [(round(random.uniform(-10, 10), 3), round(random.uniform(-10, 10), 3))
                  for _ in range(x)]


def generate_LCM_matrix(vals):
    """Generating 15x15 matrix with values "ANDD", "ORR", "NOTUSED"
    """
    vals = ["ANDD", "ORR", "NOTUSED"] if not vals else vals
    for v in vals:
        if v not in ("ANDD", "ORR", "NOTUSED"):
            raise ArgumentError("provide a value of ANDD, ORR, NOTUSED for the lcm matrix")
    lcm = [["" for _ in range(15)] for _ in range(15)]
    for i in range(15):
        for j in range(15):
            choice = random.choice(vals)
            lcm[i][j] = choice
            lcm[j][i] = choice
    return lcm


def generate_puv():
    """Generating T/F vector
    """
    return [random.randint(0, 1) for _ in range(15)]
    

def generate_parameters(num_datapoints = 10, lcm_values = [], file_name = ''):
    points = generate_datatpoints(num_datapoints)
    lcm = generate_LCM_matrix(lcm_values)
    puv = generate_puv()
    if not file_name:
        return points, lcm, puv
    with open(file_name, 'w') as f:
        f.write(f"POINTS={points}")
        f.write('\n')
        f.write(f"LCM={lcm}")
        f.write('\n')
        f.write(f"PUV={puv}")
        f.write('\n')
    f.close()
    return points, lcm, puv


if __name__ == "__main__":
    print(generate_parameters())