from scipy import fftpack
from matplotlib import pyplot as plt
import numpy as np

def task_func(arr):
    # Sum each row in the 2D array
    row_sums = np.sum(arr, axis=1)
    
    # Perform FFT on the row sums
    fft_coeffs = fftpack.fft(row_sums)
    
    # Calculate the absolute values of the FFT coefficients
    abs_fft_coeffs = np.abs(fft_coeffs)
    
    # Plot the absolute values of the FFT coefficients
    fig, ax = plt.subplots()
    ax.plot(abs_fft_coeffs)
    ax.set_title('Absolute Values of FFT Coefficients')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Magnitude')
    
    # Show the plot
    plt.show()
    
    return ax