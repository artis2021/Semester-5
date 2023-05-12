# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

N = 1000
h = 0.5

# Generate Exp(1) using inverse transfrom
def generate_inverse_transformation():
    sequence_1 = []
    for i in range(N):
        u = np.random.uniform(0,1)
        sequence_1.append(-np.log(u))
    return sequence_1

print("Estimate generated using Inverse Transform method = ", np.mean(generate_inverse_transformation()))
print("Variance of estimator generated using Inverse Transform method = ", np.var(generate_inverse_transformation()))
print("")

# Generate random varible of density q(x)
def generate_Essential_cher():
    sequence_1 = []
    for x in range(N):
        a = np.random.uniform(0,1)
        sequence_1.append(np.log(a)/(h-1))
    return sequence_1

# Generate Estimator values by Importance Sampling using q(x)
def genEstimator():
    sequence_1 = generate_Essential_cher()
    return np.exp(np.multiply(-h,sequence_1))/(1-h)

print("Estimate generated using Importance Sampling method = ", np.mean(genEstimator()))
print("Variance of estimator generated using Importance Sampling method = ", np.var(genEstimator()))
print("")

var1 = np.var(genEstimator())
var2 = np.var(generate_inverse_transformation())
print("Amount of reduction in variance = ", (var2-var1)/var2 * 100)
