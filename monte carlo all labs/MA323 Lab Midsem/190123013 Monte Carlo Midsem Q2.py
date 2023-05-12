
import numpy as np
import math
import random
import statistics

def box_muller(n):
	# lists to store the generated values
	x=[]
	y=[]
	for i in range(0,n):
		# generating 2 uniform random variables and then using them
		# to generate random variables on random distributio as specified in box-muller method
		u1=random.random()
		u2=random.random()

		R=math.sqrt(-2*math.log(u1))
		theta=2*math.pi*u2

		z1=R*math.cos(theta)
		z2=R*math.sin(theta)

		x.append(z1)
		y.append(2*z1+1+2*z2) # mean is 2*x+1 and sqrt(variance)=2 

	# mean and variance of the random variables generated
	mean_x=statistics.mean(x)
	variance_x=statistics.variance(x)
	mean_y=statistics.mean(y)
	variance_y=statistics.variance(y)

	# generating covariance matrix.
	cov_mat = np.cov(x, y)

	corr_coeff=cov_mat[0][1]/math.sqrt(cov_mat[0][0]*cov_mat[1][1])
	
	print('Mean X = '+str(mean_x))
	print('Variance X = '+str(variance_x))
	print('\n')
	print('Mean Y = '+str(mean_y))
	print('Variance Y = '+str(variance_y))
	print('\n')
	print('Correlation Coefficient = '+str(corr_coeff))


box_muller(1000)