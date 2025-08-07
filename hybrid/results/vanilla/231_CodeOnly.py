import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes

class ValueObject:
    value = 0
    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)

def task_func(obj_list) -> Axes:
    # Extract values from the list of ValueObjects
    values = [obj.value for obj in obj_list]
    
    # Calculate mean and standard deviation
    if values:
        mean = np.mean(values)
        std = np.std(values)
    else:
        mean = 0
        std = 0
    
    # Create a histogram of the values
    fig, ax = plt.subplots()
    ax.hist(values, bins=10, density=True, alpha=0.6, color='g', label='Histogram')
    
    # Plot the custom normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2, label='Normal Distribution')
    
    # Add labels and legend
    ax.set_title('Histogram and Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the plotted Axes
    return ax

# Example usage:
# obj_list = [ValueObject(mu=5, std=2) for _ in range(100)]
# ax = task_func(obj_list)
# plt.show()