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
        raise ArgumentError


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
    else:
        print("The rocket has not been launched")


if __name__ == "__main__":
    should_launch = sys.argv[1]
    launch(parse_args(should_launch))
