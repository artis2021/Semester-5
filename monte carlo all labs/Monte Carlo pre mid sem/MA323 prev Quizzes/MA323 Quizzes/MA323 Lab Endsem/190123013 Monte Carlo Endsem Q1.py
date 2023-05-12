# Aryan Rathee
# Roll No. 190123013


import math
import random
import matplotlib.pyplot as plt

values=[] # list to store the generated values, values[i] will keep track of the values of (i+1)th graph
for j in range(0,10):
	values.append([0]) # the value at t=0 is 0

time=[0] # this list will store the uniform time intervals on which value of W(t(i))s are computed
for i in range(0,5000):
	time.append(time[-1]+1/5000)


for j in range(0,10):
	# loop is till n/2 because in each iteration, we get 2 random variables
	for i in range(0,2500):
		# generating random variables with normal distribution from box-muller method
		u1=random.random()
		u2=random.random()

		R=math.sqrt(-2*math.log(u1))
		theta=2*math.pi*u2

		z1=R*math.cos(theta)
		z2=R*math.sin(theta)

		# value generated from the formula given in the question, once for z1 and then for z2
		w=values[j][-1]+math.sqrt(1/5000)*z1
		values[j].append(w)
		w=values[j][-1]+math.sqrt(1/5000)*z2
		values[j].append(w)

# plotting all the graphs in the same figure
for j in range(0,10):
	plt.plot(time, values[j], label=str(j+1), linewidth=0.5)

# plotting all the graphs in the same figure
plt.xlabel('Time')
plt.ylabel('W(t(i))')
plt.legend(loc='upper right')
plt.show()