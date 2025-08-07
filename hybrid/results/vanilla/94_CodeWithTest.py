import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mean, scale=std_dev, size=num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Overlay the PDF of the normal distribution
    pdf_x = np.linspace(min(bins), max(bins), 1000)
    pdf_y = norm.pdf(pdf_x, mean, std_dev)
    ax.plot(pdf_x, pdf_y, 'k', linewidth=2)
    
    # Set the title with the fit results
    ax.set_title(f"Fit results: mean = {mean:.2f}, std = {std_dev:.2f}")
    
    # Show the plot
    plt.show()
    
    # Return the figure and the samples
    return fig, samples

# Example usage:
# fig, samples = task_func(0, 1, 1000)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        """ Set up for each test, fixing the random seed for reproducibility. """
        np.random.seed(0)
    def test_samples_length(self):
        """ Test if the number of generated samples is correct. """
        samples, _ = task_func(0, 1, 1000)
        self.assertEqual(len(samples), 1000)
    def test_samples_type(self):
        """ Test the type of the samples. """
        samples, _ = task_func(0, 1, 1000)
        self.assertIsInstance(samples, np.ndarray)
    def test_mean_approximation(self):
        """ Test if the mean of the samples is approximately equal to the specified mean. """
        samples, _ = task_func(0, 1, 1000)
        self.assertAlmostEqual(np.mean(samples), 0, places=1)
    def test_std_dev_approximation(self):
        """ Test if the standard deviation of the samples is approximately equal to the specified standard deviation. """
        samples, _ = task_func(0, 1, 1000)
        self.assertAlmostEqual(np.std(samples), 1, places=1)
    def test_plot_title(self):
        """ Test if the plot title correctly reflects the mean and standard deviation. """
        _, fig = task_func(0, 1, 1000)
        self.assertIn("mean = 0.00,  std = 1.00", fig.axes[0].get_title())
    def test_histogram_bins(self):
        """ Test if the histogram displays the correct number of bins. """
        _, fig = task_func(0, 1, 1000)
        self.assertEqual(len(fig.axes[0].patches), 30)  # Check for 30 bins, as defined in the function
    def test_pdf_overlay(self):
        """ Test if the probability density function (PDF) is correctly overlayed on the histogram. """
        _, fig = task_func(0, 1, 1000)
        lines = fig.axes[0].get_lines()
        self.assertGreater(len(lines), 0)  # Ensure that at l
    def test_pdf_overlay_accuracy(self):
        """ Test if the PDF overlay accurately represents the normal distribution. """
        mean, std_dev, num_samples = 0, 1, 1000
        _, fig = task_func(mean, std_dev, num_samples)
        ax = fig.axes[0]
        line = ax.get_lines()[0]  # Assuming the first line is the PDF
        x, y = line.get_data()
        expected_y = norm.pdf(x, mean, std_dev)
        np.testing.assert_array_almost_equal(y, expected_y, decimal=2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)