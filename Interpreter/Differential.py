import sympy
import numpy 
import math
from math import sin, cos, tan, log, sqrt,pi

def diferencial(A):
    A = A.replace('dy/dx', 'Diff')
    A = A.replace("y'", 'Diff')
    izquierda, derecha = A.split('=')
    izq = sympy.sympify(izquierda)
    der = sympy.sympify(derecha)
    ecuacion = izq - der
    Diff = sympy.Symbol('Diff')
    coef = ecuacion.collect(Diff, evaluate=False)
    if Diff in coef:
        resultado = -sum(v for k, v in coef.items() if k != Diff) / coef[Diff]
    else:
        resultado = sum(v for k, v in coef.items())
    x, y = sympy.symbols('x y')
    def f(x_val, y_val):
        return float(resultado.subs([(x, x_val), (y, y_val)]))
    return f

# #Casos Pruebas
# resultado1 = diferencial("dy/dx/6 +9*y=x-8*y")
# print("Resultado1:", resultado1)
# print(type(resultado1))

# resultado2 = diferencial("y'= 7+x")
# print("Resultado2:", resultado2)

# resultado3 = diferencial("y' +5 + 2*x = 5*y")
# print("Resultado3:", resultado3)

# resultado4 = diferencial("dy/dx - log(x,2)=9")
# print("Resultado4:", resultado4)
# print(type(resultado4))