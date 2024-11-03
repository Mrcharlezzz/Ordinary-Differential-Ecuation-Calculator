import sympy as sp

class MathMethods:
    def __init__(self, x0, y0, f, h, n, s_x, s_y):
        self.x0 = x0
        self.y0 = y0
        self.f = f
        self.h = h
        self.n = n
        self.x = sp.symbols(s_x)
        self.y = sp.symbols(s_y)


    def euler_method(self):
        f_lambdify = sp.lambdify((self.x, self.y), self.f)
        x_values = [self.x0]
        y_values = [self.y0]
