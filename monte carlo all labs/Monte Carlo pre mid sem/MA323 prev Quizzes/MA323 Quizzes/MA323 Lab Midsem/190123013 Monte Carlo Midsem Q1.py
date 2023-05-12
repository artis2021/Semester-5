# Aryan Rathee
# Roll No. 190123013


import matplotlib.pyplot as plt
import numpy as np
import math
import random
import statistics

def plot_graph(values,mean,n):

	plt.hist(values, 25, color='g', rwidth=0.9, label='Frequency')

	plt.xlabel('Amount of Rain')
	plt.ylabel('Frequency')
	# giving title to graph
	plt.title('Freq vs Amt of Rain N = '+str(n))
	# it shows the labels corresponding to different plots
	plt.legend()
	# show the graph
	plt.show()

	mean=statistics.mean(values)
	variance=statistics.variance(values)

	# Printing empirical data for the plots.
	print('For n = '+str(n))
	print('Mean (Empirical Sample) = '+str(mean))

def generate_sequence(mean,n):
	values=[]
	for i in range(0,n):
		u=random.random()
		u2=random.random();
		if u2<=0.2: values.append(-mean*math.log(u)) # if u2<=0.2 then rain occurred otherwise no rain occurred
		else: values.append(0)

	plot_graph(values,mean,n)

# mean=1/2 and n=1000 
generate_sequence(1/2,1000)
