import sympy
import numpy 
import math
from math import sin, cos, tan, log, sqrt,pi

def incognita(A):
    x = sympy.symbols('x')  # Define symbolic variable x(Define la variable simbólica x)
    if'ln' in A:            # Replace 'ln' with 'log'(Reemplaza 'ln' por 'log')
        A = A.replace('ln','log')     
    if 'log' in A and ',' in A:    # Replace 'log(x,y)' with 'log(y)/log(x)'(Reemplaza 'log(x,y)' por 'log(y)/log(x)')
        comma_pos = A.find(',')    # Find comma position(Encuentra la posición de la coma)
        x_before_comma = A.find('x') < comma_pos # Check if 'x' is before comma(Verifica si 'x' está antes de la coma)
        if x_before_comma:           # If true, x is the base(si lo esta, el la base)  
            arg_start = comma_pos + 1  # Mark argument start(marca el inicio del argumento)
            arg_end = A.find(')')      # Mark argument end(marca el final del argumento)
            arg = A[arg_start:arg_end]   # Get argument(encuentra el argumento)
            A = A.replace(f'log(x,{arg})', f'log({arg})/log(x)')     # Perform base change(realiza el cambio de base)
        else:                             # If false, x is the argument(si no lo esta es el argumento)
            base_start = A.find('log(') + 4  # Find base start(encuentra el inicio de la base)
            base_end = comma_pos             # Find base end(encuentra el final de la base)
            base = A[base_start:base_end]     # Get base(encuentra la base)
            A = A.replace(f'log({base},x)', f'log(x)/log({base})')   #  Perform base change(realiza el cambio de base)
    ecuacion_simbolica = sympy.sympify(A.split('=')[0]) - sympy.sympify(A.split('=')[1])    # Convert to equation by subtracting left side(convierte todo en una ecuacion restando la parte izquierda)
    if ecuacion_simbolica.has(sympy.sin, sympy.cos, sympy.tan): # If trigonometric use solveset(si es trigonometrica usa solveset )
        soluciones = sympy.solveset(ecuacion_simbolica, x, domain=sympy.Interval(0, 2*sympy.pi)) # Solve trigonometric equation in interval [0, 2π](resuelve la ecuacion trigonometrica en un intervalo de 0 a 2pi)
    else: 
        soluciones = sympy.solve(ecuacion_simbolica, x) # Solve normal equation(resuelve la ecuacion normal)
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