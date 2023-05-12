import matplotlib.pyplot as plt
import numpy as np

def generator(a,b,m,x,i,u):
    x0=x
    for z in range(17):
        x0=((a*x0)+b)%m
        u.append(x0/m)
    for z in range(17, i):
        u1=u[z-17]-u[z-5]
        if u1 < 0:
            u1 += 1
            u.append(u1)
        else:
            u.append(u1)




def plothist(u):
    plt.xlabel('interval')
    plt.ylabel('frequency')
    plt.hist(u, bins = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],edgecolor = 'black')
    plt.show()

def plotscat(u):
    ux=[]
    for z in range(0,len(u)-1):
        ux.append(u[z])
    uy=[]
    for z in range(1,len(u)):
        uy.append(u[z])
    plt.xlabel('u[i-1]')
    plt.ylabel('u[i]')
    plt.scatter(ux,uy)
    plt.show()

def main():
    a=625
    b=1
    m=1000
    x=754
    i=1000
    u1=[]
    u2=[]
    u3=[]


    generator(a,b,m,x,1000,u1)
    generator(a,b,m,x,10000,u2)
    generator(a,b,m,x,100000,u3)

    plothist(u1)
    plothist(u2)
    plothist(u3)

    plotscat(u1)
    plotscat(u2)
    plotscat(u3)
if __name__ == '__main__':
    main()