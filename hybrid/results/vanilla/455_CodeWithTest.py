import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mean, scale=std_dev, size=n)
    
    # Plot histogram of the samples
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram of samples')
    
    # Plot the probability density function
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2, label='PDF')
    
    # Add labels and legend
    plt.title('Histogram and PDF of Generated Samples')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    
    # Show the plot
    plt.show()
    
    return samples

# Example usage
samples = task_func(5, 2, 500)
print(len(samples))  # Should output 500
import unittest
class TestCases(unittest.TestCase):
    def test_sample_length(self):
        # Test if the function returns the correct number of samples
        samples = task_func(0, 1, 1000)
        self.assertEqual(len(samples), 1000)
    def test_sample_mean(self):
        # Test if the mean of the samples is approximately equal to the specified mean
        samples = task_func(0, 1, 100000)
        self.assertAlmostEqual(np.mean(samples), 0, places=1)
    def test_sample_std_dev(self):
        # Test if the standard deviation of the samples is approximately equal to the specified standard deviation
        samples = task_func(0, 1, 100000)
        self.assertAlmostEqual(np.std(samples), 1, places=1)
    def test_negative_std_dev(self):
        # Test if a ValueError is raised for negative standard deviations
        with self.assertRaises(ValueError):
            task_func(0, -1, 1000)
    def test_zero_samples(self):
        # Test if the function can handle a request for zero samples
        samples = task_func(0, 1, 0)
        self.assertEqual(len(samples), 0)
    def test_return_type(self):
        # Test if the function returns a numpy array
        samples = task_func(0, 1, 100)
        self.assertIsInstance(samples, np.ndarray)
    def test_non_integer_samples(self):
        # Test if the function raises a TypeError for non-integer n
        with self.assertRaises(TypeError):
            task_func(0, 1, '100')
    def test_non_numeric_mean_or_std(self):
        # Test if the function raises a TypeError for non-numeric mean or std_dev
        with self.assertRaises(TypeError):
            task_func('0', 1, 100)
        with self.assertRaises(TypeError):
            task_func(0, '1', 100)
    def test_very_small_n(self):
        # Test if the function behaves correctly for very small n
        samples = task_func(0, 1, 1)
        self.assertEqual(len(samples), 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)