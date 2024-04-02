import numpy as np
def f(x): return (x - 3)**2- 3*x + x**2 - 40

def gsearch(interval,tol):
    coord = []
    a = interval[0]
    b = interval[1]
    L = b - a

    x1 = b - L/((1+np.sqrt(5))/2)
    x2 = a + L/((1+np.sqrt(5))/2)

    f1 = f(x1)
    f2 = f(x2)

    coord.append([x1,x2, a, b])
    neval = 2
    while np.abs(L) > tol:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            L = b - a
            x1 = b - L/((1+np.sqrt(5))/2)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            L = b - a
            x2 = a + L/((1+np.sqrt(5))/2)
            f2 = f(x2)
        coord.append([x1,x2, a, b])
        neval += 1
    if f1 < f2:
        xmin = x1
        fmin = f1
    else:
        xmin = x2
        fmin = f2
    answer_ = [xmin, fmin, neval, coord]
    return answer_