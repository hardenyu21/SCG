import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Calculate the Fast Fourier Transform (FFT) of the signal
    transformed_signal = fft(signal)
    
    # Round the transformed signal values to the specified precision
    transformed_signal_rounded = np.round(transformed_signal, precision)
    
    # Plot the original signal
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    axes[0].plot(signal, label='Original Signal')
    axes[0].set_title('Original Signal')
    axes[0].set_xlabel('Sample Index')
    axes[0].set_ylabel('Amplitude')
    axes[0].grid(True)
    
    # Plot the transformed signal
    axes[1].plot(np.abs(transformed_signal_rounded), label='Transformed Signal')
    axes[1].set_title('Transformed Signal')
    axes[1].set_xlabel('Frequency Index')
    axes[1].set_ylabel('Magnitude')
    axes[1].grid(True)
    
    # Show the plots
    plt.tight_layout()
    plt.show()
    
    # Return the rounded transformed signal and the Axes objects
    return transformed_signal_rounded, (axes[0], axes[1])

# Example usage:
# signal = np.random.rand(100)  # Example signal
# transformed_signal, axes = task_func(signal, precision=2)