import math
import statistics
import numpy as np

def task_func(input_list):
    # Sort the input list in ascending order based on the degree value of its elements
    sorted_list = sorted(input_list)
    
    # Calculate mean, median, and mode of the sorted list
    mean_sorted = round(statistics.mean(sorted_list))
    median_sorted = round(statistics.median(sorted_list))
    
    # Calculate mode, handling the case where there might be no unique mode
    try:
        mode_sorted = round(statistics.mode(sorted_list))
    except statistics.StatisticsError:
        mode_sorted = None  # or handle it as needed
    
    # Calculate the Fast Fourier Transform (FFT) of the sorted list
    fft_values = np.fft.fft(sorted_list)
    
    # Calculate the magnitude of the FFT values
    fft_magnitudes = np.abs(fft_values)
    
    # Calculate mean, median, and mode of the FFT magnitudes
    mean_fft = round(statistics.mean(fft_magnitudes))
    median_fft = round(statistics.median(fft_magnitudes))
    
    # Calculate mode, handling the case where there might be no unique mode
    try:
        mode_fft = round(statistics.mode(fft_magnitudes))
    except statistics.StatisticsError:
        mode_fft = None  # or handle it as needed
    
    # Return the results as a tuple
    return (mean_sorted, median_sorted, mode_sorted, mean_fft, median_fft, mode_fft)

# Example usage:
# input_list = [30, 45, 60, 90, 120]
# result = task_func(input_list)
# print(result)