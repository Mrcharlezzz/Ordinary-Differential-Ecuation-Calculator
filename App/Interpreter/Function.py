import sympy
import numpy 
import math
import re
from math import sin, cos, tan, log, sqrt,pi


def function(A): #This method receives a string, converts it into a mathematical expression, clears the variable and returns the cleared function and derived function
    try:
        A = A.replace('y', 'Diff')     # Replace y with Diff
        
        if "dy/dx" in A :   #check if it is an ODE
          return None
        
        if re.search(r'\d+e', A) or re.search(r'e\d+', A) or re.search(r'\d+pi', A) or re.search(r'pi\d+', A): 
            return None                                 #Look if there is any number before or after pi or e
        
        A = A.replace("√", "sqrt")
        A = A.replace("^", "**")
        A = A.replace("π", "pi")
        A = A.replace('e', str(math.e))       # Replace e with math.e
        
        izquierda, derecha = A.split('=') # Split equation into two parts
        
        izq = sympy.sympify(izquierda)    # Convert left side to symbolic expression
        der = sympy.sympify(derecha)      # Convert right side to symbolic expression
        
        ecuacion = izq - der              # Combine into one equation by subtracting right side
        
        Diff = sympy.Symbol('Diff')       # Define symbolic variable Diff
        
        coef = ecuacion.collect(Diff, evaluate=False)   # Group terms with Diff
   
        if Diff in coef:   #If there are terms with Diff, reorganize the equation
            resultado = -sum(v for k, v in coef.items() if k != Diff) / coef[Diff]
        
        else:  #If no terms with Diff, sum all terms
            resultado = sum(v for k, v in coef.items())
        
        x = sympy.symbols('x')  # Define symbolic variables x 
        
        f = sympy.lambdify((x), resultado, 'numpy')
        
        derivative = sympy.diff(resultado,x)    # Derive the function

        f_derivative = sympy.lambdify((x), derivative, 'numpy')
        
        return f,f_derivative     # Return de function and the derived function
    
    except:  #if there is an error return none
        return None