
import numpy as np

def gauss_jordan(A,b):
    n=A.shape[0]
    forward(A,b,n)
    return back(A,b,n)

def forward(A,b,n):
   for k in range(0,n) :
        for i in range(0,n) :
            if i==k :
               continue
            m=-A[i][k]/A[k][k]
            for j in range(0,n) :
                A[i][j]=A[i][j]+m*A[k][j]
            b[i]=b[i]+b[k]*m
   return A


def back(A,b,n):
    x=np.zeros((n,1),dtype=float)
    for i in range(0,n):
      x[i]=b[i]/A[i][i]
    return x



