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
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a constant signal
        signal = np.array([1.0, 1.0, 1.0, 1.0])
        transformed_signal, (ax1, ax2) = task_func(signal)
        
        # Assert transformed signal
        self.assertTrue(all(transformed_signal == np.array([4.0, 0.0, 0.0, 0.0])))
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_2(self):
        # Test with a sine wave signal
        signal = np.sin(np.linspace(0, 2 * np.pi, 100))
        transformed_signal, (ax1, ax2) = task_func(signal, precision=3)
        
        # Assert transformed signal values (checking just the first few)
        self.assertTrue(np.isclose(transformed_signal[0], 0.0, atol=1e-3))
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_3(self):
        # Test with a random signal
        signal = np.random.rand(50)
        transformed_signal, (ax1, ax2) = task_func(signal, precision=4)
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_4(self):
        # Test with a short signal
        signal = np.array([0., 1., 0., -1.])
        transformed_signal, (ax1, ax2) = task_func(signal, precision=1)
        
        # Assert transformed signal
        self.assertTrue(all(transformed_signal == np.array([-0.-0.j, 0.-2.j, 0.-0.j, 0.+2.j])))
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_5(self):
        # Test with a complex signal
        signal = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])
        transformed_signal, (ax1, ax2) = task_func(signal, precision=2)
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)