from argparse import ArgumentError
import sys
from pathlib import Path
import ast


def read_CMV_PUV_LCM_from_file(f = "input.txt"):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / f
    try:
        input_file = open(file_location, "r")
        input = input_file.read()
        input_array = input.split('\n')
    except:
        raise ArgumentError("name your file input.txt in the same directory and is line separated")

    try:
        input_array = list(map(lambda entry: entry.split('=')[1], input_array))
    except:
        raise ArgumentError("ensure that each line is formatted as PARAM=VALUE")

    assert len(input_array) == 23, "incorrect number of inputs"

    num_points = int(input_array[0])
    points = ast.literal_eval(input_array[1])

    assert len(points) == num_points, "incorrect number of points. ensure num_points is set correctly"

    LENGTH1 = float(input_array[2])
    RADIUS1 = float(input_array[3])
    EPSILON = float(input_array[4])
    AREA1 = float(input_array[5])
    Q_PTS = int(input_array[6])
    QUADS = int(input_array[7])
    DIST = float(input_array[8])
    N_PTS = int(input_array[9])
    K_PTS = int(input_array[10])
    A_PTS = int(input_array[11])
    B_PTS = int(input_array[12])
    C_PTS = int(input_array[13])
    D_PTS = int(input_array[14])
    E_PTS = int(input_array[15])
    F_PTS = int(input_array[16])
    G_PTS = int(input_array[17])
    LENGTH2 = float(input_array[18])
    RADIUS2 = float(input_array[19])
    AREA2 = float(input_array[20])
    LCM = ast.literal_eval(input_array[21])
    PUV = ast.literal_eval(input_array[22])

if __name__ == "__main__":
    read_CMV_PUV_LCM_from_file()
