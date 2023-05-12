import math, random, numpy as np
import scipy.special as scsp

def find_k(alpha) :
    integral=math.gamma(alpha)-scsp.gammaincc(alpha, 1)*math.gamma(alpha)

     #integration of function in interval (0, 1)

    #gammaincc(a, b) returns integral of e^-x * x^(a-1) over the interval (b, infinity) divided by gamma(a)
   
    return 1/integral

def calc(alpha) :
        
    k=find_k(alpha)
    #change it. It will vary in accordance with -> integration of kf(x) over (0, 1) is 1
    def fx(x):
        return k*math.pow(math.e, -x)* math.pow(x, alpha-1)
    def gx(x) :
        return alpha*math.pow(x, alpha-1)   
    def G_inv(x):
        return math.pow(x, 1/alpha)
    c=k/alpha
    def generate() :
        while True:
            y=random.random()
            x=G_inv(y)
            prob=fx(x)/(c*gx(x))
            event=random.random()
            if event <=prob :
                return x
    n=10000
    v=[]
    while len(v) < n :
        v.append(generate())
    print('Mean of the distribution is ', np.mean(v))
    print('Variance of the distribution is ', np.var(v))

print('(a)')
calc(0.7)
print('(b)')
calc(3)
print('(c)')
calc(3.7)