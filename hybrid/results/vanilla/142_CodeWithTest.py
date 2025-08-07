import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Create an array of x values from 0 to 2π
    x = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the sine and cosine of x
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    # Create a figure and a set of subplots
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    
    # Plot the sine function
    axs[0].plot(x, y_sin, label='sin(x)')
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    axs[0].grid(True)
    
    # Plot the cosine function
    axs[1].plot(x, y_cos, label='cos(x)', color='orange')
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    axs[1].grid(True)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Return the figure and axes
    return fig, axs

# Example usage
fig, axs = task_func()
plt.show()
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.fig, self.axs = task_func()
    def test_return_types(self):
        self.assertIsInstance(self.fig, plt.Figure)
        self.assertEqual(len(self.axs), 2)
        for ax in self.axs:
            self.assertIsInstance(ax, plt.Axes)
    def test_plot_titles(self):
        self.assertEqual(self.axs[0].get_title(), 'Sine function')
        self.assertEqual(self.axs[1].get_title(), 'Cosine function')
    def test_axes_labels(self):
        self.assertEqual(self.axs[0].get_xlabel(), 'x')
        self.assertEqual(self.axs[0].get_ylabel(), 'sin(x)')
        self.assertEqual(self.axs[1].get_xlabel(), 'x')
        self.assertEqual(self.axs[1].get_ylabel(), 'cos(x)')
    def test_plot_contents(self):
        sine_line = self.axs[0].lines[0]
        cosine_line = self.axs[1].lines[0]
        np.testing.assert_array_almost_equal(sine_line.get_ydata(), np.sin(sine_line.get_xdata()), decimal=5)
        np.testing.assert_array_almost_equal(cosine_line.get_ydata(), np.cos(cosine_line.get_xdata()), decimal=5)
    def test_x_values_range(self):
        for ax in self.axs:
            line = ax.lines[0]
            self.assertTrue(np.all(line.get_xdata() >= 0) and np.all(line.get_xdata() <= 2 * np.pi))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)