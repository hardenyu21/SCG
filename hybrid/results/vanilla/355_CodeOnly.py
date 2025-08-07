import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    # Generate the complex wave
    real_part = amplitude * np.cos(2 * np.pi * frequency * time)
    imag_part = amplitude * np.sin(2 * np.pi * frequency * time)
    complex_wave = real_part + 1j * imag_part
    
    # Apply a Hann window
    hann_window = get_window('hann', len(time))
    complex_wave *= hann_window
    
    # Plot the real and imaginary parts
    fig, ax = plt.subplots()
    ax.plot(time, complex_wave.real, label='Real Part')
    ax.plot(time, complex_wave.imag, label='Imaginary Part')
    
    # Set plot title and labels
    ax.set_title("Complex Wave with Hann Window")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()
    
    # Show grid
    ax.grid(True)
    
    # Return the complex wave and plot objects
    return complex_wave, fig, ax

# Example usage:
# amplitude = 1.0
# frequency = 5.0
# time = np.linspace(0, 1, 1000)
# complex_wave, fig, ax = task_func(amplitude, frequency, time)
# plt.show()