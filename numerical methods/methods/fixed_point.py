import sympy as sp
import numpy as np


class FixedPoint:
    def __init__(self, fun, x0, es=0.05, iter_max=50):
        self.x = sp.symbols('x')
        self.function = sp.simplify(fun)
        self.g = self.function + self.x
        self.initialX = x0
        self.xr = x0
        self.xr_old = x0
        self.eps = es
        self.max_iteration = iter_max
        self.taken_iteration = 0
        self.table = []

    # calculate all requirements of the method
    def calculate(self):
        print("G(x) : ", self.g)
        self.xr = self.g.subs(self.x, self.xr_old)

        error = self.get_error()

        iteration = 1
        if self.is_converge():
            while error > self.eps and iteration < self.max_iteration:
                d = {
                    "iter": iteration,
                    "X(i)": self.xr_old,
                    "X(i+1)": self.xr,
                    "error": error
                }
                self.table.append(d)
                self.xr_old = self.xr
                self.xr = self.g.subs(self.x, self.xr_old)
                error = self.get_error()

                iteration += 1
            d = {
                "iter": iteration,
                "X(i)": self.xr_old,
                "X(i+1)": self.xr,
                "error": error
            }
            self.taken_iteration = iteration
            self.table.append(d)
        else:
            print("this function will converge using fixed point iteration")

    # return error of specific  iteration
    def get_error(self):
        if self.xr != 0:
            return abs(((self.xr - self.xr_old) / self.xr) * 100)
        else:
            return 100

    # plot all curves related to all iteration in single figure
    def plot(self, canvas):
        canvas.ax.clear()
        x_axis = np.linspace(-5, 5, 100)
        y_axis = [self.function.subs(self.x, a) for a in x_axis]
        canvas.ax.plot(x_axis, y_axis)
        y1_axis = [self.g.subs(self.x, a) for a in x_axis]
        canvas.ax.plot(x_axis, y1_axis)
        y1_axis = [self.x.subs(self.x, a) for a in x_axis]
        canvas.ax.plot(x_axis, y1_axis)
        canvas.ax.figure.canvas.draw()

        # plot(self.g, self.x, (self.x, -5, 5), show=True)

    # determine if this method is converge or diverge
    def is_converge(self):
        return abs(sp.diff(self.g, self.x).subs(self.x, self.initialX)) < 1

    # return the table of the details of each iteration
    def get_table(self):
        return self.table

    # return maximum number of iteration
    def get_max_iteration(self):
        return self.max_iteration

    # return total number of iteration taken to implement method
    def get_taken_iteration(self):
        return self.taken_iteration

    # return root of given function after solution
    def get_root(self):
        return self.xr

    # set maximum number of iteration
    def set_max_it(self, max_it):
        self.max_iteration = max_it

