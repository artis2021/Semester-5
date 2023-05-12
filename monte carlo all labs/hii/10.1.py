from statistics import NormalDist
import numpy as np
import matplotlib.pyplot as plt
import math

s0=100
paths = []
def generatePaths(u, sig):    
    s=[s0]
    for t in range(1,5000):
        ti=t/1000
        zt=np.random.normal(loc=0.0, scale=1.0, size=1)
        st= s[t-1]* math.exp( (u-sig*sig/2)*1/1000 +  sig*math.sqrt(1/1000)*zt)
        s.append(st)
        
    #print(s)
    return s

sum2=0 
s5=[]
u=-0.1
sig=0.04
for i in range(10):
    path = generatePaths(u, sig)
    s5.append(path[4999])   
    paths.append(path)
    
    
# now plot all paths in one figure 
x= [k/1000 for k in range(0,5000)]
fig, ax = plt.subplots()
for i in range(10):
    ax.plot(x, paths[i])

plt.title("geometric Brownian Motion")
plt.show()

e=s0*np.exp(u*5)
print("Simulated value of E[S[5]] = {}".format(np.mean(s5)))
print("Actual value of E[S[5]] = {}".format(e))

v=s0*s0*np.exp(2*u*5)*(np.exp(5*sig*sig)-1)
print("Simulated value of Var[S[5]] = {}".format(np.var(s5)))
print("Actual value of Var[S[5]] = {}".format(v))
