import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import cmath
import math

def findIm(lmt):
    A = list()
    B = list()
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
        B.append(np.exp(np.sqrt(x)))
        sum1+=x
        S.append((np.exp(np.sqrt(x)) - (sum1/i))**2)
        sum2+=((np.exp(np.sqrt(x)) - (sum1/i))**2)

    
    s_n = np.sqrt(sum2/(lmt-1))
    I_m = np.mean(B)
    u_m = np.mean(A)
    l=np.var(B)

    
    openI = I_m-(1.96*(s_n/np.sqrt(lmt)))
    clostI = I_m+(1.96*(s_n/np.sqrt(lmt)))

    print("value of I_m = {}".format(I_m))
    print("Variance of y :{}".format(l))
    print("The  95 percent confidence interval for the I :({} , {})".format(openI , clostI))
    print()
    print()


print("The exact value of I is 2 .")

print()
findIm(100)
findIm(1000)
findIm(10000)
findIm(100000)
