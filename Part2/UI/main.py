# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from methods.parser import parsing
from methods.gauss_jordan import gaussJordan
from methods.gauss_sediel import gaussSediel
from methods.gauss import gauss
from methods.LUDecomposition import LUDecomposition
import numpy as np
import random

class MatplotlibWidget(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("qt_designer.ui", self)

        self.setWindowTitle("System of linear equations")

        self.solveButton.clicked.connect(self.solve)

        self.fileButton.clicked.connect(self.addFile)

        self.addButton.clicked.connect(self.addText)

        self.method = self.comboBox.currentText()
        self.comboBox.currentIndexChanged.connect(self.showPlot)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.MplWidget.move(2000, 20)
        self.widget.move(2000, 400)

        self.result=[]
        self.coeff=[]
        self.constants=[]
        self.filePath = ""
        self.equNum = 0
        self.equations = []
        self.maxItrations = 50
        self.epsilon = 0.00001
        self.solver = None

    def solve(self):
       # fs = 500
       # f = random.randint(1, 100)
       # ts = 1 / fs
       # length_of_signal = 100
       # t = np.linspace(0, 1, length_of_signal)

        #cosinus_signal = np.cos(2 * np.pi * f * t)
        #sinus_signal = np.sin(2 * np.pi * f * t)

       # self.MplWidget.canvas.axes.clear()
       # self.MplWidget.canvas.axes.plot(t, cosinus_signal)
       # self.MplWidget.canvas.axes.plot(t, sinus_signal)
       # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
       # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
       # self.MplWidget.canvas.draw()

       pars = parsing(self.equations,self.equNum)
       pars.solve()
       self.coeff= pars.getCoff()
       self.constants=pars.getConstants()
       print(self.coeff)
       print(self.constants)
       self.method = self.comboBox.currentText()
       if self.method == "Gaussian-elimination" :
            self.solver = gauss(self.coeff,self.constants,self.equNum)
       if self.method == "Gauss-Seidel":
            self.solver = gaussSediel(self.coeff,self.constants,self.result,self.maxItrations,self.epsilon,self.equ)
       if self.method == "Gaussian-Jordan":
            self.solver = gaussJordan(self.coeff,self.constants,self.equNum)
       if  self.method == "LU decomposition":
            self.solver = LUDecomposition(self.coeff,self.constants,self.equNum)

       self.result = self.solver.solve()








    def addFile(self):
        fileName, _ = QFileDialog.getOpenFileName(None,"Select File","","Text Files (*.txt)")
        if fileName:
            self.filePath = f"{fileName}"
            self.lineEdit_2.setText(self.filePath)

    def addText(self):
        value = self.lineEdit.text()
        if value:
            self.lineEdit.clear()
            self.listWidget.addItem(value)
            self.equNum += 1
            self.equations.append(value)

    def showPlot(self):
        self.method = self.comboBox.currentText()
        if self.method == "Gauss-Seidel" or self.method == "All Methods":
            self.MplWidget.move(400, 20)
            self.widget.move(30, 470)
        else:
            self.MplWidget.move(2000, 20)
            self.widget.move(2000, 400)

    a = True

    def update_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        self.MplWidget.canvas.axes.plot(t, sinus_signal)
        self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()
app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
