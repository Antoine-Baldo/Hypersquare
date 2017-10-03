import sys
import os 
import random
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy
from PyQt4 import QtGui, QtCore

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())

class Window(QtGui.QDialog):

	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.setGeometry(630,80,800,800)
		self.setWindowTitle('Hypersquare control!!!')
		self.setWindowIcon(QtGui.QIcon('images.png'))

		self.fig = Figure() 
		self.canvas = FigureCanvas(self.fig)

		btnQ = QtGui.QPushButton('Quit', self)
		btnQ.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btnQ.move(300,170)

		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		grid.addWidget(self.canvas)

		def lhs():
			# Initialisation:	
			nV = 2
			nS = self.sl.value()
			# Grid Setup
			ax = self.fig.add_subplot(111)
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

			data1 = [float(x[k][0]) for k in range(1,nS+1)]
			data2 = [float(x[k][1]) for k in range(1,nS+1)]

			ax.clear()
			ax.plot(data1, data2, 'b.')
			if nS < 26 :
				ax.set_xticks(numpy.arange(0,1,(1/float(nS))))
				ax.set_yticks(numpy.arange(0,1,(1/float(nS))))
			ax.grid(True)
			self.canvas.draw()
			

		def function():
			lhs()

		btnR = QtGui.QPushButton("Run", self)
		btnR.clicked.connect(function)
		btnR.move(100,170)

		self.sp = QtGui.QSpinBox(self)
		self.sp.move(200,50)
		self.sp.setRange(0, 100)
		self.sp.setSingleStep(1)

		self.toolbar = NavigationToolbar(self.canvas, self)

		self.sl = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		self.sl.setMinimum(0)
		self.sl.setMaximum(100)
		self.sl.setValue(0)
		self.sl.move(200,110)
		self.sl.setTickInterval(10)
		self.sl.setTickPosition(QtGui.QSlider.TicksBelow)
		self.sl.valueChanged.connect(self.sp.setValue)
		self.sp.valueChanged.connect(self.sl.setValue)

		grid.addWidget(btnR)
		grid.addWidget(btnQ)
		grid.addWidget(self.sl)
		grid.addWidget(self.sp)
		grid.addWidget(self.toolbar)

run()