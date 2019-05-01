import numpy as np
def gauss(A,b):
    n=A.shape[0]
    forward(A,b,n)
    return back(A,b,n)
def forward(A,b,n):
   for k in range(0,n-1) :
        for i in range(k+1,n) :
            m=-A[i][k]/A[k][k]
            for j in range(k+1,n) :
                A[i][j]=A[i][j]+m*A[k][j]
            b[i]=b[i]+b[k]*m
            A[i][k]=0
   return A

def back(A,b,n):
    x=np.zeros((n,1),dtype=float)
    x[n-1]=b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
      sum=b[i]
      for j in range(i+1,n):
        sum = sum - A[i][j]*x[j]
      x[i]=sum/A[i][i]
    return x





