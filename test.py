import os.path
import bisection
save_path = 'K:/Works/Python/'


completeName = os.path.join(save_path, "input"+".txt")         

file1 = open(completeName, "r")
equation =(file1.readline())[:-1]
print("equation = "+equation)
method = file1.readline()[:-1]
x=file1.read(1)
x1=""
while(x!=" "):
    x1=x1+str(x)
    x=file1.read(1)
x2 = file1.readline()[:-1]
x1=float (x1)
x2=float (x2)
addition = file1.readline()
addition = float(addition)
max=addition
maxerr=addition
file1.close()
if(addition >1):
    print("max no of iteration is "+str(addition))
    max=int(addition)
    maxerr=1*10^-15
else:
    print("max error "+str(addition))
    max=50
if(method == "bisection"):
    bisection.bisection(equation,max,maxerr,x1,x2)
