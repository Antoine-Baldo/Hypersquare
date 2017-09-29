import sys
import os 
import random
from pprint import pprint
import matplotlib.pyplot as plt
import numpy
from PyQt4 import QtGui, QtCore

def lhs():
		# Var number (nV dimension) setpoint
	# You can change the dimension's size
	nV = 2

	# Sample number setpoint
	# You can change the Sample number
	nS = 40

	# Initialisation:
	# Grid Setup
	fig = plt.figure() 
	ax = fig.gca()
	ax.set_xticks(numpy.arange(0,1,(1/float(nS))))
	ax.set_yticks(numpy.arange(0,1,(1/float(nS))))
	# Creation of a list dictionnary
	k = 1
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
	for k in range(1,nS+1):
		plt.scatter(float(x[k][0]),float(x[k][1]) , color="b", label="LHS")
	plt.grid()
	plt.show()

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,500)
		self.setWindowTitle('Hypersquare !!!')
		self.home()

	def home(self):
		btn = QtGui.QPushButton("refresh", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().lhs)
		self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())