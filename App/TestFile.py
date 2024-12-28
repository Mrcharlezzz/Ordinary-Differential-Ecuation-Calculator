import math
import sympy as sp
from App import Math_Methods

x, y = sp.symbols('x y')

function = -(sp.sqrt(x))/sp.tan(sp.log(2, y))

f_lambda = sp.lambdify((x, y), function, 'numpy')

calculator = Math_Methods.MathMethods(0, 1, f_lambda, .01, 0)

x_vals, y_vals = calculator.get_values()

print("y(0) = ", calculator.get_evaluation())

#print("(x) Values: ", x_vals)
#print("(y) Values: ", y_vals)