import math
import random
import cmath
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def fun(lim):
    A=list()
    B=list()
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
        B.append(np.exp(np.sqrt(x)))
        sum1+=x
        S.append((np.exp(np.sqrt(x))-(sum1/i))**2)  
        sum2+=((np.exp(np.sqrt(x))-(sum1/i))**2) 

    sn=np.sqrt(sum2/(lim-1))
    im=np.mean(B)
    um=np.mean(A)
    l=np.var(B)

    open_i=im-(1.96*(sn/np.sqrt(lim)))
    close_i=im+(1.96*(sn/np.sqrt(lim)))

    print("value of im = {} ".format(im))
    print("variance of y {}".format(l))
    print("95% confidence interval for i ({},{})".format(open_i,close_i))


print(" value of im is 2" )
print()
fun(100)
fun(1000)
fun(10000)
fun(100000)
