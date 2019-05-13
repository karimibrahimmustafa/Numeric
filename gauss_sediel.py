import numpy as np

class gaussSediel:


    def __init__(self,A,X_old,b,maxIteration,tor):
        self.A=A
        self.X_old=X_old
        self.maxIteration=maxIteration
        self.tor=tor
        self.numEqu=self.A.shape[0]
        self.error=np.zeros(self.numEqu, dtype=float)

    def solve(self):
        n = self.numEqu
        if not self.check_convergence(self.A, n):
            return False
        X_new = np.zeros(n, dtype=float)
        for k in range(0, self.maxIteration):
            for i in range(0, n):
                X_new[i] = self.b[i]
                for j in range(0, n):
                    if i == j:
                        continue
                    if i > j:
                        X_new[i] = X_new[i] - self.A[i][j] * X_new[j]
                    else:
                        X_new[i] = X_new[i] - self.A[i][j] * self.X_old[j]
                X_new[i] = X_new[i] / self.A[i][i]
            if self.check_error(X_new, self.X_old, self.tor, n, self.error):
                return X_new
            self.X_old[0:] = X_new
        return X_new


    def check_error(X_new, X_old, tor, n, error):
        done = True
        for i in range(0, n):
            error[i] = (abs(X_new[i] - X_old[i]) / X_new[i]) * 100
            if error[i] > tor:
                done = False
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
