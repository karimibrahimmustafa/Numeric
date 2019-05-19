from PyQt5 import QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np
import math


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        # t = np.arange(0.0, 5.0, 0.01)
        # s = []
        # for i in range(t.size):
        #   s.append(math.sin(2 * math.pi * t[i]))
        # self.ax.plot([2, 3], [4, 6])
        # self.ax.plot([1, 4], [5, 7])
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MplGraph(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.n = NavigationToolbar(self.canvas, self)
        self.vbl.addWidget(self.n)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def update_canvas(self, method):
        method.plot(self.canvas)
