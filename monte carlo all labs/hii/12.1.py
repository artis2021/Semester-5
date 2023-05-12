import numpy as np
import math
import matplotlib.pyplot as plt
import random

def pi(x):
    return x*np.exp(-x)

# def q(x,mu):
#     return np.exp((x-mu)*(x-mu)/2)/np.sqrt(2*np.pi)    

def metropolis_hasting(n):
    seq=list()

    while len(seq)<n:
        x0=0.45
        ctrol=0
        while ctrol<2000:
            z=np.random.normal()
            newx=x0+z
            aplha=pi(newx)/pi(x0)
            if aplha >=1:
                x0=newx
                ctrol+=1
            else:
                u=np.random.uniform()
                if(aplha>=0.5):
                    if(u>1-aplha):
                        x0=newx
                        ctrol+=1
                else:
                    if(u<=aplha):
                        x0=newx
                        ctrol+=1
        seq.append(x0)
    plt.hist(seq,density=1)
    plt.show()
    print("mean for obtained sequence for n",n,"is",np.mean(seq))

# metropolis_hasting(100)
# metropolis_hasting(2000)
metropolis_hasting(500)    

