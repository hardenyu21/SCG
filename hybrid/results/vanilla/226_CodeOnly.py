import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    def exp_generator():
        x = range_start
        while x <= range_end:
            yield (x, math.exp(x))
            x += step

    # Create the generator object
    gen = exp_generator()

    # Extract x and e^x values for plotting
    x_values = []
    exp_values = []
    for x, exp_x in gen:
        x_values.append(x)
        exp_values.append(exp_x)

    # Plot the exponential function
    fig, ax = plt.subplots()
    ax.plot(x_values, exp_values, label='e^x')
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    ax.legend()

    # Show the plot
    plt.show()

    # Return the generator object and the Axes object
    return exp_generator(), ax

# Example usage
gen, ax = task_func()