import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Check if the original list is empty
    if original_array.size == 0:
        return original_array, np.array([]), None
    
    # Calculate the Fast Fourier Transform (FFT)
    fft_data = fft(original_array)
    
    # Calculate the magnitude of the FFT data
    fft_magnitude = np.abs(fft_data)
    
    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(fft_magnitude, bins='auto', alpha=0.7, color='blue')
    ax.set_title('Histogram of FFT Magnitude')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    
    # Return the original array, FFT data, and the axes object
    return original_array, fft_data, ax