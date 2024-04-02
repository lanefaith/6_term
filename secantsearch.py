import numpy as np

def f(x): return x**2 -  10*np.cos(0.3*np.pi*x) - 20
def df(x): return 2*x + 3*np.pi*np.sin(0.3*np.pi*x)

def ssearch(interval,tol):
    coords = []
    a = interval[0]
    b = interval[1]

    x = b - (df(b)*(b-a))/(df(b)-df(a))
    neval = 1
    coords.append([x,a,b])

    while np.abs(df(x)) > tol and np.abs(b - a) > tol:
        if df(x) > 0:
            b = x
        if df(x) < 0:
            a = x
        x = b - (df(b)*(b-a))/(df(b)-df(a))
        coords.append([x,a,b])
        neval += 1
    xmin = x
    fmin = f(x)

    answer_ = [xmin, fmin, neval, coords]
    return answer_