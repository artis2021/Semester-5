import numpy as np
import random
import math
import matplotlib.pyplot as plt

def pi(x):
    return x*np.exp(-x)

def auto_corelation(seq,leg):
    x=list()
    y=list()
    i=0
    j=leg
    while(i<len(seq) and j<len(seq)):
        x.append(seq[i])
        y.append(seq[j])
        i+=1
        j+=1
        mat=np.cov(x,y)
        return mat[0][1]/np.sqrt(mat[0][0]*mat[1][1])


def trace_plot(seq):
    x=list()
    for i in range(0,len(seq)):
        x.append(i)
    plt.plot(x,seq)
    plt.show()

def generate_chain_symmetric():
    seq=list()
    x0=5
    ctrol=0
    while ctrol<5000:
        z=np.random.normal()
        newx=z+x0
        alpha=pi(newx)/pi(x0)
        if alpha>=1:
            x0=newx
            ctrol+=1
            seq.append(x0)
        else:
            u=np.random.uniform()
            if(alpha>=0.5):
                if(u>1-alpha):
                    x0=newx
                    ctrol+=1
                    seq.append(x0)
            else:
                if(u<=alpha):
                    x0=newx
                    ctrol+=1
                    seq.append(x0)
    print("autocorealtoin with leg 0 for symmetric mcmc is ",auto_corelation(seq,0))
    print("autocorealtoin with leg 50 for symmetric mcmc is ",auto_corelation(seq,50))
    print("autocorealtoin with leg 100 for symmetric mcmc is ",auto_corelation(seq,100))
    print("autocorealtoin with leg 150 for symmetric mcmc is ",auto_corelation(seq,150))
    print()
    trace_plot(seq)





def generate_chain_independent():
    seq=list()
    x0=5
    ctrol=0
    while ctrol<5000:
        z=np.random.normal()
        newx=z
        alpha=pi(newx)*np.exp((newx*newx-x0*x0)/2)/pi(x0)
        if alpha>=1:
            x0=newx
            ctrol+=1
            seq.append(x0)
        else:
            u=np.random.uniform()
            if(alpha>=0.5):
                if(u>1-alpha):
                    x0=newx
                    ctrol+=1
                    seq.append(x0)
            else:
                if(u<=alpha):
                    x0=newx
                    ctrol+=1
                    seq.append(x0)
    print("autocorealtoin with leg 0 for independent mcmc is ",auto_corelation(seq,0))
    print("autocorealtoin with leg 50 for independent mcmc is ",auto_corelation(seq,50))
    print("autocorealtoin with leg 100 for independent mcmc is ",auto_corelation(seq,100))
    print("autocorealtoin with leg 150 for independent mcmc is ",auto_corelation(seq,150))
    print()
    trace_plot(seq)


    
def generate_chain_random_walk():
    seq=list()
    x0=5
    ctrol=0
    while ctrol<5000:
        z=np.random.normal()
        newx=z+x0
        alpha=pi(newx)/pi(x0)
        if alpha>=1:
            x0=newx
            ctrol+=1
            seq.append(x0)
        else:
            u=np.random.uniform()
            if(alpha>=0.5):
                if(u>1-alpha):
                    x0=newx
                    ctrol+=1
                    seq.append(x0)
            else:
                if(u<=alpha):
                    x0=newx
                    ctrol+=1
                    seq.append(x0)
    print("autocorealtoin with leg 0 for random walk mcmc is ",auto_corelation(seq,0))
    print("autocorealtoin with leg 50 for random walk mcmc is ",auto_corelation(seq,50))
    print("autocorealtoin with leg 100 for random walk mcmc is ",auto_corelation(seq,100))
    print("autocorealtoin with leg 150 for random walk mcmc is ",auto_corelation(seq,150))
    print()
    trace_plot(seq)

generate_chain_random_walk()    