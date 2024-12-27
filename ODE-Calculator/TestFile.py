import sympy as sp
import Math_Methods

x, y = sp.symbols('x y')

function = sp.sqrt(y)

f_lambda = sp.lambdify((x, y), function, 'numpy')

calculator = Math_Methods.MathMethods(1, 1, f_lambda, .01, 3)

x_vals, y_vals = calculator.get_values()

#print("y(3) = ", calculator.get_evaluation())

#print("(x) Values: ", x_vals)
#print("(y) Values: ", y_vals)