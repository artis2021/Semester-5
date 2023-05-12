import numpy as np
import matplotlib.pyplot as plt

def radical_inverse(b,n):
    seq=list()
    for i in range(n+1):
        if i==0:
            continue
        tmp=i
        v=list()
        while tmp>0:
            v.append(tmp%b)
            tmp=tmp//b
        ans=0
        ctr=0
        for x in v:
            ans=ans+(x)*np.float_power(b,-ctr-1)
            ctr=ctr+1
        seq.append(ans)
    return seq

def f(n):
    x=radical_inverse(2,n)
    y=radical_inverse(3,n)
    plt.scatter(x,y)
    plt.show()

f(100)
f(100000)