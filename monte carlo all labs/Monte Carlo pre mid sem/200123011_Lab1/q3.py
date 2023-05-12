import matplotlib.pyplot as plt
import random

def gene_plot(a,b,m,k):    
    # values of u
    arr = []
    n = k
    for i in range(10000):
        arr.append(n/m)    
        n = (a*n+b)%m
    
    # stores the values of u[i-1]
    vec1 = []
    
    # stores the values of u[i]
    vect = []

    for i in range(1,len(arr)):
        vec1.append(arr[i-1])
        vect.append(arr[i])

    plt.scatter(vec1,vect,s = 0.05,c='brown')
    plt.show()

def main():
    a = 1229
    b = 1
    m = 2048
    x0 = random.randint(0,m)
    gene_plot(a,b,m,x0)

if __name__ == '__main__':
    main()
        



    