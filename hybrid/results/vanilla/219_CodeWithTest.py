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
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        input_data = [30, 45, 60, 90, 180]
        result = task_func(input_data)
        self.assertEqual(result, (81, 60, 30, 10712, 8460, 8460))
        
    def test_case_2(self):
        input_data = [0, 90, 180, 270, 360]
        result = task_func(input_data)
        self.assertEqual(result, (180, 180, 0, 24508, 21932, 21932))
        
    def test_case_3(self):
        input_data = [10, 20, 30, 40, 50]
        result = task_func(input_data)
        self.assertEqual(result, (30, 30, 10, 3296, 2437, 2437))
        
    def test_case_4(self):
        input_data = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
        result = task_func(input_data)
        self.assertEqual(result[:5], (82.5, 82.5, 15, 11366, 6311))
        
    def test_case_5(self):
        input_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        result = task_func(input_data)
        self.assertEqual(result, (32.5, 32.5, 5, 4718, 2431, 6641))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)