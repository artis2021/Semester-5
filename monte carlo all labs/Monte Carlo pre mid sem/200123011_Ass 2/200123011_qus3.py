import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random

# if using a Jupyter notebook, kindly uncomment following line:
# %matplotlib inline

samp_given = [10, 100, 1000, 10000, 100000]



for data_points in samp_given:
  np.random.seed(42)
  seq_number = random.uniform(size=data_points) 
  print(len(seq_number))



  X = list()
  for i in seq_number:
    val = 0.5 - 0.5*math.cos(i*cmath.pi)
    X.append(val)



  y_in_sorted = np.sort(X)
  y_val = np.arange(len(y_in_sorted))/float(len(y_in_sorted) - 1)
  


  plt.title('Distribution Function of X ( sample count = {} )'.format(data_points))
  plt.ylabel('Probability - P(X <= x)')
  plt.xlabel('X (generated values)')
  plt.plot(y_in_sorted, y_val, color='purple')
  plt.show()




#   plt.title('Frequency Distribution of X ( sample count = {} )'.format(data_points))
#   counts, bin_edges = np.histogram(X, bins=np.arange(min(X), max(X)+0.001, 0.01))
#   plt.ylabel('Frequency')
#   plt.xlabel('X (generated values)')
#   plt.plot(bin_edges[1:], counts)
#   plt.show()





  print("Sample count =", data_points)
  print("Mean =", np.mean(X))
  print("Variance =", np.var(X))
  print()





x = np.arange(0, 1.001, 0.01)
Fx = [(2/cmath.pi)*math.asin(math.sqrt(i)) for i in x]



plt.plot(x, Fx, color='yellow')
plt.title('Actual Distribution Function')
plt.ylabel('F (x) ')
plt.xlabel('x')
plt.show()