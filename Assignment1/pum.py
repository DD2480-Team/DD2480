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
    pum = [[False for _ in range(15)] for _ in range(15)]

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
