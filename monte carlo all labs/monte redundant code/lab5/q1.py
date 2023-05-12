
import random, math, matplotlib.pyplot as plt, numpy as np
from scipy.stats import multivariate_normal

def MarsalgiaBray(sz) :
    array_1=[]
    array_2=[]
    while len(array_1) < sz :
        rand_1=random.random()
        rand_2=random.random()
        rand_1=2*rand_1-1
        rand_2=2*rand_2-1
        R=rand_1**2+rand_2**2
        if R > 1:
            continue
        Z1=rand_1*math.sqrt((-2*math.log(R))/R)
        Z2=rand_2*math.sqrt((-2*math.log(R))/R)
        array_1.append(Z1)
        array_2.append(Z2)
    return [array_1, array_2]

def multivariate(sz, sigma, mean):
    multi=MarsalgiaBray(sz)
    dev1=math.sqrt(sigma[0][0])
    dev2=math.sqrt(sigma[1][1])
    corr=sigma[0][1]/(dev1*dev2)
    for i in range(sz) :
        multi[1][i]=mean[1]+corr*dev2*multi[0][i]+math.sqrt(1-corr**2)*dev2*multi[1][i]
        multi[0][i]=mean[0]+dev1*multi[0][i]
    plt.hist2d(multi[0], multi[1], bins=(100, 100))
    x, y=np.mgrid[0:9:0.1, 0:16:0.1]
    pos=np.dstack((x, y))
    rv=multivariate_normal(mean, sigma, allow_singular=True)
    z=rv.pdf(pos)
    plt.contour(x, y, z)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title(f'Multivariate Normal Distribution for a = {a}')
    plt.show()

mean=[5, 8]
for a in [-0.5, 0, 0.5, 1] :
    sigma=[[1, 2*a], [2*a, 4]] 
    multivariate(10000, sigma, mean)