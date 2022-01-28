def cmv_condition_11(points, G_PTS):
    if G_PTS > len(points) - 2 or len(points) < 3:
        return False
    for beginIdx in range(len(points) - G_PTS - 1):
        endIdx = beginIdx + G_PTS + 1
        x_begin, x_end = points[beginIdx][0], points[endIdx][0]
        if x_end - x_begin < 0:
            return True
    return False


if __name__ == "__main__":
    pass

