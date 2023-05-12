import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

time_stamp=0.001
n=5000

W_2=0
W_5=0

xarray=[]
yarray=[]
for j in range(10):
    xarray.append(0)
    yarray.append(0)

    for i in range(1,n+1):
        t=time_stamp*i
        z=np.random.normal(0,1,1)
        w=yarray[i-1]+pow(time_stamp,0.5)*z[0]

        xarray.append(t)
        yarray.append(w)

        if(i==2):
            W_2+=w

        if(i==5):
            W_5  +=w

    plt.plot(xarray,yarray)
    xarray.clear()
    yarray.clear()

plt.show()

print("the estimated value of E[W(2)] is ",W_2/10)
print("the estimated value of E[W(5)] is ",W_5/10)




