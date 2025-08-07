import numpy as np
import matplotlib.pyplot as plt

def task_func(frequency, sample_size=10000):
    # Validate inputs
    if frequency < 0:
        raise ValueError("Frequency must be non-negative.")
    if sample_size <= 0:
        raise ValueError("Sample size must be positive.")
    
    # Generate time values
    t = np.linspace(0, 1, sample_size)
    
    # Generate sine and cosine waves
    sine_wave = np.sin(2 * np.pi * frequency * t)
    cosine_wave = np.cos(2 * np.pi * frequency * t)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(t, sine_wave, label='Sine Wave')
    ax.plot(t, cosine_wave, label='Cosine Wave')
    
    # Add labels and legend
    ax.set_title('Sine and Cosine Waves')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    
    # Return the figure and axes objects
    return fig, ax

# Example usage:
# fig, ax = task_func(5)
# plt.show()