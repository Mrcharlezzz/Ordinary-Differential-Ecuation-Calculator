from math import sin, cos, tan, log, sqrt,pi

def simple(A):
    resultado = eval(A, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "ln": log, "log":logs, "sqrt": sqrt, "pi": pi}) # eval() evaluates the mathematical expression
    return round(resultado,10)   # round the result to 10 decimal places
    
def logs(base,argumento):              # method to achieve the base change, go from ln to log
    return log(argumento)/log(base)