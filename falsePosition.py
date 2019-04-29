import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.pyplot as plt
from sympy import sympify, Symbol
curr_pos = 0

def false_position(st,maxnum,maxer):
  x=sp.Symbol('x')
  y=sp.Symbol('y')
  H = sympify(st)
  x1=[]
  y1=[]
  xu=[]
  xl=[]
  fl=[]
  fu=[]
  xks=[]
  ys=[]
  errors=[]
  plots=[]
  print(float(H.subs(x,0)))
  xlf=0.0
  xuf=3.0
  ys.append(float(H.subs(x,xuf)))
  ys.append(float(H.subs(x,xlf)))
  i=0.0
  err=1
  while i <= 10:
    x1.append(i)
    y1.append(float(H.subs(x,i)))
    i=i+0.01
  maxsize=maxnum
  for i in range(0, maxsize, 1):
   xl.append(xlf)
   xu.append(xuf)
   if(err<=maxer):
      break
   x2=[xlf,xuf]
   flx=float(H.subs(x,xlf))
   fux=float(H.subs(x,xuf))
   y2=[flx,fux]
   plots.append((x2,y2))
   xk=xlf*fux-xuf*flx
   xk=xk/(fux-flx)
   xks.append(xk)
   if i==0:
    errors.append(1.0)
    print(i)
   else:
    err=abs((xks[i]-xks[i-1])/xks[i])
    errors.append(err)
   f=float(H.subs(x,xk))
   ys.append(f)
   if f<0:
      xlf=xk
   else:
      xuf=xk 
  def key_event(e):
    global curr_pos

    if e.key == "right":
        curr_pos = curr_pos + 1
    elif e.key == "left":
        curr_pos = curr_pos - 1
    else:
        return
    curr_pos = curr_pos % len(plots)
    axes = plt.gca()
    ax.cla()
    axes.set_xlim([1.3*xl[0],1.3*xu[0]])
    axes.set_ylim([1.3*min(ys),1.3*max(ys)])
    ax.plot(plots[curr_pos][0], plots[curr_pos][1],'r',plots[curr_pos][0], plots[curr_pos][1],'ro',plots2[1][0], plots2[1][1],'g',[-200,200],[0,0],'y')
    plt.title("Iteration "+str(curr_pos)+" xr= "+str(xks[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
    fig.canvas.draw()   
  plots2 = [(x1,y1),(x1,y1)]
  curr_pos = 0
  print(xl)
  fig = plt.figure()
  axes = plt.gca()
  axes.set_xlim([1.3*xl[0],1.3*xu[0]])
  axes.set_ylim([1.3*min(ys),1.3*max(ys)])
  fig.canvas.mpl_connect('key_press_event', key_event)
  ax = fig.add_subplot(111)
  ax.plot(plots[curr_pos][0], plots[curr_pos][1],'r',plots[curr_pos][0], plots[curr_pos][1],'ro',plots2[1][0], plots2[1][1],'g',[-200,200],[0,0],'y')
  plt.show()
false_position('(x^4)+(3*x)-4',10,0.5*10**-2)
