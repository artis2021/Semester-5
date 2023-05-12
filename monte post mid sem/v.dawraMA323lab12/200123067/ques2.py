import numpy as np
import math
import matplotlib.pyplot as plt

def pi(x):
    return x*np.exp(-x)


def autocorelation(seq,lag):
    x=list()
    y=list()
    i=0
    j=lag
    while(i<len(seq) and j<len(seq)):
        x.append(seq[i])
        y.append(seq[j])
        i=i+1
        j=j+1
    mat=np.cov(x,y)
    return mat[0][1]/np.sqrt(mat[0][0]*mat[1][1])

def traceplot(seq):
    x=list()
    for i in range(0,len(seq)):
        x.append(i)
    plt.plot(x,seq)
    plt.show()

def generate_chain_symmetric():
        seq=list()
        xo=5
        ctr=0
        while ctr<5000:
            z=np.random.normal()
            new_x=z+xo
            alpha=pi(new_x)/pi(xo)
            if alpha>=1:
                xo=new_x
                ctr=ctr+1
                seq.append(xo)
            else:
                u=np.random.uniform()
                if(alpha>=0.5):
                    if(u>1-alpha):
                        xo=new_x
                        ctr=ctr+1  
                        seq.append(xo)  
                else:
                    if(u<=alpha):
                        xo=new_x
                        ctr=ctr+1
                        seq.append(xo)
        print("Autocorelation with lag 0 for symmetric mcmc is",autocorelation(seq,0))
        print("Autocorelation with lag 50 for symmetric mcmc is",autocorelation(seq,50))
        print("Autocorelation with lag 100 for symmetric mcmc is",autocorelation(seq,100))
        print("Autocorelation with lag 150 for symmetric mcmc is",autocorelation(seq,150))
        print()
        traceplot(seq)


def generate_chain_independent():
        seq=list()
        xo=5
        ctr=0
        while ctr<5000:
            z=np.random.normal()
            new_x=z
            alpha=pi(new_x)*np.exp((new_x*new_x-xo*xo)/2)/pi(xo)
            if alpha>=1:
                xo=new_x
                ctr=ctr+1
                seq.append(xo)
            else:
                u=np.random.uniform()
                if(alpha>=0.5):
                    if(u>1-alpha):
                        xo=new_x
                        ctr=ctr+1  
                        seq.append(xo)  
                else:
                    if(u<=alpha):
                        xo=new_x
                        ctr=ctr+1
                        seq.append(xo)
        print("Autocorelation with lag 0 for independent mcmc is",autocorelation(seq,0))
        print("Autocorelation with lag 50 for independent mcmc is",autocorelation(seq,50))
        print("Autocorelation with lag 100 for independent mcmc is",autocorelation(seq,100))
        print("Autocorelation with lag 150 for independent mcmc is",autocorelation(seq,150))
        print()
        traceplot(seq)



def generate_chain_random_walk():
        seq=list()
        xo=5
        ctr=0
        while ctr<5000:
            z=np.random.normal()
            new_x=xo+z
            alpha=pi(new_x)/pi(xo)
            if alpha>=1:
                xo=new_x
                ctr=ctr+1
                seq.append(xo)
            else:
                u=np.random.uniform()
                if(alpha>=0.5):
                    if(u>1-alpha):
                        xo=new_x
                        ctr=ctr+1  
                        seq.append(xo)  
                else:
                    if(u<=alpha):
                        xo=new_x
                        ctr=ctr+1
                        seq.append(xo)
        print("Autocorelation with lag 0 for random walk mcmc is",autocorelation(seq,0))
        print("Autocorelation with lag 50 for random walk mcmc is",autocorelation(seq,50))
        print("Autocorelation with lag 100 for random walk mcmc is",autocorelation(seq,100))
        print("Autocorelation with lag 150 for random walk mcmc is",autocorelation(seq,150))
        traceplot(seq)


generate_chain_random_walk()
