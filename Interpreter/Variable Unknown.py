import sympy
import numpy 
import math
from math import sin, cos, tan, log, sqrt,pi

def incognita(A):
    x = sympy.symbols('x')
    if'ln' in A:
        A = A.replace('ln','log')
    if 'log' in A and ',' in A:
        comma_pos = A.find(',')
        x_before_comma = A.find('x') < comma_pos
        if x_before_comma:
            arg_start = comma_pos + 1
            arg_end = A.find(')')
            arg = A[arg_start:arg_end]
            A = A.replace(f'log(x,{arg})', f'log({arg})/log(x)')
        else:
            base_start = A.find('log(') + 4
            base_end = comma_pos
            base = A[base_start:base_end]
            A = A.replace(f'log({base},x)', f'log(x)/log({base})')
    ecuacion_simbolica = sympy.sympify(A.split('=')[0]) - sympy.sympify(A.split('=')[1])
    if ecuacion_simbolica.has(sympy.sin, sympy.cos, sympy.tan): 
        soluciones = sympy.solveset(ecuacion_simbolica, x, domain=sympy.Interval(0, 2*sympy.pi)) 
    else: 
        soluciones = sympy.solve(ecuacion_simbolica, x)
    return soluciones

#Casos Pruebas
# resultado1 = incognita("x=8")
# print("Resultado 1:", resultado1)

# resultado2 = incognita("sin(x)+cos(x)=0")
# print("Resultado 2:", resultado2)

# resultado3 = incognita("x/23456.67=1")
# print("Resultado 3:", resultado3)

# resultado4 = incognita("ln(x)=1")
# print("Resultado 4:", resultado4)

# resultado5 = incognita("sqrt(x)=9")
# print("Resultado 5:", resultado5)

# resultado6 = incognita("x**2=4")
# print("Resultado 6:", resultado6)

# resultado7 = incognita("-x=-1")
# print("Resultado 7:", resultado7)

# resultado8 = incognita("x+y=1")
# print("Resultado 8:", resultado8)

# resultado9 = incognita("log(x,4)=2")
# print("Resultado 9:", resultado9)

# resultado10 = incognita("log(2,x)=3")
# print("Resultado 10:", resultado10)