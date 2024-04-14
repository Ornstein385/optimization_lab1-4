import numpy as np
def f(x): return 2 * (x ** 2) - 9 * x - 31
def df(x): return 4 * x - 9

def bsearch(interval,tol):
# searches for minimum using bisection method
# arguments: bisectionsearch(f,df,interval,tol)
# f - an objective function
# df -  an objective function derivative
# interval = [a, b] - search interval
#tol - tolerance for both range and function value
# output: [xmin, fmin, neval, coords]
# xmin - value of x in fmin
# fmin - minimul value of f
# neval - number of function evaluations
# coords - array of x values found during optimization
    
    
    a, b = interval
    neval = 0
    coords = []
    
    while True:
        x = (a + b) / 2
        g = df(a)
        coords.append(x)
        neval += 1
        
        if np.abs(b - a) <= tol and np.abs(g) <= tol:
            break
        
        if g * df(x) > 0:
            a = x
        else:
            b = x
    
    xmin = x
    fmin = f(xmin)
    
    answer_ = [xmin, fmin, neval, coords]
    return answer_