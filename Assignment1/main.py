import sys
from pathlib import Path
import ast


def main():
    script_location = Path(__file__).absolute().parent
    file_location = script_location / "input.txt"
    input_file = open(file_location, "r")
    input = input_file.read()
    input_array = input.split('\n')

    assert len(input_array) == 23, "incorrect number of inputs"

    num_points = int(input_array[0])
    points = ast.literal_eval(input_array[1])

    assert len(points) == num_points, "incorrect number of points"

    length1 = float(input_array[2])
    radius1 = float(input_array[3])
    epsilon = float(input_array[4])
    area1 = float(input_array[5])
    Q_PTS = int(input_array[6])
    quads = int(input_array[7])
    dist = float(input_array[8])
    N_PTS = int(input_array[9])
    K_PTS = int(input_array[10])
    A_PTS = int(input_array[11])
    B_PTS = int(input_array[12])
    C_PTS = int(input_array[13])
    D_PTS = int(input_array[14])
    E_PTS = int(input_array[15])
    F_PTS = int(input_array[16])
    G_PTS = int(input_array[17])
    length2 = float(input_array[18])
    radius2 = float(input_array[19])
    area2 = float(input_array[20])
    LCM = ast.literal_eval(input_array[21])
    PUV = ast.literal_eval(input_array[22])


if __name__ == "__main__":
    main()
