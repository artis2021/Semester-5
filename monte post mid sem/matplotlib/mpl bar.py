import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A','B','C','D']);
y=np.array([3,8,1,10]);

plt.bar(x,y,color='green');
plt.show();

# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
# bar width    width=0.3
#For horizontal bars, use height instead of width.

x=np.array(['A','B','C','D']);
y=np.array([3,8,1,10]);

plt.bar(x,y,color='green',width=0.2);
plt.barh(x,y,color='red',height=0.4)
plt.show();




# Create Histogram
# In Matplotlib, we use the hist() function to create histograms.


#A Normal Data Distribution by NumPy:

# NumPy to randomly generate an array with 10 values,
#  where the values will concentrate around 20,
#   and the standard deviation is 10.

x=np.random.normal(20,10,10);
plt.hist(x);
plt.show();