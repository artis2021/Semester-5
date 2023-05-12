import numpy as np
import pandas as pd
import math
import cmath
import random

def calculate_Im(up_to_limit):
    U = list()
    Y = list()
    S = list()
    i = 0
    for i in range(0,up_to_limit) :
        x = np.random.uniform(0,1)
        U.append(x)
    i = 0
    s = 0    #s=sum
    s1 = 0    #s1=sum1
    for x in U:
        i+=1
        Y.append(np.exp(np.sqrt(x)))
        s+=x
        S.append((np.exp(np.sqrt(x)) - (s/i))**2)
        s1+=((np.exp(np.sqrt(x)) - (s/i))**2)

    
    s_n = np.sqrt(s1/(up_to_limit-1))
    I_m = np.mean(Y)
    u_m = np.mean(U)

    
    open_i = I_m-(1.96*(s_n/np.sqrt(up_to_limit)))
    clost_i = I_m+(1.96*(s_n/np.sqrt(up_to_limit)))

    print("value of I_m = {}".format(I_m))
    print("The  95 percent confidence interval for the I is ({} , {})".format(open_i , clost_i))


print("The exact value of I id 2.")
calculate_Im(100)
calculate_Im(1000)
calculate_Im(10000)
calculate_Im(100000)