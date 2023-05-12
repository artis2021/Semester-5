import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random

def function1(t):
    return 20*t*((1-t)**3)

def function2(u):
    return 2*(1-u)
    # return 1



def graph(sum , j , sum_2 , num):
    x = []
    a = 0
    while a<1:
        x.append(a)
        a+=0.01
    
    y = []

    for a in x:
        y.append(function1(a))
    
    plt.title('Frequency Distribution of X - Histograms')
    plt.plot(x,y)
    plt.hist(num , bins = 50 , rwidth=0.75 , density=True , color='yellow')
    plt.xlabel('X')
    plt.ylabel('Frequency')
    plt.show()
    



def solve(z):
    # sum of random numbers which are accepted
    sum1 = 0
    # sum of all random number which are accepted and lies  between 0.25 and 0.75
    sum_2 = 0
    # random no. list
    number1 = []
    i = 0
    j = 0
    while i<10000 :
        t1 = random.randint(0,1000);
        U = t1/1000
        x = 1-math.sqrt(1-U)
        f_x = function1(x)
        g_x = function2(x)
        t2 = random.randint(0 , 1000)
        # generating another random no. 
        r2 = t2/1000
        if(g_x!=0):
            if f_x/(z*g_x)>r2:
                number1.append(x)
                sum1+=x
                i+=1
                if x>=0.25 and x<=0.75 :
                    sum_2+=x
            
        j+=1
    

    # mean of accepted random no
    mean1 = sum1/10000
    print('I took c= ' , z)

    # part B

    print('Mean of Accepted no.= ', mean1)

    # part C

    print('Probability of accepted no b/w 0.25 and 0.75 is: ' , sum_2/10000)

    # part D

    print('Total no of Iteration for finding 10000 random variables is: ', j)
    print('Average no. of iterations: ' , j/10000)

    return sum1 , j , sum_2 , number1


sum , j , sum_2 , num = solve(1.4815)
graph(sum , j , sum_2 , num)

# sum , j , sum_2 , num = solve(2.109375)
# graph(sum , j , sum_2 , num)

sum , j , sum_2 , num = solve(3)
graph(sum , j , sum_2 , num)

sum , j , sum_2 , num = solve(10)
graph(sum , j , sum_2 , num)