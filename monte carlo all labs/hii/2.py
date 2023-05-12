import math
import cmath
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fun(lim):
    A=list()
    B1=list()
    B2=list()
    S=list()
    i=0

    for i in range(0,lim):
        x=np.random.uniform(0,1)
        A.append(x)

    i=0
    sum1=0
    sum2=0

    for x in A:
        i+=1
        k1=(np.exp(np.sqrt(x))+np.exp(np.sqrt(1-x)))/2
        k2=np.exp(np.sqrt(x))
        B1.append(k1)
        B2.append(k2)
        sum1+=x
        S.append((k1-(sum1/i))**2)
        sum2+=((k1-(sum1/i))**2)

    sn=np.sqrt(sum2/(lim-1))
    im=np.mean(B1)
    um=np.mean(A)
    l2=np.var(B2)
    h=((l2-1)/l2)*100


    openI=im-(1.96*(sn/np.sqrt(lim)))
    closeI=im+(1.96*(sn/np.sqrt(lim)))

    print("val of im= {}".format(im))
    print("variance of y {}".format(l2))
    print("old varianve of y {}".format(l2))
    print()

    print("95% confidence interval for i is ({},{})".format(openI,closeI))
    print("percentage of variance reduction {}%".format(h))
    print()
    print()

print("exact val of i is 2")
print()

fun(100)

fun(1000)

fun(10000)

fun(100000)



