
# Programmed by Antoine BALDO

import os 
import random
from pprint import pprint

# Var number (nV dimension) setpoint
# You can change the dimension's size
nV = 2

# Sample number setpoint
# You can change the Sample number
nS = 20

# Initialisation:
k = 1
# Creation of a list dictionnary
x = {}
x[k] = []

# Loop elements (part1)
for i in range(1,(nV+1)):
	x1 = []

	for j in range(1,(nS+1)):
		a = ((float(j)-1)/nS)
		b = ((float(j))/nS)
		listesample = random.uniform(a,b)
		x1.append(listesample)

	# Select a random number nP times between each Sample and for each Var (part2)
	for k in range(1,nS+1):
		listechoice = random.choice(x1)
		x.setdefault(k, []).append(listechoice)
		x1.remove(listechoice)
pprint(x)
