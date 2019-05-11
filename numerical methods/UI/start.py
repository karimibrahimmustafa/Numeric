from PyQt5 import QtWidgets
from view import Ui_MainWindow
import methods.fixed_point as FP
import methods.birge_vieta as BV
import methods.Secant as SC
from methods.Bisection import Bisection
import sys


# main window of application
class MainApp(QtWidgets.QMainWindow):
    # constructor
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.method = None
        self.methodNum = 0
        self.mode = False
        self.ui.setupUi(self)
        self.setWindowTitle("Root Finder")
        self.ui.modeCombo.activated.connect(self.mode_changed)
        self.ui.methodCombo.activated.connect(self.method_changed)
        self.ui.solveBtn.clicked.connect(self.solve_btn_action)
        self.ui.prevBtn.clicked.connect(self.prev_btn_action)
        self.ui.nextBtn.clicked.connect(self.next_btn_action)

    # handle the event of selection specific mode of solution(single mode , Direct Solution)
    def mode_changed(self):
        self.mode = bool(self.ui.modeCombo.currentIndex())
        # print(self.mode)
        if self.mode:
            self.ui.nextBtn.setEnabled(True)
            self.ui.prevBtn.setEnabled(True)
        else:
            self.ui.nextBtn.setEnabled(False)
            self.ui.prevBtn.setEnabled(False)

    # handle the event of selection specific method
    def method_changed(self):
        self.methodNum = self.ui.methodCombo.currentIndex()
        # print(self.methodNum)
        if self.methodNum == 0:
            self.ui.solveBtn.setEnabled(False)
        elif self.methodNum == 3 or self.methodNum == 4 or self.methodNum == 6:
            self.ui.X1lineEdit.setEnabled(False)
            self.ui.labelX1.setText("  ")
            self.ui.solveBtn.setEnabled(True)
        else:
            self.ui.X1lineEdit.setEnabled(True)
            self.ui.labelX1.setText("X(1)")
            self.ui.solveBtn.setEnabled(True)

    # handle the event of solve button
    def solve_btn_action(self):
        function = self.ui.functionLineEdit.text()
        if function == "":
            return
        # take value of initial point if exist
        print("function : ", function)
        try:
            x0 = float(self.ui.X0lineEdit.text())
            # print(x0)
        except:
            x0 = 0

        if x0 == 0:
            return
        print("x0 : ", x0)
        # take value of second point if exict
        try:
            x1 = float(self.ui.X1lineEdit.text())
            # print(x1)
        except:
            x1 = 0
        if (self.methodNum == 1 or self.methodNum == 2 or self.methodNum == 5) and x1 == 0:
            print(self.methodNum)
            return
        print("x1 : ", x1)
        # take value of eps
        try:
            eps = float(self.ui.EpslineEdit.text())
        except:
            eps = 0.05
        # take value of max iteration
        try:
            max_iter = float(self.ui.iterlineEdit.text())
        except:
            max_iter = 50

        print("eps : ", eps)
        if self.methodNum == 1:
            self.method = Bisection(function, x0, x1, eps, max_iter)
            print("bisection")
        elif self.methodNum == 2:
            print(self.methodNum)
        elif self.methodNum == 3:
            self.method = FP.FixedPoint(function, x0, eps, max_iter)
        elif self.methodNum == 4:
            print(self.methodNum)
        elif self.methodNum == 5:
            self.method = SC.Secant(function, x0, x1, eps, max_iter)
            print("Secant")
        elif self.methodNum == 6:
            print("birge vieta")
            self.method = BV.BirgeVieta(function, x0, eps, max_iter)

        self.method.calculate()
        print("calculated")
        if self.mode:
            self.single_mode()
        else:
            self.direct_solution_mode()

    # actions performed in case of direct solution display
    def direct_solution_mode(self):
        print("before plotted")
        self.method.plot(self.ui.mplGraph.canvas)
        print("plotted")
        text = "\t\tsolution\n\n" + " estimate Root = " + str(self.method.get_root()) + "\n\n" + " Relative Error = "
        text += str(self.method.get_error()) + "\n\n" + " # Iterations = " + str(
            self.method.get_taken_iteration()) + "\n\n"
        self.ui.solutionText.setText(text)

    # actions performed in case of direct solution display
    def single_mode(self):
        return

    # handle the event of prev button
    def prev_btn_action(self):
        return

    # handle the event of next button
    def next_btn_action(self):
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainApp()
    application.show()
    sys.exit(app.exec())
