import sympy
import numpy 
import math
from math import sin, cos, tan, log, sqrt,pi

def simple(A):
    resultado = eval(A, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "ln": log, "log":logs, "sqrt": sqrt, "pi": pi})
    return round(resultado,10)
    
def logs(base,argumento):
    return log(argumento)/log(base)

# #Casos pruebas
# resultado = simple("sqrt(12345**2 + 54321**2)")
# print("Resultado:", resultado)  # Resultado: 55566.4037611294

# # Caso 2: Funciones trigonométricas combinadas
# resultado_trig = simple("sin(45/57.2958) + cos(30/57.2958) + tan(60/57.2958)")
# print("Resultado trigonométrico:", resultado_trig)  # Resultado trigonométrico: 2.366...

# # Caso 3: Raíz cuadrada simple
# resultado3 = simple("sqrt(16)")
# print("Resultado 3:", resultado3)  # Resultado: 4.0

# # Caso 4: Logaritmo natural
# resultado4 = simple("log(10,10)")
# print("Resultado 4:", resultado4)  # Resultado: 1

# # Caso 5: Operaciones trigonométricas simples
# resultado5 = simple("sin(0) + cos(pi/2)")
# print("Resultado 5:", resultado5)

# resultado6 = simple("ln(10)")
# print("Resultado 6:", resultado6)

# resultado_div = simple("1/2 + 1/2")
# print("Resultado7:",resultado_div)