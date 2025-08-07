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
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        arr, fft_data, _ = task_func(original)
        self.assertTrue(np.array_equal(arr, np.array([1, 2, 3, 4])))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (4,))
    def test_case_2(self):
        original = [('a', i) for i in range(1, 101)]
        arr, fft_data, ax = task_func(original)
        self.assertTrue(np.array_equal(arr, np.array(range(1, 101))))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (100,))
        # Test that the plot is created
        self.assertIsInstance(ax, plt.Axes)
        # Test the axis limits
        self.assertEqual(ax.get_xlim(), (-200.0, 5300.0))
    def test_case_3(self):
        original = [('a', 5) for i in range(10)]
        arr, fft_data, _ = task_func(original)
        self.assertTrue(np.array_equal(arr, np.array([5]*10)))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (10,))
    def test_case_4(self):
        original = [('a', i) for i in range(10)]
        arr, fft_data, ax = task_func(original)
        self.assertTrue(np.array_equal(arr, np.array(range(10))))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (10,))
        # Test the plot data array
        self.assertEqual(len(ax.get_children()), 20)
        # Test the plot limits
        self.assertEqual(ax.get_xlim(), (3.0, 47.0))
    def test_case_5(self):
        original = []
        arr, fft_data, ax = task_func(original)
        self.assertTrue(np.array_equal(arr, np.array([])))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (0,))
        self.assertIsNone(ax)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)