from argparse import ArgumentError
from cmath import pi
from pathlib import Path
import ast


def read_CMV_PUV_LCM_from_file(f="input.txt"):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / f
    try:
        input_file = open(file_location, "r")
        input = input_file.read()
        input_array = input.split("\n")
    except:
        raise ArgumentError(
            "name your file input.txt in the same directory and is line separated"
        )

    try:
        input_array = list(map(lambda entry: entry.split("=")[1], input_array))
    except:
        raise ArgumentError("ensure that each line is formatted as PARAM=VALUE")

    assert len(input_array) == 23, "incorrect number of inputs"

    NUMPOINTS = int(input_array[0])
    POINTS = ast.literal_eval(input_array[1])

    assert (
        len(POINTS) == NUMPOINTS
    ), "incorrect number of points. ensure num_points is set correctly"

    LENGTH1 = float(input_array[2])
    assert LENGTH1 >= 0
    RADIUS1 = float(input_array[3])
    assert RADIUS1 >= 0
    EPSILON = float(input_array[4])
    assert pi > EPSILON >= 0
    AREA1 = float(input_array[5])
    assert AREA1 >= 0
    Q_PTS = int(input_array[6])
    assert NUMPOINTS >= Q_PTS >= 2
    QUADS = int(input_array[7])
    assert 3 >= QUADS >= 1
    DIST = float(input_array[8])
    assert DIST >= 0
    N_PTS = int(input_array[9])
    assert NUMPOINTS >= N_PTS >= 3
    K_PTS = int(input_array[10])
    assert NUMPOINTS - 2 >= K_PTS >= 1
    A_PTS = int(input_array[11])
    assert A_PTS >= 1
    B_PTS = int(input_array[12])
    assert B_PTS >= 1
    assert A_PTS + B_PTS <= NUMPOINTS - 3
    C_PTS = int(input_array[13])
    assert C_PTS >= 1
    D_PTS = int(input_array[14])
    assert D_PTS >= 1
    assert C_PTS + D_PTS <= NUMPOINTS - 3
    E_PTS = int(input_array[15])
    assert E_PTS >= 1
    F_PTS = int(input_array[16])
    assert F_PTS >= 1
    assert E_PTS + F_PTS <= NUMPOINTS - 3
    G_PTS = int(input_array[17])
    assert 1 <= G_PTS <= NUMPOINTS - 2
    LENGTH2 = float(input_array[18])
    assert LENGTH2 >= 0
    RADIUS2 = float(input_array[19])
    assert RADIUS2 >= 0
    AREA2 = float(input_array[20])
    assert AREA2 >= 0
    LCM = ast.literal_eval(input_array[21])
    assert len(LCM) == 15 and all([len(row) == 15 for row in LCM])
    PUV = ast.literal_eval(input_array[22])
    assert len(PUV) == 15


if __name__ == "__main__":
    read_CMV_PUV_LCM_from_file()
