import random
import math
import cmath
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def Covariance(x,y):
    meanx=sum(x)/float(len(x))
    meany=sum(y)/float(len(y))
    subx=[j-meanx for j in x]
    suby=[j-meany for j in y]
    numerator=sum([subx[j]*suby[j] for j in range(len(subx))])
    denominator=len(x)-1
    covariance=numerator/denominator
    return covariance

def fun(limit):
        