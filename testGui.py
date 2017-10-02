import sys
import os 
import random
from pprint import pprint
import matplotlib.pyplot as plt
import numpy
from PyQt4 import QtGui, QtCore

def lhs(nV,nS):
	# Var number (nV dimension) setpoint
	# You can change the dimension's size
	# nV = 2

	# Sample number setpoint
	# You can change the Sample number
	# nS = 40

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
	# pprint(x)
	for k in range(1,nS+1):
		plt.scatter(float(x[k][0]),float(x[k][1]) , color="b", label="LHS")
	plt.grid()
	plt.show()

def function():
	lhs(2,20)

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(100,100,500,200)
		self.setWindowTitle('Hypersquare control!!!')
		self.setWindowIcon(QtGui.QIcon('images.png'))
		self.home()

	def home(self):
	
		btnQ = QtGui.QPushButton("Quit!", self)
		btnQ.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btnQ.move(300,170)

		btnR = QtGui.QPushButton("Run!", self)
		btnR.clicked.connect(function)
		btnR.move(100,170)

		self.sp = QtGui.QSpinBox(self)
		self.sp.move(200,50)
		self.sp.setRange(0, 100)
		self.sp.setSingleStep(1)

		self.sl = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		self.sl.setMinimum(0)
		self.sl.setMaximum(100)
		self.sl.setValue(0)
		self.sl.move(200,110)
		self.sl.setTickInterval(10)
		self.sl.setTickPosition(QtGui.QSlider.TicksBelow)
		self.sl.valueChanged.connect(self.V_change)
		self.sp.valueChanged.connect(self.sl.setValue)

		self.show()

	def V_change(self):
		nS_Value = str(self.sl.value())
		self.sp.setSpecialValueText(nS_Value)

run()