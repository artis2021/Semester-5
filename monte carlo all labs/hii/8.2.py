import matplotlib.pyplot as plt
import math
import cmath
import random
import pandas as pd
from scipy.stats import norm
import numpy as np

N=1000
h=0.5

#generate Exp(1) using inverse transform
def genrate_inverse_trans():
    seq1=[]
    for i in range(N):
        u=np.random.uniform(0,1)
        seq1.append(-np.log(u))
    return seq1

print("estimate generated using inverse tranform method= ", np.mean(genrate_inverse_trans()))  
print("varince of estimator generated using inverse transform method = ", np.var(genrate_inverse_trans()))  
print(" ")

#generate random variable of density q(x)
def genrate_essential_cher():
    seq1=[]
    for x in range(N):
        a=np.random.uniform(0,1)
        seq1.append(np.log(a)/(h-1))
    return seq1

#generate esimator value by importance sampling using q(x) 
def genEstimator():
    sq1=genrate_essential_cher()
    return np.exp(np.multiply(-h,sq1))/(1-h) 

print("estimate generated using importance sampling method =", np.mean(genEstimator()))
print("variance of estimator generated using importance sampling method= ",np.var(genEstimator()))
print(" ")


var1=np.var(genEstimator())
var2=np.var(genrate_inverse_trans())
print("amount of reduction in variance= ",(var2-var1)/var2 *100)          