import argparse
from fuv import form_the_fuv
from generate_datapoints import generate_LCM_matrix
from parser import *
from pum import form_the_pum
import sys


def parse_args(arg):
    ua = str(arg).upper()
    if "TRUE".startswith(ua):
        return True
    elif "FALSE".startswith(ua):
        return False
    else:
        raise argparse.ArgumentError(None, "ensure one boolean argument is provided")

def DECIDE(puv, lcm):
    cmv = read_CMV_PUV_LCM_from_file()
    pum = form_the_pum(cmv.CMV_VECTOR, lcm)
    fuv = form_the_fuv(pum, puv)

    if all(fuv):
        print("YES")
        return True
    else:
        print("NO")
        return False

def launch(should_launch):
    puv = [False for _ in range(15)] if should_launch else [True for _ in range(15)]
    cmv = read_CMV_PUV_LCM_from_file()
    print(f"The cmv vector is {cmv.CMV_VECTOR}")
    vals = ["NOTUSED"] if should_launch else ["ORR"]
    lcm = generate_LCM_matrix(vals)
    print(f"The lcm matrix is {lcm}")
    pum = form_the_pum(cmv.CMV_VECTOR, lcm)
    print(f"The pum matrix is {pum}")
    fuv = form_the_fuv(pum, puv)
    print(f"The FUV vector is {fuv}")
    if all([fuv[i] for i in range(len(fuv))]):
        print("The rocket has been launched!")
        return True
    else:
        print("The rocket has not been launched")
        return False


def form_the_pum(cmv, lcm):
    """
    CMV and LCM are combined to form PUM.
    CMV: The CMV is a boolean vector whose elements have a one-to-one
    correspondence with the launch interceptor conditions
    LCM: The entries in the LCM represent the logical connectors to be used
    between pairs of LICs to determine the corresponding entry in the PUM
    Args:
        cmv (list): list of boolean value
        lcm(2D-list): 15*15 matrix of "ANDD", "ORR", "NOTUSED"
    Returns:
        pum(2D-list): 15*15 matrix of boolean value
    """
    pum = [[False for x in range(15)] for i in range(15)]

    for i in range(15):
        for j in range(i, 15):
            if lcm[i][j] == "ANDD":
                if cmv[i] and cmv[j]:
                    pum[i][j] = True
                    pum[j][i] = True
            elif lcm[i][j] == "ORR":
                if cmv[i] or cmv[j]:
                    pum[i][j] = True
                    pum[j][i] = True
            elif lcm[i][j] == "NOTUSED":
                pum[i][j] = True
                pum[j][i] = True
    return pum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentError(None, "ensure one boolean argument is provided")
    should_launch = sys.argv[1]
    launch(parse_args(should_launch))
