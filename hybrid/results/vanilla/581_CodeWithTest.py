import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def task_func(size=SIZE, frequency=1):
    # Generate random phase shift
    phase_shift = random.uniform(0, 2 * PI)
    
    # Generate x values
    x_values = np.linspace(0, RANGE, size)
    
    # Generate random sinusoidal values
    y_values = np.sin(2 * PI * frequency * x_values / RANGE + phase_shift)
    
    # Plot the sinusoidal wave
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_title('Random Sinusoidal Wave')
    ax.set_xlabel('X')
    ax.set_ylabel('Amplitude')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage
task_func()
import unittest
class TestCases(unittest.TestCase):
        
    def test_case_4(self):
        ax = task_func(size=1500, frequency=0.5)
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), 1500)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)
    def test_standard_functionality(self):
        """Test the function with default parameters."""
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
    def test_varying_sizes(self):
        """Test the function with different array sizes."""
        for size in [0, 10, 500, 1500]:
            ax = task_func(size=size)
            self.assertIsInstance(ax, plt.Axes)
            self.assertEqual(len(ax.lines[0].get_xdata()), size)
    def test_different_frequencies(self):
        """Test the function with different frequencies."""
        for frequency in [0.5, 1, 2]:
            ax = task_func(frequency=frequency)
            self.assertIsInstance(ax, plt.Axes)
    def test_plot_output(self):
        """Verify the plot is generated and is of correct type."""
        ax = task_func()
        self.assertTrue(hasattr(ax, 'figure'), "Plot does not have associated figure attribute")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)