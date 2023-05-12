import random
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

def l_bound(arr,val,n):
    i=0
    en=n
    while(i<en):
        mid=math.floor((i+en)/2)
        if(arr[mid]>val):
            en=mid
        else:
            i=mid+1
    return i            


def eval(n):
    arr=np.random.normal(0,1,n)
    arr.sort()
    array1=[]
    for i in range(0,n):
        u=random.random()
        y=-1*math.log(u)
        gen=l_bound(arr,(1-y)/2,n)
        gen/=n
        array1.append(gen)
    print("for the given procedure,expected value is {} and variance is {}".format(np.mean(array1),np.var(array1)))    
    return np.var(array1)

def antithetic(n):
    arr=np.random.normal(0,1,n)
    arr.sort()
    array1=[]
    for i in range(0,n):
        u=random.random()
        y=-1*math.log(u)
        y1=-1*math.log(1-u)
        gen=l_bound(arr,(1-y)/2,n)
        gen+=l_bound(arr,(i-y1)/2,n)
        gen/=(2*n)
        array1.append(gen)
    print(" for the given procedure the expected value is {} and variance is {}".format(np.mean(array1),np.var(array1)))
    return np.var(array1)

x1_val=eval(100000)
x2_val=antithetic(100000)
print(" % variance reduction is {}".format((1-x2_val/x1_val)*100))    


