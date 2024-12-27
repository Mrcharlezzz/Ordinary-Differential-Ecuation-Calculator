import numpy as np
import warnings

class MathMethods:
    def __init__(self, x0, y0, f, h, x1):
        self.__n = int(1e4)
        self.__f_lambda = f
        self.__values = self.__euler_method(x0, y0, h)
        self.__ode_evaluation = (x1, float(self.__get_solution(x1)))

    # Method to get Euler's method values...
    def get_values(self):
        x_values = []
        y_values = []
        for plot in self.__values:
            x_values.append(plot[0])
            y_values.append(plot[1])
        return x_values, y_values

    # Method to get the specified evaluation of the equation...
    def get_evaluation(self):
        return self.__ode_evaluation

    def __get_lambda_eval(self, coordinate):
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings('error', category=RuntimeWarning)
                return float(self.__f_lambda(coordinate[0], coordinate[1]))
        except (ValueError, RuntimeWarning):
            return np.nan

    def __euler_method(self, x0, y0, h):
        isnan = (False, False)
        values = [(x0, y0)]
        for i in range(self.__n):
            if not isnan[0]:
                l_coordinate = values[0]
                x_prev = l_coordinate[0] - h
                y_prev = l_coordinate[1] - h * self.__get_lambda_eval(l_coordinate)
                if np.isnan(y_prev):
                    isnan = (True, isnan[1])
                else:
                    values.insert(0,(x_prev, y_prev))

            if not isnan[1]:
                r_coordinate = values[len(values) - 1]
                x_next = r_coordinate[0] + h
                y_next = r_coordinate[1] + h * self.__get_lambda_eval(r_coordinate)
                if np.isnan(y_next):
                    isnan = (isnan[0], True)
                else:
                    values.append((x_next, y_next))

        return values

    def __get_solution(self, t):
        f = self.__values
        rg = (f[0][0], f[len(f) - 1][0])

        if t < rg[0] or t > rg[1]:
            return None

        for i in range(len(f) - 1):
            x1 = f[i][0]
            y1 = f[i][1]
            x2 = f[i + 1][0]
            y2 = f[i + 1][1]

            if (t >= x1) and (t < x2):
                m = (y2 - y1)/(x2 - x1)
                n = y1 - m*x1
                return m*t+n