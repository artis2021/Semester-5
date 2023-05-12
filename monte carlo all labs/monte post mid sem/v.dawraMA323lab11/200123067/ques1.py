import numpy as np
import matplotlib.pyplot as plt


def generate_overlapping(seq):
    n=len(seq)
    x=list()
    y=list()
    for i in range(0,n):
        if i==n-1:
            break
        x.append(seq[i])
    
    for i in range(0,n):
        if i==0:
            continue
        y.append(seq[i])
    
    plt.scatter(x,y)
    plt.show()


def generate_histogram(seq):
    plt.hist(seq,ec="red",range=(0,1),bins=20)
    plt.show()

def van_der_corput(n):
    seq=list()
    for i in range(n+1):
        if i==0:
            continue
        tmp=i
        v=list()
        while tmp>0:
            v.append(tmp%2)
            tmp=tmp//2
        ans=0
        ctr=0
        for x in v:
            ans=ans+(x)*np.float_power(2,-ctr-1)
            ctr=ctr+1
        seq.append(ans)
    return seq
        
def lcg(n):
    
    a=16807
    m=(1<<31)-1

    last_x=23
    ans=list()
    for i in range(n):
        x=(a*last_x)%m
        u=x/m
        ans.append(u)
        last_x=x
    return ans

# print(van_der_corput(25))
# generate_overlapping(van_der_corput(1000))
# generate_histogram(van_der_corput(100000))
generate_histogram(lcg(100000))