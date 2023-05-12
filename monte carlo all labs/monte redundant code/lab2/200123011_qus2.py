import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random


given_inputs = [10, 100, 1000, 10000, 100000]

for data_numbers in given_inputs:
  np.random.seed(42)
  seq_numbers = random.uniform(size=data_numbers) 
  print(len(seq_numbers))

  alpha = cmath.pi/2
  X = list()

  for i in seq_numbers:
    val = -alpha * math.log(1 - i)
    X.append(val)

  y_sorted = np.sort(X)
  y_val = np.arange(len(y_sorted))/float(len(y_sorted) - 1)
  
  plt.title('Distribution Function of N = {}'.format(data_numbers))
  plt.ylabel('Probability - P(X <= x)')
  plt.xlabel('X (generated values)')
  plt.plot(y_sorted, y_val, color='red')
  plt.show()

#   plt.title('Frequency Distribution of X ( sample count = {} )'.format(data_numbers))
#   counts, bin_edges = np.histogram(X, bins=np.arange(min(X), max(X)+1, 0.1))
#   plt.ylabel('Frequency')
#   plt.xlabel('X (generated values)')
#   plt.plot(bin_edges[1:], counts)
#   plt.show()

  print("Sample count =", data_numbers)
  print("Mean =", np.mean(X))
  print("Variance =", np.var(X))
  print()


x = np.arange(0, 25, 0.01)
Fx = [1 - math.exp(-i/alpha) for i in x]

plt.plot(x, Fx, color='red')
plt.title('Actual Distribution Function')
plt.ylabel('F (x) ')
plt.xlabel('x')
plt.show()

print("Theoretical Mean =", alpha)
print("Theoretical Variance =", alpha*alpha)