import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def task_func(size=SIZE, frequency=1):
    # Generate random phase shift
    phase_shift = random.uniform(0, 2 * PI)
    
    # Generate x values
    x_values = np.linspace(0, RANGE, size)
    
    # Generate random sinusoidal values
    y_values = np.sin(2 * PI * frequency * x_values / RANGE + phase_shift)
    
    # Plot the sinusoidal wave
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_title('Random Sinusoidal Wave')
    ax.set_xlabel('X')
    ax.set_ylabel('Amplitude')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage
task_func()