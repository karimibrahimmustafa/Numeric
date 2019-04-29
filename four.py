import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.pyplot as plt
from sympy import sympify, Symbol
curr_pos = 0

def newton(st,maxnum,maxer,xi):
  x=sp.Symbol('x')
  y=sp.Symbol('y')
  H = sympify(st)
# x and y for the function to plot it
  x1=[]
  y1=[]
  # x and y for lower pound
  xis=[]
  # x and y for upper pound
  fxi=[]
  # different values of xk
  dfxi=[]
  # different values of ys to determine upper and lower pound for the axis
  # store the value of each error
  errors=[]
  # store plots which mean the steps of this method
  plots=[]
  # store the first two values of ys in the ys array
  xis.append(xi)
  dif=sp.diff(st,x)
  print(dif)
  i=0.0
  err=1
  maxsize=maxnum
  # loop to determine the points to draw the function
  while i <= 100 & i < 1.3*xi:
    x1.append(i)
    y1.append(float(H.subs(x,i)))
    i=i+0.1
  # loop to get the value of xk
  for i in range(0, maxsize, 1):
  # test the error pound
   fxi_value = float(H.subs(x,xi))
   fxi.append(fxi_value)
   dfxi_value = float(dif.subs(x,xi))
   dfxi.append(dfxi_value)
   x2=[xi]
   xi = xi - (fxi_value/dfxi_value)
   x2.append(xi)
   y2=[fxi_value,0]
  # add this points to the plots
   plots.append((x2,y2))
    if i==0:
     errors.append(1.0)
    else:
     err=abs((xi[i]-xi[i-1])/xi[i])
     errors.append(err)
   if(err<=maxer):
      break
   i=i+1   
  # function to move between plots
  def key_event(e):
    global curr_pos

    if e.key == "right":
        curr_pos = curr_pos + 1
    elif e.key == "left":
        curr_pos = curr_pos - 1
    else:
        return
    curr_pos = curr_pos % len(plots)
    # set the axis limits to fit the plot
    axes = plt.gca()
    ax.cla()
    axes.set_xlim([1.3*xl[0],1.3*xu[0]])
    axes.set_ylim([1.3*min(ys),1.3*max(ys)])
    # plot the line and the curve
    ax.plot(plots[curr_pos][0], plots[curr_pos][1],'r',plots[curr_pos][0], plots[curr_pos][1],'ro',plots2[1][0], plots2[1][1],'g',[-200,200],[0,0],'y')
    # put the title of plot
    plt.title("Iteration "+str(curr_pos+1)+" xr= "+str(xks[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
    fig.canvas.draw()   
  # the plot of curve
  plots2 = [(x1,y1),(x1,y1)]
  curr_pos = 0
  # the same function to draw the plots
  fig = plt.figure()
  axes = plt.gca()
  axes.set_xlim([1.3*xl[0],1.3*xu[0]])
  axes.set_ylim([1.3*min(ys),1.3*max(ys)])
  fig.canvas.mpl_connect('key_press_event', key_event)
  ax = fig.add_subplot(111)
  ax.plot(plots[curr_pos][0], plots[curr_pos][1],'r',plots[curr_pos][0], plots[curr_pos][1],'ro',plots2[1][0], plots2[1][1],'g',[-200,200],[0,0],'y')
  plt.title("Iteration "+str(curr_pos+1)+" xr= "+str(xks[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
  plt.show()
# calling the function with (String Function , max number of iterations , max error, xl,xu)
newton('(x^4)+(3*x)-4',30,0.5*10**-2,0)
