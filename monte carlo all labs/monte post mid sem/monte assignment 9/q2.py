
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# Repeat the above exercise with the following Brownian motion (BM(µ, σ2)) discretization X(ti+1) = X(ti) + µ(ti+1 − ti) + σ(√ti+1 − t))z_arrayi+1. 
# Take the following values  X(0) = 5, µ = 0.06 and σ = 0.3.

time_stamp = 0.001
n = 5000
m1 = 0.06
sigma = 0.3

X_2 = 0 
X_5 = 0

X_axis_array = []
Y_axis_array = []
for j in range(10):
    X_axis_array.append(0)
    Y_axis_array.append(5)

    for i in range(1, n + 1):
        time_stamp_1 = time_stamp*i
        z_array = np.random.normal(0, 1, 1)
        x_value = Y_axis_array[i - 1] + m1*time_stamp + sigma*pow(time_stamp, 0.5)*z_array[0]

        X_axis_array.append(time_stamp_1)
        Y_axis_array.append(x_value)

        if (i == 2):
            X_2 += x_value 
        
        if (i == 5):
            X_5 += x_value
    
    plt.plot(X_axis_array, Y_axis_array)
    X_axis_array.clear()
    Y_axis_array.clear()

plt.show()

print("The Estimated value of E[X(2)] is: ", X_2 / 10)
print("The Estimated value of E[X(5)] is: ", X_5 / 10)
