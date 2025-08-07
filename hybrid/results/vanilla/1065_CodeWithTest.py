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
import unittest
import numpy as np
from scipy import fftpack
class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""
    def test_plot_title(self):
        """Test that the plot title is correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Absolute values of FFT coefficients")
    def test_plot_data(self):
        """Test that the plot data is correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        row_sums = arr.sum(axis=1)
        fft_coefficients = fftpack.fft(row_sums)
        expected_y_data = np.abs(fft_coefficients)
        np.testing.assert_array_equal(y_data, expected_y_data)
    def test_with_zeros(self):
        """Test that the plot data is correct when the array is all zeros."""
        arr = np.zeros((5, 3))
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        expected_y_data = np.zeros(5)
        np.testing.assert_array_equal(y_data, expected_y_data)
    def test_with_ones(self):
        """Test that the plot data is correct when the array is all ones."""
        arr = np.ones((5, 3))
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        expected_y_data = [15.0, 0.0, 0.0, 0.0, 0.0]
        np.testing.assert_array_almost_equal(y_data, expected_y_data)
    def test_with_large_numbers(self):
        """Test that the plot data is correct when the array has large numbers."""
        arr = np.array([[i * 100 + j * 1000 for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        row_sums = arr.sum(axis=1)
        fft_coefficients = fftpack.fft(row_sums)
        expected_y_data = np.abs(fft_coefficients)
        np.testing.assert_array_equal(y_data, expected_y_data)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)