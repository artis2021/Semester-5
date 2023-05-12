import matplotlib.pyplot as plt
import numpy as np

x=np.array([30,20,40,10]);
y=np.array([5,10,15,20]);
x1=np.array([5,6,7,8]);
x2=np.array([5,6,7,8]);
x3=np.array([16,17,18,19,20]);
y3=np.array([36,37,38,39,40]);
x4=np.array([5,6,7,8]);
y4=np.array([36,37,38,39]);

plt.plot(y,x,color='yellow',marker='*',ms='40',linewidth='4.5',linestyle='dashed',mfc='green',mec='red');
plt.plot(x1,x2,color='yellow',mec='red',ms='30',marker='*');
plt.plot(x3,y3,color='green',mec='red',ms='30',marker='*');

plt.plot(x4,y4,color='red',marker='*',mec='yellow',ms='30');
plt.show();
