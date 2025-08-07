import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from scipy.stats import norm

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, bins=num_bins, density=True, alpha=0.6, color='b', edgecolor='black')
    
    # Calculate the PDF of the normal distribution
    pdf_x = np.linspace(min(bins), max(bins), 1000)
    pdf_y = norm.pdf(pdf_x, mu, sigma)
    
    # Overlay the PDF on the histogram
    ax.plot(pdf_x, pdf_y, 'r-', linewidth=2, label='PDF')
    
    # Fit a second order polynomial to the histogram bins using OLS
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    model = ols('count ~ I(bin_centers**2) + bin_centers', data={'count': count, 'bin_centers': bin_centers}).fit()
    
    # Generate the polynomial values
    poly_x = np.linspace(min(bins), max(bins), 1000)
    poly_y = model.predict({'bin_centers': poly_x, 'I(bin_centers**2)': poly_x**2})
    
    # Overlay the polynomial on the histogram
    ax.plot(poly_x, poly_y, 'g-', linewidth=2, label='2nd Order Polynomial')
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func(mu=0, sigma=1)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = task_func(0, 1)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Check if the OLS line is plotted
        self.assertEqual(ax.lines[1].get_color(), 'g', "The OLS line color should be green.")
        
    def test_case_2(self):
        ax = task_func(2, 2, 555, 1000, 50)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Check if the OLS line is plotted
        self.assertEqual(ax.lines[1].get_color(), 'g', "The OLS line color should be green.")
        # Check the axis data
        self.assertAlmostEquals(ax.get_xlim()[0], -5.66, msg="The x-axis limits are incorrect.", places=2)
        self.assertAlmostEquals(ax.get_xlim()[1], 8.54, msg="The x-axis limits are incorrect.", places=2)
        
    def test_case_3(self):
        ax = task_func(-2, 0.5, 77, 50000)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Check the axis data
        self.assertAlmostEquals(ax.get_ylim()[0], -0.28, msg="The y-axis limits are incorrect.", places=2)
        self.assertAlmostEquals(ax.get_ylim()[1], 0.84, msg="The y-axis limits are incorrect.", places=2)
        # Check the histogram data
        self.assertEqual(len(ax.patches), 30, "The number of histogram bars is incorrect.")
        
    def test_case_4(self):
        ax = task_func(5, 3)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Test the plot array
        self.assertEqual(len(ax.lines), 2, "The plot should have two lines.")
        
    def test_case_5(self):
        ax = task_func(-5, 1.5)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)