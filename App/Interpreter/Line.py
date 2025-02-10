import numpy as np
import logging

def line(x0,y0):  #calculates the line of best fit for a set of points
    n = len(x0)
    x = sum(x0)
    y = sum(y0)
    xy = sum(x0*y0)
    x2 = sum(x0**2)
    print(n,x,y,xy,x2)
    
    A = np.array([[x2,x],[x,n]])   # Create matrices A and B to solve the system of linear equations
    B = np.array([xy,y])
    
    a,b = np.linalg.solve(A,B)   # Solve the system of linear equations to find the coefficients a and b
    print(a,b)

    def f(x):               # Define the line of best fit function
        return round(a,6)*x + round(b,6)

    error = 0               # Calculate the sum of squared errors
    for i in range(n):
        error += (y0[i] - f(x0[i]))**2
    
    return f,error


