from turtle import color
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# xpoint=np.array([0,6]);
# ypoint=np.array([0,255]);
# plt.plot(xpoint,ypoint);
# plt.show();

print(matplotlib.__version__);

# one more example 

# x=np.array([1,8]);
# y=np.array([3,10]);

# plt.plot(x,y);
# plt.show();


#plot without line

# xx=np.array([3,7]);
# yy=np.array([0,100]);
# plt.plot(xx,yy,'o');
# plt.show();


# plot multiple point 

# x1=np.array([1,2,6,8]);
# y1=np.array([3,8,1,10]);
# plt.plot(x1,y1);
# plt.show();


# default x axis 
# below this code is not working 

# x2=np.array([0,1,2,3,4,5,6]);
# y2=np.array([1,10,20,30,40,50,60]);
# plt.plot(x2,y2);
# plt.show();


# marker


# x1=np.array([1,2,6,8]);
# y1=np.array([3,8,1,10]);
# plt.plot(x1,y1,marker='o');
# plt.show();

# x2=np.array([2,4,5,6]);
# y2=np.array([8,9,0,1]);
# plt.plot(x2,y2,marker='*');
# plt.show();



#formate string fmt
x3=np.array([6,2,9,1]);
y3=np.array([4,5,6,7]);
plt.plot(x3,y3,'o:g');     ## g,b,r,y, are the colours...
plt.show();

#marker size

x4=np.array([2,8,5,0]);
y4=np.array([0,9,8,7]);

plt.plot(x4,y4,marker='o',color='pink',ms=30);
plt.show();



#adding multiple line just adding the coordinate in plt.plot
#marker edge color by markeredgecolor  or mec    and markerfacecolor  or mfc
#linestyle='dotted'  for dotted line 
#linestyle='dashed'   for dashed line 
#linewidth='12.7'     for width of a line 

x=np.array([2,0,5,1]);
y=np.array([0,8,1,9]);
y2=np.array([12,23,34,45]);
x2=np.array([9,98,87,76]);

plt.plot(x,y,mec='red',color='yellow',marker='*',ms=40,mfc='green',linestyle='dashed',linewidth='6.5');
plt.plot(x2,y2);
plt.plot(x,y2,x2,y,color='red')
plt.show();