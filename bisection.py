import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.pyplot as plt
from sympy import sympify, Symbol
curr_pos = 0
import numpy as np
import os.path
import sys 
def bisection(st,maxnum,maxer,xlf,xuf):
  save_path = 'K:/Works/Python/'
  completeName = os.path.join(save_path, "test"+".txt")         
  file1 = open(completeName, "w")
  x=sp.Symbol('x')
  e=sp.Symbol('e')
  y=sp.Symbol('y')
  H = sympify(st)
  print(H)
  table = []
  x1=[]
  y1=[]
  xu=[]
  xl=[]
  xks=[]
  ys=[]
  errors=[]
  plots=[]
  print(((H.subs(x,xuf)).subs(e,2.71828182846)))
  ys.append(float((H.subs(x,xuf)).subs(e,2.71828182846)))
  ys.append(float((H.subs(x,xlf)).subs(e,2.71828182846)))
  i=0.0
  err=1
  maxsize=maxnum
  if(ys[1]>0.0 and ys[0]<0.0):
    temp=xlf
    xlf=xuf
    xuf=temp
  if(ys[0]*ys[1]>0.0):
      print("error wrong interval")
      return
  print(maxnum)
  for i in range(0, maxsize, 1):
   xl.append(xlf)
   xu.append(xuf)
   print('xl ='+ str(xlf))
   print('xu ='+ str(xuf))
   if(err<=maxer):
      break
   xk=xlf+xuf
   xk=xk/2
   print('xk ='+ str(xk))
   x2=[xk,xk]
   y2=[-100,100]
   plots.append((x2,y2))
   xks.append(xk)
   if i==0:
    errors.append(1.0)
    print(i)
   else:
    err=abs((xks[i]-xks[i-1])/xks[i])
    print(str((xks[i]-xks[i-1])))
    errors.append(err)
   f=float((H.subs(x,xk)).subs(e,2.71828182846))
   print("fk ="+str(f))
   f2=float((H.subs(x,xlf)).subs(e,2.71828182846))
   print("fl ="+str(f2))
   f3=f*f2
   ys.append(f)
   print (xl[0],xu[0])
   print(f)
   table.append([xuf,xlf,xk,f,f2,err])
   if f3<0:
      xuf=xk
   else:
      xlf=xk 
  i=min([xl[0],xu[0]])
  add=(abs((xu[0])-(xl[0]))/100)
  print ("min = "+str(i)+" add = "+str(add)+ "max = "+str(max([xl[0],xu[0]])))
  while i <= max([xl[0],xu[0]]):
    x1.append(i)
    print("x="+str(i)+ " y = "+str(float((H.subs(x,i)).subs(e,2.71828182846))))
    y1.append(float((H.subs(x,i)).subs(e,2.71828182846)))
    i=i+add
  teams_list = ["        Xu      ", "   Xl      ", "   Xr      ","   F(Xr)      ","   F(Xl)      ","   Error      "]
  row_format ="{:>10}  " * (len(teams_list) + 1)
  row_format2 ="{:>10.10f}  " * (len(teams_list) + 1)
  file1.write(row_format.format("iteration", *teams_list))
  file1.write("\n")
  print (row_format.format(0, *teams_list))
  number=1
  for  row in table:
    print (row_format2.format(0, *row))
    file1.write(row_format2.format(number, *row))
    number=number+1
    file1.write("\n")
  file1.close()
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
    axes.set_xlim([xl[0],xu[0]])
    axes.set_ylim([min(ys),max(ys)])
    ax.plot([xl[curr_pos],xl[curr_pos]], [-200,200],'r',plots2[0][0], plots2[0][1],'g',[xu[curr_pos],xu[curr_pos]],[-200,200],'b',[-200,200],[0,0],'y')
    plt.title("Iteration "+str(curr_pos+1)+" xr= "+str(xks[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
    fig.canvas.draw()   
  plots2 = [(x1,y1)]
  curr_pos = 0
  print(xl)
  fig = plt.figure()
  axes = plt.gca()
  axes.set_xlim([xl[0],xu[0]])
  axes.set_ylim([min(ys),max(ys)])
  fig.canvas.mpl_connect('key_press_event', key_event)
  ax = fig.add_subplot(111)
  plt.title("Iteration "+str(curr_pos+1)+" xr= "+str(xks[curr_pos])+" errors= "+str(errors[curr_pos]*100)+"%")
  ax.plot([xl[curr_pos],xl[curr_pos]], [-200,200],'r',plots2[0][0], plots2[0][1],'g',[xu[curr_pos],xu[curr_pos]],[-200,200],'b',[-200,200],[0,0],'y')
  plt.show()
