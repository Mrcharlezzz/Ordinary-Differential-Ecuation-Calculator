import sympy as sp

class MathMethods:
    def __init__(self, x0, y0, f, h, n, s_x, s_y, t):
        self.f_lambda = sp.lambdify((sp.symbols(s_x), sp.symbols(s_y)), f)
        self.values = self.__euler_method(x0, y0, h, n)
        self.ode_evaluation = (t, self.__get_solution(t))

    def get_values(self):
        return self.values

    def evaluation(self):
        return self.ode_evaluation

    def __get_eval(self, coordinate):
        return self.f_lambda(coordinate[0], coordinate[1])

    def __euler_method(self, x0, y0, h, n):
        values = [(x0, y0)]
        step = h

        for i in range(n):
            r_coordinate = values[len(values) - 1]
            l_coordinate = values[0]

            x_prev = l_coordinate[0] - step
            y_prev = l_coordinate[1] - step * self.__get_eval(l_coordinate)

            x_next = r_coordinate[0] + step
            y_next = r_coordinate[1] + step * self.__get_eval(r_coordinate)

            values.insert(0,(x_prev, y_prev))
            values.append((x_next, y_next))

        return values

    def __get_solution(self, t):
        f = self.values
        for i in range(len(self.values) - 1):
            x1 = f[i][0]
            y1 = f[i][1]
            x2 = f[i + 1][0]
            y2 = f[i + 1][1]

            if (t >= x1) and (t < x2):
                m = (y2 - y1)/(x2 - x1)
                n = y1 - m*x1
                return m*t+n