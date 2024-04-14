import numpy as np


def f(x):
    return (x - 3) ** 2 - 3 * x + x ** 2 - 40


def gsearch(interval, tol):
    # GOLDENSECTIONSEARCH searches for minimum using golden section
    # 	[xmin, fmin, neval] = GOLDENSECTIONSEARCH(f,interval,tol)
    #   INPUT ARGUMENTS
    # 	f is a function
    # 	interval = [a, b] - search interval
    # 	tol - set for bot range and function value
    #   OUTPUT ARGUMENTS
    # 	xmin is a function minimizer
    # 	fmin = f(xmin)
    # 	neval - number of function evaluations
    #   coords - array of statistics,  coord[i][] =  [x1,x2, a, b]

    a, b = interval
    neval = 0
    coord = []

    phi = (1 + np.sqrt(5)) / 2  # Золотое сечение
    invphi = 1 / phi

    # Вычисляем начальные точки x1 и x2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = f(x1)
    f2 = f(x2)
    neval += 2  # Две оценки функции

    coord.append([x1, x2, a, b])

    while np.abs(b - a) > tol:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / phi
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / phi
            f2 = f(x2)
        neval += 1
        coord.append([x1, x2, a, b])

    xmin = (a + b) / 2
    fmin = f(xmin)

    answer_ = [xmin, fmin, neval, coord]
    return answer_
