def form_the_fuv(pum, puv):
    """The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. 
     FUV[i] should be set to true if PUV[i] is false 
    (indicating that the associated LIC should not hold back launch) 
    or if all elements in PUM row i are true.

    Args:
        pum (Array of bools): Preliminary Unlocking Matrix
        puv (Array of bools): The input PUV indicates whether the corresponding LIC 
        is to be considered as a factor in signaling interceptor launch.

    Returns:
        (Array of bools): Final Unlocking Vector
    """
    fuv = [False for _ in range(15)]
    for i in range(len(puv)):
        if not puv[i]:
            fuv[i] = True
        else:
            for j in range(len(puv)):
                if(i==j):
                    pum[i][j] = True
            fuv[i] = all(pum[i])
    return fuv
