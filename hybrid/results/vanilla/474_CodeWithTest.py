import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mu, scale=sigma, size=n_samples)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples with density normalization
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Calculate the PDF values for the range of the samples
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    
    # Plot the PDF as a red line
    ax.plot(x, p, 'r-', linewidth=2)
    
    # Set labels and title
    ax.set_title('Histogram and PDF of Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object and the samples
    return ax, samples

# Example usage
ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=42)
import unittest
import matplotlib.pyplot as plt
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.default_seed = 42
        self.large_n_samples = 100000
        self.small_n_samples = 100
        self.zero_n_samples = 0
        self.negative_n_samples = -100
        self.default_mu = 0
        self.default_sigma = 1
        self.large_sigma = 5
        self.small_sigma = 0.2
        self.zero_sigma = 0
        self.negative_sigma = -1
        self.custom_mu = 5
        self.custom_sigma = 2
    def test_case_1(self):
        # Test data generation correctness
        mu_test = 3
        sigma_test = 2
        n_samples_test = 10000
        random_seed_test = 42
        _, samples = task_func(
            n_samples=n_samples_test,
            mu=mu_test,
            sigma=sigma_test,
            random_seed=random_seed_test,
        )
        # Calculate sample mean and standard deviation
        sample_mean = np.mean(samples)
        sample_std = np.std(samples)
        # Verify sample mean and standard deviation are close to mu and sigma within a tolerance
        self.assertAlmostEqual(
            sample_mean,
            mu_test,
            places=1,
            msg="Sample mean does not match expected mean.",
        )
        self.assertAlmostEqual(
            sample_std,
            sigma_test,
            places=1,
            msg="Sample standard deviation does not match expected sigma.",
        )
    def test_case_2(self):
        # Default parameters
        ax, _ = task_func(random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_3(self):
        # Custom parameters: small number of samples, custom mean and standard deviation
        ax, _ = task_func(
            n_samples=self.small_n_samples,
            mu=self.custom_mu,
            sigma=self.custom_sigma,
            random_seed=self.default_seed,
        )
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_4(self):
        # Large number of samples
        ax, _ = task_func(n_samples=self.large_n_samples, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) >= 30)
    def test_case_5(self):
        # Small number of samples
        ax, _ = task_func(n_samples=self.small_n_samples, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) <= 30)
    def test_case_6(self):
        # Large standard deviation
        ax, _ = task_func(sigma=self.large_sigma, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_7(self):
        # Small standard deviation
        ax, _ = task_func(sigma=self.small_sigma, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_8(self):
        # Invalid negative standard deviation
        with self.assertRaises(ValueError):
            task_func(sigma=self.negative_sigma)
    def test_case_9(self):
        # Invalid zero standard deviation
        with self.assertRaises(Exception):
            task_func(sigma=self.zero_sigma)
    def test_case_10(self):
        # Invalid zero samples
        with self.assertRaises(Exception):
            task_func(n_samples=self.zero_n_samples)
    def test_case_11(self):
        # Invalid negative samples
        with self.assertRaises(ValueError):
            task_func(n_samples=self.negative_n_samples)
    def test_case_12(self):
        # Reproducibility with same seed
        ax1, sample1 = task_func(random_seed=self.default_seed)
        ax2, sample2 = task_func(random_seed=self.default_seed)
        self.assertEqual(ax1.patches[0].get_height(), ax2.patches[0].get_height())
        self.assertTrue((sample1 == sample2).all())
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)