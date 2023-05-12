import matplotlib.pyplot as plt
import numpy as np
import random
import math
import cmath

time_stamp=0.001
n=5000
m1=0.06
sigma=0.3

x2=0
x5=0

x_array=[]
y_array=[]
for j in range(10):
    x_array.append(0)
    y_array.append(5)

    for i in range(1,n+1):
        time_stamp1=time_stamp*i
        z_array=np.random.normal(0,1,1)
        x_value=y_array[i-1]+m1*time_stamp+sigma*pow(time_stamp,0.5)*z_array[0]

        x_array.append(time_stamp1)
        y_array.append(x_value)

        if(i==2):
            x2+=x_value

        if(i==5):
            x5+=x_value

    plt.plot(x_array,y_array)
    x_array.clear()
    y_array.clear()

plt.show()

print("the estimated value of E[X(2)] is ",x2/10)
print("the estimated value of E[X(5)] is ",x5/10)




