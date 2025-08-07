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
import unittest
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import get_window
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up common constants for the tests."""
        self.amplitude = 1
        self.frequency = 5
        self.time = np.linspace(0, 1, 500, endpoint=False)
    def test_return_types(self):
        """Test that the function returns a numpy array, a matplotlib figure, and axes objects."""
        wave, fig, ax = task_func(self.amplitude, self.frequency, self.time)
        self.assertIsInstance(wave, np.ndarray)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, plt.Axes)
    def test_array_length(self):
        """Test the length of the returned array matches the length of the time array."""
        wave, _, _ = task_func(self.amplitude, self.frequency, self.time)
        self.assertEqual(len(wave), len(self.time))
    def test_wave_properties(self):
        """Test that the wave properties conform to expected cosine and sine functions with Hann window applied."""
        wave, _, _ = task_func(self.amplitude, self.frequency, self.time)
        window = get_window('hann', self.time.size)  # Apply a Hann window
        expected_wave = self.amplitude * np.exp(1j * 2 * math.pi * self.frequency * self.time) * window
        np.testing.assert_array_almost_equal(wave, expected_wave)
    def test_zero_amplitude(self):
        """Test that the wave is zero throughout when amplitude is zero."""
        wave, _, _ = task_func(0, self.frequency, self.time)
        self.assertTrue(np.all(wave == 0))
    def test_different_frequencies(self):
        """Test the function with different frequencies to ensure the wave changes accordingly."""
        wave_1, _, _ = task_func(self.amplitude, 1, self.time)
        wave_2, _, _ = task_func(self.amplitude, 2, self.time)
        self.assertFalse(np.array_equal(wave_1, wave_2))
    def test_negative_frequency(self):
        """Test that the function correctly handles negative frequencies with Hann window applied."""
        wave, _, _ = task_func(self.amplitude, -1, self.time)
        window = get_window('hann', self.time.size)  # Apply a Hann window
        expected_wave = self.amplitude * np.exp(-1j * 2 * math.pi * self.time) * window
        np.testing.assert_array_almost_equal(wave, expected_wave)
    def test_plot_title(self):
        """Test that the plot title is correctly set."""
        _, fig, _ = task_func(self.amplitude, self.frequency, self.time)
        self.assertEqual(fig.axes[0].get_title(), "Complex Wave with Hann Window")
    def test_plot_x_label(self):
        """Test that the x-axis label is correctly set to 'Time'."""
        _, _, ax = task_func(self.amplitude, self.frequency, self.time)
        self.assertEqual(ax.get_xlabel(), "Time")
    def test_plot_y_label(self):
        """Test that the y-axis label is correctly set to 'Amplitude'."""
        _, _, ax = task_func(self.amplitude, self.frequency, self.time)
        self.assertEqual(ax.get_ylabel(), "Amplitude")
    def test_plot_lines(self):
        """Test that the plot includes both real and imaginary parts of the complex wave."""
        _, _, ax = task_func(self.amplitude, self.frequency, self.time)
        lines = ax.get_lines()
        # Assuming the first line is the real part and the second line is the imaginary part
        self.assertEqual(len(lines), 2, "Plot does not contain two lines for real and imaginary parts")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)