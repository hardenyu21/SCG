import numpy as np
import matplotlib.pyplot as plt

def task_func(mu, sigma, sample_size):
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, sample_size)
    
    # Plot the histogram of the generated samples
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Generated Samples')
    plt.show()
    
    # Return the generated samples as a numpy array
    return samples
import unittest
from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """ Test that the function returns a numpy array. """
        result = task_func(0, 1, 1000)
        self.assertIsInstance(result, np.ndarray)
    def test_sample_size(self):
        """ Test that the returned array has the correct size. """
        result = task_func(0, 1, 1000)
        self.assertEqual(len(result), 1000)
    def test_normal_distribution_properties(self):
        """ Test if the generated samples have the correct mean and standard deviation. """
        mu, sigma = 0, 1
        result = task_func(mu, sigma, 1000000)
        self.assertAlmostEqual(np.mean(result), mu, places=1)
        self.assertAlmostEqual(np.std(result), sigma, places=1)
    @patch('matplotlib.pyplot.show')
    def test_plot_labels_and_title(self, mock_show):
        """ Test if the plot has correct labels and title. """
        with patch('matplotlib.pyplot.hist') as mock_hist:
            task_func(0, 1, 1000)
            args, kwargs = mock_hist.call_args
            self.assertIn('bins', kwargs)
            self.assertEqual(kwargs['bins'], 30)
            self.assertEqual(kwargs['alpha'], 0.75)
            self.assertEqual(kwargs['color'], 'blue')
            self.assertEqual(plt.gca().get_xlabel(), 'Sample values')
            self.assertEqual(plt.gca().get_ylabel(), 'Frequency')
            self.assertEqual(plt.gca().get_title(), 'Histogram of Generated Samples')
    def test_mock_random_normal(self):
        """ Test the function with a mock of np.random.normal. """
        with patch('numpy.random.normal', return_value=np.full(1000, 0.5)) as mock_random_normal:
            mu, sigma = 0, 1
            result = task_func(mu, sigma, 1000)
            mock_random_normal.assert_called_once_with(mu, sigma, 1000)
            self.assertTrue(all(x == 0.5 for x in result))
    def test_output_consistency(self):
        """ Test if repeated calls with the same parameters produce different results. """
        mu, sigma = 0, 1
        result1 = task_func(mu, sigma, 1000)
        result2 = task_func(mu, sigma, 1000)
        self.assertFalse(np.array_equal(result1, result2))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)