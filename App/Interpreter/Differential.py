import sympy
import math
import re


def differential(A): #This method receives a string, converts it into a mathematical expression, clears the variable and returns the cleared function
    try:
        if "dy/dx" not in A:            #if the equation is not a differential equation return none
            return None
        
        A = A.replace('dy/dx', 'Diff')     # Replace dy/dx with Diff
        A = A.replace("√", "sqrt")         # Replace √ with sqrt
        A = A.replace("^", "**")           # Replace ^ with **
        
        if re.search(r'\d+e', A) or re.search(r'e\d+', A) or re.search(r'\d+pi', A) or re.search(r'pi\d+', A): 
            return None                                 #Look if there is any number before or after pi or e
        
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
        
        x, y = sympy.symbols('x y')  # Define symbolic variables x and y
        
        def f(x_val, y_val):
            return float(resultado.subs([(x, x_val), (y, y_val)]))  # Evaluate expression with numerical values
        
        return f
    
    except:  #if there is an error return none
        return None
    

    