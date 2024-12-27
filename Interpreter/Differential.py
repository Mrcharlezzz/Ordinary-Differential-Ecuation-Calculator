import sympy
import numpy 
import math
import re
from math import sin, cos, tan, log, sqrt,pi


def differential(A): #This method receives a string, converts it into a mathematical expression, clears the variable and returns the cleared function
    try:
        A = A.replace('dy/dx', 'Diff')     # Replace dy/dx with Diff(remplaza dy/dx por Diff)
        A = A.replace("√", "sqrt")
        A = A.replace("^", "**")
        A = A.replace("π", "pi")
        if re.search(r'\d+e', A) or re.search(r'e\d+', A) or re.search(r'\d+pi', A) or re.search(r'pi\d+', A): 
            return None                                 #Look if there is any number before or after pi or e
        
        A = A.replace('e', str(math.e))       # Replace e with math.e(reemplaza e por math.e)
        
        izquierda, derecha = A.split('=') # Split equation into two parts(separa la ecuacion en dos partes)
        
        izq = sympy.sympify(izquierda)    # Convert left side to symbolic expression(convierte la parte izquierda en una expresion simbolica)
        der = sympy.sympify(derecha)      # Convert right side to symbolic expression(convierte la parte derecha en una expresion simbolica)
        
        ecuacion = izq - der              # Combine into one equation by subtracting right side(lo une todo en una ecuacion restando la parte izquierda)
        
        Diff = sympy.Symbol('Diff')       # Define symbolic variable Diff(define la variable Diff)
        
        coef = ecuacion.collect(Diff, evaluate=False)   # Group terms with Diff(agrupa los coeficientes de Diff)
   
        if Diff in coef:   #If there are terms with Diff, reorganize the equation(cuando Diff tiene coeficiente, suma todos los terminos que no son Diff y los divide por el coeficiente )
            resultado = -sum(v for k, v in coef.items() if k != Diff) / coef[Diff]
        
        else:  #If no terms with Diff, sum all terms(cuando Diff no tiene coeficiente, suma todos los terminos)
            resultado = sum(v for k, v in coef.items())
        
        x, y = sympy.symbols('x y')  # Define symbolic variables x and y(Define las variables simbólicas x e y)
        f_lambda = sympy.lambdify((x, y), resultado, 'numpy')
        return f_lambda
    except:  #if there is an error return none
        return None

# #Casos Pruebas
resultado1 = differential("dy/dx/6 +9*y =8*y")
print("Resultado1:", resultado1)
print(type(resultado1))


resultado2 = differential("dy/dx = 7+x")
print("Resultado2:", resultado2)

# resultado3 = differential("dy/dx +5 + 2*x = 5*y")
# print("Resultado3:", resultado3)

resultado4 = differential("dy/dx - 56*e =0")
print("Resultado4:", resultado4(1,0))
print("Resultado" ,resultado4)