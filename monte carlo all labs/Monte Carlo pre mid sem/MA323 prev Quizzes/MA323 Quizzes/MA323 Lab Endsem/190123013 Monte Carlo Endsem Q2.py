# Aryan Rathee
# Roll No. 190123013


import random
import math
import statistics

def simple_monte_carlo(n):
	values=[]
	for i in range(0,n//2):
		# generating random variables with normal distribution from box-muller method
		u1=random.random()
		u2=random.random()

		R=math.sqrt(-2*math.log(u1))
		theta=2*math.pi*u2

		z1=R*math.cos(theta)
		z2=R*math.sin(theta)

		if z1>4:
			values.append(1)
		else:
			values.append(0)
		if z2>4:
			values.append(1)
		else:
			values.append(0)

	# calculating mean of the obtained values
	mean=statistics.mean(values)
	print("Probability = "+str(mean))

	s=0
	# calculating the calue of s which is used in our approximation for variance
	for i in values:
		s+=(i-mean)*(i-mean)

	s/=n*n
	print("Variance = "+str(s))
	# calculating the left and right end of the confidence interval by using the formula which is obtained by CLT(Central Limit Theorem)
	left=mean-2.58*math.sqrt(s)
	right=mean+2.58*math.sqrt(s)

	print("99% Confidence Interval = ("+str(left)+","+str(right)+")")
	print('\n')

def importance_sampling(n):
	values=[]
	for i in range(0,n):
		# generating randome variable with uniform distribution in (0,1)
		u=random.random()
		x=4-math.log(u)
		y=math.exp(-x*x/2+x-4)/math.sqrt(2*math.pi)
		values.append(y)

	# calculating mean of the obtained values
	mean=statistics.mean(values)
	print("Probability = "+str(mean))

	s=0
	# calculating the calue of s which is used in our approximation for variance
	for i in values:
		s+=(i-mean)*(i-mean)

	s/=n*n
	print("Variance = "+str(s))
	# calculating the left and right end of the confidence interval by using the formula which is obtained by CLT(Central Limit Theorem)
	left=mean-2.58*math.sqrt(s)
	right=mean+2.58*math.sqrt(s)

	print("99% Confidence Interval = ("+str(left)+","+str(right)+")")
	print('\n')

n=10000
simple_monte_carlo(n)
importance_sampling(n)
