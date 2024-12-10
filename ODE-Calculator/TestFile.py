import sympy as sp
import Math_Methods

x, y = sp.symbols('x y')

function = x + y

f_lambda = sp.lambdify((x, y), function, 'numpy')

calculator = Math_Methods.MathMethods(0, 0, f_lambda, .01, 1)

x_vals, y_vals = calculator.get_values()

print("y(1) = ", calculator.get_evaluation())

print("(x) Values: ", x_vals, "\n(y) Values: ", y_vals)