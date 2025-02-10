import numpy as np
import warnings

class LeastSquare:
    def __init__(self, x0, y0):
        n = len(x0)
        x = sum(x0)
        y = sum(y0)
        x2 = sum(x ** 2 for x in x0)
        x3 = sum(x ** 3 for x in x0)
        x4 = sum(x ** 4 for x in x0)
        xy = sum(x * y for x, y in zip(x0, y0))
        x2y = sum(x ** 2 * y for x, y in zip(x0, y0))

        A_line = np.array([[x2, x], [x, n]])  # Create matrices A and B to solve the system of linear equations
        B_line = np.array([xy, y])

        self.__a_l, self.__b_l = np.linalg.solve(A_line, B_line)  # Solve the system of linear equations to find the coefficients a and b

        A_par = np.array([[x4, x3, x2], [x3, x2, x], [x2, x, n]])  # Create matrices A and B to solve the system of linear equations
        B_par = np.array([x2y, xy, y])

        self.__a_p, self.__b_p, self.__c_p = np.linalg.solve(A_par, B_par)  # Solve the system of linear equations to find the coefficients a, b, and c

    def __line(self, x):  # Define the line of best fit function
        return round(self.__a_l, 4) * x + round(self.__b_l, 4)

    def __parabola(self, x):  # Define the parabola of best fit function
        return round(self.__a_p, 4) * x ** 2 + round(self.__b_p, 4) * x + round(self.__c_p, 4)

    def get_line_and_parabola(self):
        return self.__line, self.__parabola


class NumericError:
    def __init__(self, solution, derivative, ini, end):
        self.__s = solution
        self.__d = derivative
        self.__ini = ini
        self.__end = end

    def absolute_error(self, y, x):
        return abs(self.__s(x) - y)

    def relative_error(self, y, x):
        if self.__s(x) == 0:
            print("Relative Error Is Not Defined on x=", x)
            return 0
        return abs(self.absolute_error(y, x) / self.__s(x))

    def condition(self, x):
        if self.__s(x) == 0:
            print("Condition Is Not Defined on x=", x)
            return 0
        return abs((x*self.__d(x))/self.__s(x))

    def __aux_error(self, evaluation):
        x = evaluation[0]
        y = evaluation[1]
        return self.absolute_error(y, x), self.relative_error(y, x), self.condition(x)

    def range_error(self, values):
        x_vals = []
        y_vals_a = []
        y_vals_r = []
        y_vals_c = []
        max_a = (0, 0)
        max_r = (0, 0)
        max_c = (0, 0)

        for evaluation in values:
            x = evaluation[0]
            if self.__ini <= x <= self.__end:
                x_vals.append(x)
                absl, rel, cond = self.__aux_error(evaluation)
                max_a = max(max_a, (absl, x))
                max_r = max(max_r, (rel, x))
                max_c = max(max_c, (cond, x))
                y_vals_a.append(absl)
                y_vals_r.append(rel)
                y_vals_c.append(cond)
        return [x_vals, y_vals_a, y_vals_r, max_a, max_r, y_vals_c, max_c]

