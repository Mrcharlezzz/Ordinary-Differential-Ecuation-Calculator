import sympy

def incognita(A):
    x = sympy.symbols('x')  # Define symbolic variable x
    if'ln' in A:            # Replace 'ln' with 'log'
        A = A.replace('ln','log')     
    if 'log' in A and ',' in A:    # Replace 'log(x,y)' with 'log(y)/log(x)'
        comma_pos = A.find(',')    # Find comma position
        x_before_comma = A.find('x') < comma_pos # Check if 'x' is before comma
        if x_before_comma:           # If true, x is the base
            arg_start = comma_pos + 1  # Mark argument start
            arg_end = A.find(')')      # Mark argument end
            arg = A[arg_start:arg_end]   # Get argument
            A = A.replace(f'log(x,{arg})', f'log({arg})/log(x)')     # Perform base change
        else:                             # If false, x is the argument
            base_start = A.find('log(') + 4  # Find base start
            base_end = comma_pos             # Find base end
            base = A[base_start:base_end]     # Get base
            A = A.replace(f'log({base},x)', f'log(x)/log({base})')   #  Perform base change
    ecuacion_simbolica = sympy.sympify(A.split('=')[0]) - sympy.sympify(A.split('=')[1])    # Convert to equation by subtracting left side
    if ecuacion_simbolica.has(sympy.sin, sympy.cos, sympy.tan): # If trigonometric use solveset
        soluciones = sympy.solveset(ecuacion_simbolica, x, domain=sympy.Interval(0, 2*sympy.pi)) # Solve trigonometric equation in interval [0, 2π]
    else: 
        soluciones = sympy.solve(ecuacion_simbolica, x) # Solve normal equation
    return soluciones