
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

#  We Have to Generate 10 sample paths for the standard Brownian Motion in the time interval [0,T]= [0, 5] using the recursion technique that written below 

# W(ti+1) = W(ti) + ((ti+1 − ti)^0.5)Zi+1

# with 5000 generated values for each of the paths where Zi+1 ∼ N(0, 1). Plot all the sample paths in a single figure.
# Also estimate the value of  E[W(2)] and E[W(5)] from the 10 paths that you have generated.
time_stamp = 0.001
n = 5000

W_2 = 0 
W_5 = 0

X_Array = []
Y_Array = []
for j in range(10):
    X_Array.append(0)
    Y_Array.append(0)

    for i in range(1, n + 1):
        t = time_stamp*i
        z = np.random.normal(0, 1, 1)
        w = Y_Array[i - 1] + pow(time_stamp, 0.5)*z[0]

        X_Array.append(t)
        Y_Array.append(w)

        if (i == 2):
            W_2 += w
        
        if (i == 5):
            W_5 += w
    
    plt.plot(X_Array, Y_Array)
    X_Array.clear()
    Y_Array.clear()

plt.show()

print("The Estimated value of E[W(2)] is: ", W_2 / 10)
print("The Estimated value of E[W(5)] is: ", W_5 / 10)