class MathMethods:
    def __init__(self, x0, y0, f, h, x1):
        """Class Builder"""
        self.__n = int(1e4)
        self.__f_lambda = f
        num_args = f.__code__.co_argcount
        if num_args == 2:
            self.__values = self.__euler_method(x0, y0, h)
            y1 = self.__get_solution(x1)
            if y1 is None:
                self.__ode_evaluation = (x1, None)
            else:
                self.__ode_evaluation = (x1, float(y1))
        self.numeric_error = []

    def numeric_analysis(self, solution, derivative, ini, end):
        """Numeric Analysis trigger, call this method AFTER build the class, then get results in MathMethods fields"""
        x = self.get_evaluation()[0]
        y = self.get_evaluation()[1]
        numeric_e = NumericError(solution, derivative, ini, end)
        result_return = numeric_e.range_error(self.__values)
        result_return.append((x, numeric_e.absolute_error(y, x)))
        result_return.append((x, numeric_e.relative_error(y, x)))
        result_return.append((x, numeric_e.condition(x)))
        self.numeric_error = result_return

    def numeric_get_range_absolute_error(self):
        """Call AFTER numeric_analysis(), Get x_vals, y_vals to PLOT absolute error in [l, r]"""
        return self.numeric_error[0], self.numeric_error[1]

    def numeric_get_range_relative_error(self):
        """Call AFTER numeric_analysis(), Get x_vals, y_vals to PLOT relative error in [l, r]"""
        return self.numeric_error[0], self.numeric_error[2]

    def numeric_get_range_condition(self):
        """Call AFTER numeric_analysis(), Get x_vals, y_vals to PLOT condition in [l, r]"""
        return self.numeric_error[0], self.numeric_error[5]

    def numeric_get_range_max_absolute_error(self):
        """Call AFTER numeric_analysis(), Get (x, max_absolute_error) in [l, r] to PLOT and SHOW in window"""
        to_return = (self.numeric_error[3][1], self.numeric_error[3][0])
        return  to_return

    def numeric_get_range_max_relative_error(self):
        """Call AFTER numeric_analysis(), Get (x, max_relative_error) in [l, r] to PLOT and SHOW in window"""
        to_return = (self.numeric_error[4][1], self.numeric_error[4][0])
        return to_return

    def numeric_get_range_max_condition(self):
        """Call AFTER numeric_analysis(), Get (x, max_condition) in [l, r] to PLOT and SHOW in window"""
        to_return = (self.numeric_error[6][1], self.numeric_error[6][0])
        return to_return

    def numeric_get_specific_absolute_error(self):
        """Call AFTER numeric_analysis(), Get (x, specific_absolute_error) in f(x1) to PLOT and SHOW in window"""
        return  self.numeric_error[7]

    def numeric_get_specific_relative_error(self):
        """Call AFTER numeric_analysis(), Get (x, specific_relative_error) in f(x1) to PLOT and SHOW in window"""
        return  self.numeric_error[8]

    def numeric_get_specific_condition(self):
        """Call AFTER numeric_analysis(), Get (x, specific_condition) in f(x1) to PLOT and SHOW in window"""
        return  self.numeric_error[9]

    def least_square(self):
        """Method to get least square line and parabola"""
        x_values, y_values = self.get_values()
        ls = LeastSquare(x_values, y_values)
        return ls.get_line_and_parabola()


    def get_values(self):
        """Method to get Euler's method values..."""
        x_values = []
        y_values = []
        for plot in self.__values:
            x_values.append(plot[0])
            y_values.append(plot[1])
        return x_values, y_values

    def get_evaluation(self):
        """Method to get the specified evaluation of the equation..."""
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
                if np.isnan(y_prev) or y_prev >= float('inf'):
                    isnan = (True, isnan[1])
                else:
                    values.insert(0,(x_prev, y_prev))

            if not isnan[1]:
                r_coordinate = values[len(values) - 1]
                x_next = r_coordinate[0] + h
                y_next = r_coordinate[1] + h * self.__get_lambda_eval(r_coordinate)
                if np.isnan(y_next) or y_next >= float('inf'):
                    isnan = (isnan[0], True)
                else:
                    values.append((x_next, y_next))

        return values

    def __get_solution(self, t):
        f = self.__values
        rg = (f[0][0], f[len(f) - 1][0])

        if t < rg[0] or t > rg[1]:
            return None

        if len(f) == 1:
            return f[0][1]

        for i in range(len(f) - 1):
            x1 = f[i][0]
            y1 = f[i][1]
            x2 = f[i + 1][0]
            y2 = f[i + 1][1]

            if (t >= x1) and (t < x2):
                m = (y2 - y1)/(x2 - x1)
                n = y1 - m*x1
                return m*t+n