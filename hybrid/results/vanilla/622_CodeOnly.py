import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def task_func(L):
    # Flatten the list of lists
    flattened_list = list(chain.from_iterable(L))
    
    # Convert to a numpy array of integers
    data = np.array(flattened_list, dtype=int)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Plot the normal distribution overlay
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Add labels and title
    ax.set_title('Histogram with Normal Distribution Overlay')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the plot
    plt.show()
    
    return ax