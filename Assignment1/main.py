from parser import *


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

def launch(fuv):
    """
    the final launch/no launch decision is based on the FUV. 
    The decision to launch requires that all elements in the FUV be true, 
    i.e. LAUNCH should be set to true if and only if FUV[i] is true for all i, 0 ≤ i ≤ 14. 

    Args:
        fuv (list): a length 15 list of boolean values 

    Returns:
        boolean: returns True if False is not an element of the fuv
    """
    return False not in fuv

if __name__ == "__main__":
    cmv = read_CMV_PUV_LCM_from_file()
    print(cmv.CMV_VECTOR)
