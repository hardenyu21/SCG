import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Create an array of x values from 0 to 2π
    x = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the sine and cosine of x
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    # Create a figure and a set of subplots
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    
    # Plot the sine function
    axs[0].plot(x, y_sin, label='sin(x)')
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    axs[0].grid(True)
    
    # Plot the cosine function
    axs[1].plot(x, y_cos, label='cos(x)', color='orange')
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    axs[1].grid(True)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Return the figure and axes
    return fig, axs

# Example usage
fig, axs = task_func()
plt.show()