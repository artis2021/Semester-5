import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import cmath
import math


def findIm(lmt):
    A = list()
    B1 = list()
    B2= list()
    S = list()
    i = 0

    for i in range(0,lmt) :
        x = np.random.uniform(0,1)
        A.append(x)

    i = 0
    sum1 = 0
    sum2 = 0

    for x in A:
        i+=1
        k1=(np.exp(np.sqrt(x))+np.exp(np.sqrt(1-x)))/2
        k2=np.exp(np.sqrt(x))
        B1.append(k1)
        B2.append(k2)
        sum1+=x
        S.append((k1 - (sum1/i))**2)
        sum2+=((k1 - (sum1/i))**2)

    
    s_n = np.sqrt(sum2/(lmt-1))
    I_m = np.mean(B1)
    u_m = np.mean(A)
    l=np.var(B1)
    l2=np.var(B2)
    h=((l2-l)/l2)*100
    

    
    openI = I_m-(1.96*(s_n/np.sqrt(lmt)))
    clostI = I_m+(1.96*(s_n/np.sqrt(lmt)))


    print("value of I_m = {}".format(I_m))
    print("Variance of y : {}".format(l))
    print("Old Variance of y : {}".format(l2))
    print()
    print("The  95 percent confidence interval for the I is ({} , {})".format(openI , clostI))
    print("Percent of variance reduction : {}%".format(h))
    print()
    print()



print("The exact value of I is 2.")
print()

findIm(100)
findIm(1000)
findIm(10000)
findIm(100000)