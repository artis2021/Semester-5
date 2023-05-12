import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import cmath
import math


def Covariance(x, y):
    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))
    sub_x =[j - mean_x for j in x]
    sub_y = [j - mean_y for j in y]
    numerator = sum([sub_x[j]*sub_y[j] for j in range(len(sub_x))])
    denominator = len(x)-1
    covariance = numerator/denominator
    return covariance

def findIm(lmt):
    U = list()
    Y = list()
    Y2= list()
    S = list()
    X2= list()
    j = 0

    for j in range(0,lmt) :
        x = np.random.uniform(0,1)
        U.append(x)
    j = 0
    sum1 = 0
    sum2 = 0

    for x in U:
        x2=np.sqrt(x)
        X2.append(x2)
        k2=np.exp(np.sqrt(x))
        Y2.append(k2)
        
    mcv=np.mean(X2) 
    vcv=np.var(X2)  
    a=Covariance(X2,Y2)/vcv 

    for x in U:
        j+=1
        k=(np.exp(np.sqrt(x)) - a*(np.sqrt(x)-mcv))  
        Y.append(k)
        sum1+=x
        S.append((k - (sum1/j))**2)
        sum2+=((k - (sum1/j))**2)

    s_n = np.sqrt(sum2/(lmt-1))
    I_m = np.mean(Y)
    u_m = np.mean(U)
    l=np.var(Y)
    l2=np.var(Y2)
    h=((l2-l)/l2)*100
    openI = I_m-(1.96*(s_n/np.sqrt(lmt)))
    clostI = I_m+(1.96*(s_n/np.sqrt(lmt)))

    print("value of I_m = {}".format(I_m))
    print("The  95 percent confidence interval for the I is ({} , {})".format(openI , clostI))
    print("Variance of y : {}".format(l))
    print("Old Variance of y : {}".format(l2))
    print("Percent of variance reduction : {}%".format(h))
    print()
    print()



print("The exact value of I is 2.")

findIm(100)
findIm(1000)
findIm(10000)
findIm(100000)