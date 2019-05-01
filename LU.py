import numpy as np


def LU_Decomposition(A, b):
    n = A.shape[0]
    L = Decompose(A, n)
    U = A
    y = forward_sub(L, b, n)
    return back_sub(U, y, n)


def Decompose(A, n):
    L = np.eye(n, n)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            L[i][k] = m
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            A[i][k] = 0
    return L


def forward_sub(L, b, n):
    y = b
    for i in range(1, n):
        sum = b[i]
        for j in range(0, i):
            sum = sum - L[i][j] * y[j]
        y[i] = sum
    return y


def back_sub(U, y, n):
    x = np.zeros((n, 1), dtype=float)
    x[n - 1] = y[n - 1] / U[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum = y[i]
        for j in range(n - 1, i, -1):
            sum = sum - x[j] * U[i][j]
        x[i] = sum / U[i][i]
    return x
