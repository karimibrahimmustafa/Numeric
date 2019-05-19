import sympy as sp
import numpy as np


class Secant:
    # solving using secant method
    def __init__(self, fun, x0, x1, e=0.05, max_it=300):
        self.currentX = x1
        self.x = sp.symbols('x')
        self.prevX = x0
        self.function = sp.sympify(fun)
        self.max_iteration = int(max_it)
        self.eps = float(e)
        self.taken_iteration = 0
        self.table = []
        self.points = []  # to represent currentx and prevx in each iteration

    # calculate all requerments of the method
    def calculate(self):
        error = self.get_error()
        iteration = 0
        while abs(error) > self.eps and iteration < self.max_iteration:
            d = {
                "iter": iteration,
                "X(i)": self.prevX,
                "X(i+1)": self.currentX,
                "error": error
            }
            self.table.append(d)
            self.points.append([self.currentX, self.prevX])
            next_x = self.currentX - ((self.function.subs(self.x, self.currentX) * (self.prevX - self.currentX))
                                      / (self.function.subs(self.x, self.prevX) - self.function.subs(self.x,
                                                                                                     self.currentX)))
            print("next x :", next_x)
            self.prevX = self.currentX
            self.currentX = next_x
            error = self.get_error()
            print(error)
            iteration += 1
        self.taken_iteration = iteration

    # plot all curves related to all iteration in single figure
    def plot(self, canvas):
        canvas.ax.clear()
        x_axis = np.linspace(-5, 5, 100)
        y_axis = [self.function.subs(self.x, a) for a in x_axis]
        canvas.ax.plot(x_axis, y_axis)

        i = 0
        while i < len(self.points):
            y = [self.function.subs(self.x, self.points[i][0]), self.function.subs(self.x, self.points[i][1])]
            canvas.ax.plot(self.points[i], y)
            print("kadasjfi")
            print("x0: ", self.points[i][0], "  x1 :", self.points[i][1])
            i += 1
        canvas.ax.figure.canvas.draw()

    # return error of specific  iteration
    def get_error(self):
        return float(((self.currentX - self.prevX) / self.currentX) * 100)

    # set maximum number of iteration
    def set_max_it(self, max_it):
        self.max_iteration = max_it

    # return root of given function after solution
    def get_root(self):
        return self.currentX

    # return maximum number of iteration
    def get_max_iteration(self):
        return self.max_iteration

    # return total number of iteration taken to implement method
    def get_taken_iteration(self):
        return self.taken_iteration

    # return the table of the details of each iteration
    def get_table(self):
        self.table

    def is_converge(self):
        return self.get_error() > self.eps * 10


if __name__ == "__main__":
    s = Secant("x^2-2", 0.5, 1)
    s.calculate()
