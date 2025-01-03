from abc import ABC, abstractmethod

import numpy as np
import matplotlib.pyplot as plt

class Plotter(ABC):
    @abstractmethod
    def plot(self,*args,**kwargs):
        pass
class DirectionFieldPlotter(Plotter):
    def plot(self,ode, x_interval, y_interval, x_values, y_values, x_0, y_0):

        # Create a grid of points in the x, y plane
        x_vals = np.linspace(x_interval[0], x_interval[1], 30)
        y_vals = np.linspace(y_interval[0], y_interval[1], 30)
        X, Y = np.meshgrid(x_vals, y_vals)
        # Vectorize the ODE function to handle NumPy array inputs
        def vectorized_ode(x, y):
            if np.isscalar(x) and np.isscalar(y):
                return ode(x, y)
            else:
                return np.frompyfunc(ode, 2, 1)(x, y).astype(float)

        # Calculate the direction field
        U = 1  # Length on the x-axis
        V = vectorized_ode(X, Y)  # The slope of the ODE at each point

        # Normalize the vectors to obtain uniform directions
        N = np.sqrt(U**2 + V**2)
        U, V = U / N, V / N

        # Create the figure and axis
        fig,ax = plt.subplots(figsize=(8, 8))

        # Draw the direction field
        ax.quiver(X, Y, U, V, color="black", angles="xy", scale=85, headlength=0, headaxislength=0)

        # Plot the curve points and the point y(x_0) = y_0
        ax.plot(x_values, y_values, color="blue")
        ax.plot(x_0, y_0, 'ro', label=f"y({x_0}) = {y_0:.2f}")

        # Set labels and title
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Direction Field")

        # Set grid and limits
        ax.grid(False)
        ax.set_xlim(x_interval[0], x_interval[1])
        ax.set_ylim(y_interval[0], y_interval[1])
        
        # Add lines for the axes
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)

        # Show the legend and plot
        ax.legend()
        plt.show()

class AbsoluteErrorPlotter(Plotter):
    def plot(self, x_values, error_values):

        fig,ax = plt.subplots(figsize=(8, 8))
        # Add lines for the axes
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)

        # Set labels and title
        plt.xlabel("x")
        plt.ylabel("Absolute Error")
        plt.title("Absolute Error Plot")

        ax.plot(x_values, error_values, color="red")
        plt.grid(True)
        plt.show()

class RelativeErrorPlotter(Plotter):
    def plot(self, x_values, error_values):
        
        fig,ax = plt.subplots(figsize=(8, 8))
        # Add lines for the axes
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)

        # Set labels and title
        plt.xlabel("x")
        plt.ylabel("Relative Error")
        plt.title("Relative Error Plot")

        ax.plot(x_values, error_values, color="orange")
        plt.grid(True)
        plt.show()

class ConditionPlotter(Plotter):
    def plot(self, x_values, cond_values):
        
        fig,ax = plt.subplots(figsize=(8, 8))
        # Add lines for the axes
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)

        # Set labels and title
        plt.xlabel("x")
        plt.ylabel("Condition")
        plt.title("Condition Plot")

        ax.plot(x_values, cond_values, color="green")
        plt.grid(True)
        plt.show()

