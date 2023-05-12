import matplotlib.pyplot as plt
import numpy as np


#create title as plt.title('dcjbdcjk');
# loc is use for position the title and label
#add grid line as plt.grid();

x=np.array([2,4,7,9,1,4,7]);
y=np.array([0,9,8,7,6,5,4]);

plt.plot(x,y);

plt.title('hello dear',loc='left');
plt.xlabel('hii');
plt.ylabel('bii');
# plt.grid(axis='y');
plt.grid();
plt.show();


#line property for grid

x=np.array([1,2,3,4]);
y=np.array([6,7,8,0]);

plt.plot(x,y);
plt.grid(color='green',linestyle='--',linewidth='0.9');

plt.show();


# Display multiple graph
# With the subplot() function you can draw multiple plots in one figure:

# plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot

# Super Title

x=np.array([2,3,4,5]);
y=np.array([0,9,8,7]);

plt.subplot(2,1,1);
plt.plot(x,y);
plt.title('hii');

x=np.array([5,8,2,6]);
y=np.array([1,0,3,8]);
plt.subplot(2,1,2);
plt.plot(x,y);
plt.title('byyy');

plt.suptitle('yeee');
plt.show();



# Matplotlib Scatter  using scatter()  function 

x=([3,4,5,6,7,8,9,0]);
y=([1,0,9,8,7,6,5,4]);

plt.scatter(x,y,color='yellow');

plt.show();



#Draw two plots on the same figure:
#You cannot use the color argument for this, only the c argument.

x=np.array([23,34,56,67,89,9,2,32,54,5]);
y=np.array([90,98,67,56,45,34,21,67,0,7]);

plt.scatter(x,y);

x=np.array([1,2,3,4]);
y=np.array([2,3,4,5]);
col=np.array(['red','green','yellow','pink']);
plt.scatter(x,y,c=col);
plt.show();



#colormap
# Size
# You can change the size of the dots with the s argument.

# Alpha
# You can adjust the transparency of the dots with the alpha argument.


x=np.array([1,5,2,7]);
y=np.array([0,4,9,1]);
col=np.array([30,0,100,80]);
sz=np.array([100,500,20,80]);

plt.scatter(x,y,cmap='viridis',c=col,s=sz,alpha=0.7);
plt.colorbar();
plt.show();



#Combine Color Size and Alpha

x=np.random.randint(100,size=(100));
y=np.random.randint(100,size=(100));

col=np.random.randint(100,size=(100));
sz=10*np.random.randint(100,size=(100));

plt.scatter(x,y,c=col,s=sz,alpha=0.5,marker='*',cmap='nipy_spectral');
plt.colorbar();
plt.show();