import numpy as np

def f(x): return x**2 - 10*np.cos(0.3*np.pi*x) - 20
def df(x): return 2*x + 3*np.pi*np.sin(0.3*np.pi*x)
def ddf(x): return 2 + 0.9*(np.pi**2)*np.cos(0.3*np.pi*x)

def nsearch(tol, x0):
    coords = [x0]

    x = x0 - df(x0)/ddf(x0)
    neval = 3

    while np.abs(df(x)) >= tol:
        x = x - df(x)/ddf(x)
        coords.append(x)
        neval += 3

    xmin = x
    fmin = f(xmin)

    answer_ = [xmin, fmin, neval, coords]
    return answer_
