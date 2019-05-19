import sympy as sp
import numpy as np


class BirgeVieta:
    def __init__(self, fun, x0, es=0.05, max_it=50):
        self.function = sp.simplify(fun)
        self.x = sp.symbols('x')
        self.initialX = x0
        self.root = x0
        self.eps = es
        self.max_iteration = max_it
        self.taken_iteration = 0
        self.coefficients = sp.poly(self.function).all_coeffs()
        self.error = 100
        self.B = []  #
        self.C = []  #

    def calculate(self):
        size = len(self.coefficients)
        x = self.initialX
        while self.error > self.eps and self.taken_iteration < self.max_iteration:
            b = [self.coefficients[0]]
            c = [self.coefficients[0]]
            for i in range(1, size):
                b.append(self.coefficients[i] + x * b[i - 1])
                if i != size - 1:
                    c.append(b[i] + x * c[i - 1])
            old_x = x
            x = x - (b[size - 1] / c[size - 2])
            self.error = abs(((x - old_x) / x) * 100)
            self.B.append(b)
            self.C.append(c)
            self.taken_iteration += 1
        self.root = x

    def plot(self, canvas):
        canvas.ax.clear()
        x_axis = np.linspace(-5, 5, 100)
        y_axis = [self.function.subs(self.x, a) for a in x_axis]
        canvas.ax.plot(x_axis, y_axis)
        canvas.ax.figure.canvas.draw()
        # sp.plot(self.function, (self.x, -5, 5), show=True)

    # return the table of the details of each iteration
    def get_table(self):
        table = [self.coefficients, self.B, self.C]
        return table

    # return root of given function after solution
    def get_root(self):
        return float(self.root)

    # set maximum number of iteration
    def set_max_it(self, max_it):
        self.max_iteration = max_it

    # return maximum number of iteration
    def get_max_iteration(self):
        return self.max_iteration

    # return total number of iteration taken to implement method
    def get_taken_iteration(self):
        return self.taken_iteration

    # determine if this method is converge or diverge
    def is_converge(self):
        return self.error > 10 * self.eps

    def get_error(self):
        return self.error

# "x^4-9*x^3-2*x^2+120*x-130", -3
