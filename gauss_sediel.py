import numpy as np


def gauss_seidal(A, X_old, b, maxIteration, tor):
    n = A.shape[0]
    if not check_convergence(A, n):
        return False
    X_new = np.zeros(n, dtype=float)
    error = np.zeros(n, dtype=float)
    for k in range(0, maxIteration):
        for i in range(0, n):
            X_new[i] = b[i]
            for j in range(0, n):
                if i == j:
                    continue
                if i > j:
                    X_new[i] = X_new[i] - A[i][j] * X_new[j]
                else:
                    X_new[i] = X_new[i] - A[i][j] * X_old[j]
            X_new[i] = X_new[i] / A[i][i]
        # print(X_new)
        # print(X_old)
        if check_error(X_new, X_old, tor, n, error):
            return X_new
        X_old[0:] = X_new
    return X_new


def check_error(X_new, X_old, tor, n, error):
    done = True
    for i in range(0, n):
        error[i] = (abs(X_new[i] - X_old[i]) / X_new[i]) * 100
        if error[i] > tor:
            done = False
    # print(error)
    # print("\n")
    return done


def check_convergence(A, n):
    done1 = False
    done2 = True
    for i in range(0, n):
        res = 0
        for j in range(0, n):
            if i == j:
                continue
            res = res + abs(A[i][j])
        if res < abs(A[i][i]):
            done1 = True
        if res > abs(A[i][i]):
            done2 = False
    return (done1 and done2)


