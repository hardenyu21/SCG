import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(x):
    # Check if x is a numpy.ndarray
    if not isinstance(x, np.ndarray):
        raise TypeError("Input `x` must be a numpy.ndarray.")
    
    # Generate the real part of the complex distribution
    real_part = norm.pdf(x, loc=0, scale=1)
    
    # Generate the imaginary part of the complex distribution
    imaginary_part = norm.pdf(x, loc=2, scale=2)
    
    # Create the complex distribution
    complex_distribution = real_part + 1j * imaginary_part
    
    # Plot the real and imaginary parts
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, real_part, label='Real Part')
    plt.title('Real Part of the Complex Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(x, imaginary_part, label='Imaginary Part', color='orange')
    plt.title('Imaginary Part of the Complex Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    return complex_distribution

# Example usage:
x = np.linspace(-5, 10, 1000)
complex_dist = task_func(x)