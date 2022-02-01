def form_the_fuv(pum, puv):
    fuv = [False for _ in range(15)]
    for i in range(len(puv)):
        if not puv[i]:
            fuv[i] = True
        else:
            fuv[i] = all(pum[i])
    return fuv
