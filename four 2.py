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
  while i <= 100 :
    x1.append(i)
    y1.append(float(H.subs(x,i)))
    i=i+0.01
  # loop to get the value of xk
  for i in range(0, maxsize, 1):
  # test the error pound
   
   fxi_value = float(H.subs(x,xi))
   fxi.append(fxi_value)
   dfxi_value = float(dif.subs(x,xi))
   dfxi.append(dfxi_value)
   x2=[xi]
   xi = xi - (fxi_value/dfxi_value)
   print(xi)
   xis.append(xi)
   x2.append(xi)
   y2=[fxi_value,0]
  # add this points to the plots
   plots.append((x2,y2))
   if i==0:
     errors.append(1.0)
   else:
     err=abs((xis[i]-xis[i-1])/xis[i])
     errors.append(err)
   if(err<=maxer):
      break
   i=i+1   
   minx=min(xis)-abs(min(xis))*0.3
   maxx=max(xis)+abs(max(xis))*0.3
   extra_ymin=float(H.subs(x,minx))
   extra_ymax=float(H.subs(x,maxx))
   maxy=  max(fxi)
   miny= min(fxi)
   maxy=max([maxy,extra_ymax])*1.3
   miny=min([miny,extra_ymin])
   if(miny<0.05):
        miny=-0.1*maxy
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
    axes.set_xlim([minx,maxx])
    axes.set_ylim([miny,maxy])
    print (maxx)
    print (maxy)
    print (minx)
    print (miny)
    # plot the line and the curve
    ax.plot(plots[curr_pos][0], plots[curr_pos][1],'r',plots[curr_pos][0], plots[curr_pos][1],'ro',plots2[1][0], plots2[1][1],'g',[-200,200],[0,0],'y',[xis[curr_pos],xis[curr_pos]],[-100,100],'b')
    # put the title of plot
    plt.title("Iteration "+str(curr_pos)+" xr= "+str(xis[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
    fig.canvas.draw()   
  # the plot of curve
  plots2 = [(x1,y1),(x1,y1)]
  curr_pos = 0
  # the same function to draw the plots
  fig = plt.figure()
  axes = plt.gca()
  axes.set_xlim([minx,maxx])
  axes.set_ylim([miny,maxy])
  fig.canvas.mpl_connect('key_press_event', key_event)
  ax = fig.add_subplot(111)
  ax.plot(plots[curr_pos][0], plots[curr_pos][1],'r',plots[curr_pos][0], plots[curr_pos][1],'ro',plots2[1][0], plots2[1][1],'g',[-200,200],[0,0],'y',[xis[curr_pos],xis[curr_pos]],[-100,100],'b')
  plt.title("Iteration "+str(curr_pos+1)+" xr= "+str(xis[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
  plt.show()
# calling the function with (String Function , max number of iterations , max error, xl,xu)
newton('(x^3)-0.165*x^2+3.933*10^-4',30,0.5*10**-2,0.05)
