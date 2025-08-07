import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(loc=mean, scale=std_dev, size=1000)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    
    # Create a histogram
    plt.figure(figsize=(10, 5))
    plt.hist(sample, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Histogram of the Sample')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    histogram_path = 'histogram.png'
    if save_plots:
        plt.savefig(histogram_path)
    plt.show()
    
    # Create a QQ plot
    plt.figure(figsize=(10, 5))
    stats.probplot(sample, dist="norm", plot=plt)
    plt.title('QQ Plot of the Sample')
    qqplot_path = 'qqplot.png'
    if save_plots:
        plt.savefig(qqplot_path)
    plt.show()
    
    # Return the results
    plot_paths = [histogram_path, qqplot_path] if save_plots else []
    return skewness, kurtosis, plot_paths

# Example usage:
# skew, kurt, plot_files = task_func(save_plots=True)
# print(f"Skewness: {skew}, Kurtosis: {kurt}, Plot Files: {plot_files}")
import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_default_parameters(self):
        """
        Test task_func with default parameters.
        """
        np.random.seed(0)
        skewness, kurtosis, plot_paths = task_func()
        self.assertAlmostEqual(skewness, 0, delta=0.5)
        self.assertAlmostEqual(kurtosis, 0, delta=0.5)
        self.assertEqual(len(plot_paths), 0)
    def test_save_plots_true(self):
        """
        Test task_func with save_plots set to True.
        """
        np.random.seed(1)
        _, _, plot_paths = task_func(save_plots=True)
        self.assertEqual(len(plot_paths), 2)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))
            os.remove(path)  # Clean up: remove created files
    def test_custom_mean_std_dev(self):
        """
        Test task_func with custom mean and standard deviation.
        """
        np.random.seed(2)
        mean = 100
        std_dev = 10
        skewness, kurtosis, _ = task_func(mean, std_dev)
        self.assertAlmostEqual(skewness, 0, delta=1)
        self.assertAlmostEqual(kurtosis, 0, delta=1)
    def test_negative_std_dev(self):
        """
        Test task_func with a negative standard deviation.
        """
        np.random.seed(3)
        with self.assertRaises(ValueError):
            task_func(std_dev=-1)
    def test_large_sample(self):
        """
        Test task_func with a larger sample size.
        """
        np.random.seed(4)
        _, _, plot_paths = task_func(mean=1000, std_dev=50, save_plots=True)
        self.assertEqual(len(plot_paths), 2)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))
            os.remove(path)  # Clean up: remove created files


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)