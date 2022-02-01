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

   
def form_the_fuv(puv, pum):
    """
    he Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. 
    The input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling interceptor launch. 
    FUV[i] should be set to true if PUV[i] is false (indicating that the associated LIC should not hold back launch) 
    or if all elements in PUM row i are true (not including the current index as per Ex 3).

    Ex 1. FUV[0] is False because PUV[0] is True, but PUM[0,1] and PUM[0,3] are False.
    Ex 2. FUV[1] is True because PUV[1] is False.  
    Ex 3. FUV[2] is True because PUV[2] is True and PUM[2,i] is True for all i != 2, 0 ≤ i ≤ 14.

    Args:
        pum (2D-list): 15*15 matrix of boolean values
        puv (list): length 15 matrix of boolean values indicating which LIC should hold back launch

    Returns:
        fuv (list): length 15 matrix of boolean values
    """
    #the value of the fuv is True when corresponding value of the puv is False
    fuv = [not x for x in puv]
    for i in range(15):
        fuv[i] = True if len([x for x in pum[i] if x]) >= 14 else fuv[i]
    print(fuv)

    return fuv

if __name__ == "__main__":
    cmv = read_CMV_PUV_LCM_from_file()
    print(cmv.CMV_VECTOR)
