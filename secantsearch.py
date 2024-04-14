import numpy as np


def f(x):
    return x ** 2 - 10 * np.cos(0.3 * np.pi * x) - 20


def df(x):
    return 2 * x + 3 * np.pi * np.sin(0.3 * np.pi * x)


def ssearch(interval, tol):
    a, b = interval
    neval = 0
    coords = []

    while True:
        # Вычисляем производную в точках a и b
        df_a = df(a)
        df_b = df(b)
        neval += 2

        x = b - df_b * (b - a) / (df_b - df_a)

        coords.append([x, a, b])

        df_x = df(x)

        # Проверка критерия остановки
        if np.abs(df_x) <= tol and np.abs(b - a) <= tol:
            break

        # Обновляем границы интервала
        if df_x * df_a < 0:
            b = x
        else:
            a = x

    xmin = x
    fmin = f(xmin)
    return [xmin, fmin, neval, coords]
