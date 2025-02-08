import sympy
import numpy 
import math
import re
from math import sin, cos, tan, log, sqrt,pi


def function(A): #This method receives a string, converts it into a mathematical expression, clears the variable and returns the cleared function and derived function
    try:
        if "y" not in A:            #if the equation is not a f(x) return none
            return None
        
        A = A.replace('y', 'func')     # Replace y with func
        
        if "dy/dx" in A :   #check if it is an ODE
          return None
        
        if re.search(r'\d+e', A) or re.search(r'e\d+', A) or re.search(r'\d+pi', A) or re.search(r'pi\d+', A): 
            return None                                 #Look if there is any number before or after pi or e
        
        A = A.replace("√", "sqrt")            # Replace √ with sqrt
        A = A.replace("^", "**")              # Replace ^ with **
        A = A.replace('e', str(math.e))       # Replace e with math.e
        
        izquierda, derecha = A.split('=') # Split equation into two parts
        
        izq = sympy.sympify(izquierda)    # Convert left side to symbolic expression
        der = sympy.sympify(derecha)      # Convert right side to symbolic expression
        
        ecuacion = izq - der              # Combine into one equation by subtracting right side
        
        func = sympy.Symbol('func')       # Define symbolic variable func
        
        coef = ecuacion.collect(func, evaluate=False)   # Group terms with func
   
        for term in coef:           #check if the ode is of a degree greater than 1
            if isinstance(term, sympy.Pow) and term.args[0] == func and term.args[1] != 1:
                return None
            
        resultado = -sum(v for k, v in coef.items() if k != func) / coef[func]  #adds the values ​​that do not have func and divides it by those that have func
        
        x = sympy.symbols('x')   # Define symbolic variables x
           
        def f(x_val):
            return float(resultado.subs(x, x_val))    # Evaluate expression with numerical values(sustituye x por los valores de x_val)
        
        derivative = sympy.diff(resultado,x)    # Derive the function(deriva la funcion)

        def f_derivative(x_val):      # Evaluate derived expression with numerical values(sustituye x por los valores de x_val)
            return float(derivative.subs(x,x_val))
        
        return f,f_derivative     # Return de function and the derived function(devulve la funcion y su derivada)
    
    except:  #if there is an error return none
        return None
    
