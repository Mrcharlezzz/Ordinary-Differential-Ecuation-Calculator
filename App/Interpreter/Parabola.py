import numpy as np

def parabola(x0,y0):  #calculates the parabola of best fit for a set of points
    n = len(x0)
    x = sum(x0)
    y = sum(y0)
    x2 = sum(x0**2)
    x3 = sum(x0**3)
    x4 = sum(x0**4)
    xy = sum(x0*y0)
    x2y = sum(x0**2*y0)  

    A = np.array([[x4,x3,x2],[x3,x2,x],[x2,x,n]])   # Create matrices A and B to solve the system of linear equations
    B = np.array([x2y,xy,y])

    a,b,c = np.linalg.solve(A,B)   # Solve the system of linear equations to find the coefficients a, b, and c

    def f(x):               # Define the parabola of best fit function
        return round(a,4)*x**2 + round(b,4)*x + round(c,4)

    error = 0
    for i in range(n):
        error += (y0[i] - f(x0[i]))**2  

    return f, error    

