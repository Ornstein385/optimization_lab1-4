import numpy as np

def f(x): return x ** 2 - 10 * np.cos(0.3 * np.pi * x) - 20
def df(x): return 2 * x + 3 * np.pi * np.sin(0.3 * np.pi * x)
def ddf(x): return 2 + 0.9 * (np.pi ** 2) * np.cos(0.3 * np.pi * x)


def nsearch(tol, x0):
    # NSEARCH searches for minimum using Newton method
    # 	answer_ = nsearch(tol,x0)
    #   INPUT ARGUMENTS
    # 	tol - set for bot range and function value
    #	x0 - starting point
    #   OUTPUT ARGUMENTS
    #   answer_ = [xmin, fmin, neval, coords]
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of x values found during optimization

    coords = [x0]
    neval = 0
    x = x0
    dfx = df(x)

    while np.abs(dfx) >= tol:
        x = x - dfx / ddf(x)
        coords.append(x)
        dfx = df(x)
        neval += 3

    xmin = x
    fmin = f(xmin)

    answer_ = [xmin, fmin, neval, coords]
    return answer_
