import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a sample from a normal distribution
    sample = np.random.normal(loc=mu, scale=sigma, size=sample_size)
    
    # Calculate the empirical mean and standard deviation
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample, ddof=1)  # Using Bessel's correction
    
    # Create a histogram of the sample
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(sample, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Plot the probability density function (PDF)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set the title with the given format
    ax.set_title(r'Normal Distribution with $\mu = %0.2f, \sigma = %0.2f$' % (mu, sigma))
    
    # Return the Axes object and the empirical mean and standard deviation
    return ax, empirical_mean, empirical_std

# Example usage:
# ax, empirical_mean, empirical_std = task_func(mu=5, sigma=2, sample_size=1000, seed=42)
# plt.show()
# print("Empirical Mean:", empirical_mean)
# print("Empirical Standard Deviation:", empirical_std)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax, _, _ = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 0.00, \\sigma = 1.00$")
    def test_case_2(self):
        ax, mean, std = task_func(mu=5, sigma=2, sample_size=500, seed=42)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 5.00, \\sigma = 2.00$")
        self.assertAlmostEqual(mean, 5.0136, places=3)
    def test_case_3(self):
        ax, mean, std = task_func(mu=-3, sigma=5, sample_size=2000, seed=23)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = -3.00, \\sigma = 5.00$")
        self.assertAlmostEqual(std, 4.978, places=3)
    def test_case_4(self):
        ax, _, _ = task_func(mu=1, sigma=0.5, sample_size=100)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 1.00, \\sigma = 0.50$")
    def test_case_5(self):
        ax, mean, std = task_func(mu=10, sigma=0.1, sample_size=1500)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 10.00, \\sigma = 0.10$")
        self.assertAlmostEqual(mean, 9.998, places=3)
        self.assertAlmostEqual(std, 0.09804, places=3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)