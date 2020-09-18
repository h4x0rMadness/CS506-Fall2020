import math
def euclidean_dist(x, y):
    if len(x) == 0: raise ValueError("lengths must not be zero")
    if len(x) != len(y): raise ValueError("lengths must be equal")
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i]) * (x[i] - y[i])
    return sum

def manhattan_dist(x, y):
    if len(x) == 0: raise ValueError("lengths must not be zero")
    if len(x) != len(y): raise ValueError("lengths must be equal")
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i] - y[i])

    return sum

def jaccard_dist(x, y):
    if len(x) == 0: raise ValueError("lengths must not be zero")
    if len(x) != len(y): raise ValueError("lengths must be equal")
    '''
    M = [0, 0, 0, 0] ## M00 M01 M10 M11
    for i in range(len(x)):
        if x[i] == y[i] and x[i] == 0: M[0] += 1
        elif x[i] == 0 and y[i] == 1: M[1] += 1
        elif x[i] == 1 and y[i] == 0: M[2] += 1
        elif x[i] == y[i] and x[i] == 1: M[3] += 1

    Jsim = M[3] / float(M[0] + M[1] + M[2])
    return 1 - Jsim
    '''
    inter = 0
    union = len(x)
    for i in range(len(x)):
        if x[i] == y[i]: inter += 1

    return 1 - inter / union



def cosine_sim(x, y):
    if len(x) == 0: raise ValueError("lengths must not be zero")
    if len(x) != len(y): raise ValueError("lengths must be equal")
    dot_product = 0
    sq_sum_x = 0
    sq_sum_y = 0

    for i in range(len(x)):
        sq_sum_x += x[i] * x[i]
        sq_sum_y += y[i] * y[i]
        dot_product += x[i] * y[i]
    return dot_product / float(sq_sum_x * sq_sum_y)


# Feel free to add more
