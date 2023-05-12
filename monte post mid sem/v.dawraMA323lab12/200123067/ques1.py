#standard gamma distribution
#x^(a-1)e^(-x)/gamma(a)
#taking a to be 2
#proposal distribution is normal distribution
import numpy as np
import math
import matplotlib.pyplot as plt
def pi(x):
    return x*np.exp(-x)

# def q(x,mu):
#     return np.exp((x-mu)*(x-mu)/2)/np.sqrt(2*np.pi)

def metropolis_hastings(n):
    
    seq=list()
    
    while len(seq)<n:
        xo=0.45
        ctr=0
        while ctr<2000:
            z=np.random.normal()
            new_x=xo+z
            alpha=pi(new_x)/pi(xo)
            if alpha>=1:
                xo=new_x
                ctr=ctr+1
            else:
                u=np.random.uniform()
                if(alpha>=0.5):
                    if(u>1-alpha):
                        xo=new_x
                        ctr=ctr+1    
                else:
                    if(u<=alpha):
                        xo=new_x
                        ctr=ctr+1
        seq.append(xo)
    plt.hist(seq,density=1)
    plt.show()
    print("Mean for obtained seqeunce for n",n,"is",np.mean(seq))

#metropolis_hastings(100)
metropolis_hastings(2000)
# metropolis_hastings(500)




                    




