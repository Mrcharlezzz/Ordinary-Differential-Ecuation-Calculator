import numpy as np
import matplotlib.pyplot as plt

def plot_ode(ode, x_interval, y_interval, x_values, y_values, x_0, y_0):
    
    # Create a grid of points in the x, y plane
    x_vals = np.linspace(x_interval[0], x_interval[1], 30)
    y_vals = np.linspace(y_interval[0], y_interval[1], 30)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Calculate the direction field
    U = 1  # Length on the x-axis
    V = ode(X, Y)  # The slope of the ODE at each point

    # Normalize the vectors to obtain uniform directions
    N = np.sqrt(U**2 + V**2)
    U, V = U / N, V / N

    # Create the figure and axis
    ax = plt.subplots(figsize=(8, 8))

    # Draw the direction field
    ax.quiver(X, Y, U, V, color="black", angles="xy", scale=85, headlength=0, headaxislength=0)

    # Plot the curve points and the point y(x_0) = y_0
    ax.plot(x_values, y_values, color="blue")
    ax.plot(x_0, y_0, 'ro', label=f"y({x_0}) = {y_0:.2f}")

    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Direction Field")

    # Add lines for the axes
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)

    # Set grid and limits
    ax.grid(False)
    ax.set_xlim(x_interval[0], x_interval[1])
    ax.set_ylim(y_interval[0], y_interval[1])

    # Show the legend and plot
    ax.legend()
    plt.show()
