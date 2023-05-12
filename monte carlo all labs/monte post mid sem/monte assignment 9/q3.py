
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd


# The Euler approximated recursion with time dependent µ and σ is given by
# Y (ti+1) = Y (ti) + µ(ti)(ti+1 − ti) + σ(ti)((ti+1 − ti)^0.5)Zi+1
# Repeat the above exercise by taking Y (0) = 5, µ(t) = 0.0325 − 0.05t, σ(t) = 0.012 + 0.0138t + 0.00125t^2

time_stamp = 0.001
n = 5000

Y_2 = 0 
Y_5 = 0

X_axis_array = []
Y_axis_array = []
for j in range(10):
    X_axis_array.append(0)
    Y_axis_array.append(5)

    for i in range(1, n + 1):
        t_value = time_stamp*i
        z_value = np.random.normal(0, 1, 1)
        mu = 0.0325 - 0.05*t_value
        sigma = 0.012 + 0.0138*t_value + 0.00125*pow(t_value,2)
        y_value = Y_axis_array[i - 1] + mu*time_stamp + sigma*pow(time_stamp, 0.5)*z_value[0]

        X_axis_array.append(t_value)
        Y_axis_array.append(y_value)

        if (i == 2):
            Y_2 += y_value 
        
        if (i == 5):
            Y_5 += y_value
    
    plt.plot(X_axis_array, Y_axis_array)
    X_axis_array.clear()
    Y_axis_array.clear()

plt.show()

print("Estimated value of E[X(2)] is", Y_2 / 10)
print("Estimated value of E[X(5)] is", Y_5 / 10)