import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.pyplot as plt
from sympy import sympify, Symbol
curr_pos = 0

def false_position(st,maxnum,maxer,xlf,xuf):
  x=sp.Symbol('x')
  y=sp.Symbol('y')
  H = sympify(st)
# x and y for the function to plot it
  x1=[]
  y1=[]
  # x and y for lower pound
  xl=[]
  fl=[]
  # x and y for upper pound
  xu=[]
  fu=[]
  # different values of xk
  xks=[]
  # different values of ys to determine upper and lower pound for the axis
  ys=[]
  # store the value of each error
  errors=[]
  # store plots which mean the steps of this method
  plots=[]
  # store the first two values of ys in the ys array
  ys.append(float(H.subs(x,xuf)))
  ys.append(float(H.subs(x,xlf)))
  i=0.0
  err=1
  maxsize=maxnum
  # loop to determine the points to draw the function
  while i <= 100:
    x1.append(i)
    y1.append(float(H.subs(x,i)))
    i=i+0.1
  # loop to get the value of xk
  for i in range(0, maxsize, 1):
  # store the value of xl and xu
   xl.append(xlf)
   xu.append(xuf)
  # test the error pound
   if(err<=maxer):
      break
  # make two points that represent the line from xl to xu
   x2=[xlf,xuf]
   flx=float(H.subs(x,xlf))
   fux=float(H.subs(x,xuf))
   y2=[flx,fux]
  # add this points to the plots
   plots.append((x2,y2))
  # evaluate the value of xk and store it
   xk=xlf*fux-xuf*flx
   xk=xk/(fux-flx)
   xks.append(xk)
  # if this is the first loop put the error is max =1
   if i==0:
    errors.append(1.0)
   else:
  # get the value of error
    err=abs((xks[i]-xks[i-1])/xks[i])
    errors.append(err)
  # get the value of y to store it in ys
   f=float(H.subs(x,xk))
   ys.append(f)
  # replace the value of xl or xu with the new xk
   if f<0:
      xlf=xk
   else:
      xuf=xk 
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
false_position('(x^4)+(3*x)-4',30,0.5*10**-2,0,3)
