import numpy as np
def f(x): return 2 * (x ** 2) - 9 * x - 31
def df(x): return 4 * x - 9

def bsearch(interval,tol):
    coords = []
    a = interval[0]
    b = interval[1]
    g = df(a)
    L = (b - a) / 2

    while (np.abs(L) > tol) and (np.abs(g) > tol):
        t = a + L
        coords.append(t)
        if df(t) > 0:
            b = t
        if df(t) < 0:
            a = t
        g = df(a)
        L = (b - a) / 2

    xmin = t
    fmin = f(t)
    neval = len(coords) + 1
    
    answer_ = [xmin, fmin, neval, coords]
    return answer_