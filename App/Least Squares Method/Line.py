import numpy as np

def line(x0,y0):  #calculates the line of best fit for a set of points
    n = len(x0)
    x = sum(x0)
    y = sum(y0)
    xy = sum(x0*y0)
    x2 = sum(x0**2)
    
    A = np.array([[x2,x],[x,n]])   # Create matrices A and B to solve the system of linear equations
    B = np.array([xy,y])
    
    a,b = np.linalg.solve(A,B)   # Solve the system of linear equations to find the coefficients a and b

    def f(x):               # Define the line of best fit function
        return round(a,4)*x + round(b,4)

    error = 0               # Calculate the sum of squared errors
    for i in range(n):
        error += (y0[i] - f(x0[i]))**2
    
    return f,error