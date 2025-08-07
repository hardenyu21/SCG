import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    # Check if the radius is negative
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    # Check if the provided Axes object is a polar plot
    if not ax.name == 'polar':
        raise TypeError("The provided Axes object is not a polar plot.")
    
    # Create an array of angles from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate the x and y coordinates for the circle
    r = np.full_like(theta, radius)
    
    # Plot the circle on the polar plot
    ax.plot(theta, r, label=f'Circle with radius {radius}')
    
    # Set radial ticks
    ax.set_rticks([radius / 2, radius, 3 * radius / 2])
    
    # Add a legend
    ax.legend(loc='upper right')
    
    # Return the modified Axes object
    return ax
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_polar_plot(self):
        '''Test if the function plots on a polar plot.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        result_ax = task_func(ax, 1.0)
        self.assertIsInstance(result_ax, plt.PolarAxes)
        plt.close()
    def test_circle_radius(self):
        '''Test if the circle is drawn with the correct radius.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        radius = 2.0
        result_ax = task_func(ax, radius)
        for line in result_ax.get_lines():
            self.assertTrue(np.allclose(line.get_ydata(), radius))
        plt.close()
    def test_negative_radius(self):
        '''Test handling of negative radius.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        with self.assertRaises(ValueError):
            task_func(ax, -1.0)
        plt.close()
    def test_non_polar_plot(self):
        '''Test handling of non-polar plot input.'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        with self.assertRaises(TypeError):
            task_func(ax, 1.0)
        plt.close()
    def test_zero_radius(self):
        '''Test handling of zero radius.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        radius = 0.0
        result_ax = task_func(ax, radius)
        for line in result_ax.get_lines():
            self.assertTrue(np.allclose(line.get_ydata(), radius))
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)