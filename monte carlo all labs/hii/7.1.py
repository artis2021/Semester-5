import random
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def fun(limit):
    A=list()
    B=list()
    S=list()
    i=0

    for i in range(0,limit):
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

    sn=np.sqrt(sum2/(limit-1))
    im=np.mean(B)
    um=np.mean(A)
    l=np.var(B)

    openI=im-(1.96*(sn/np.sqrt(limit)))
    closeI=im+(1.96*(sn/np.sqrt(limit)))

    print("val of im={}".format(im))
    print("variance of y {}".format(l))
    print(" the 95% confidence interval for i ({},{}) ".format(openI,closeI)) 
    print()
    print()

print("the exact val of i is 2")

print()
fun(100)
fun(1000)
fun(10000)
fun(100000)
fun(1000000)

