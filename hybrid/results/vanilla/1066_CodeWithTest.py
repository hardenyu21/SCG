import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    normal_data = np.random.normal(loc=0, scale=1, size=num_samples)
    
    # Introduce artificial outliers
    outliers = np.random.uniform(low=-10, high=10, size=num_outliers)
    
    # Combine normal data and outliers
    data = np.concatenate((normal_data, outliers))
    
    # Sort data to facilitate IQR calculation
    sorted_data = np.sort(normal_data)
    
    # Calculate Q1 and Q3
    Q1 = np.percentile(sorted_data, 25)
    Q3 = np.percentile(sorted_data, 75)
    
    # Calculate IQR
    IQR = Q3 - Q1
    
    # Define outlier boundaries
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Detect outliers in the normally distributed data
    outliers_detected = normal_data[(normal_data < lower_bound) | (normal_data > upper_bound)]
    
    # Plot histogram of the combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, alpha=0.7, color='blue', edgecolor='black')
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Highlight detected outliers
    ax.scatter(outliers_detected, np.zeros_like(outliers_detected) - 0.1, color='red', zorder=5, label='Detected Outliers')
    ax.scatter(outliers, np.zeros_like(outliers) - 0.2, color='green', zorder=5, label='Artificial Outliers')
    ax.legend()
    
    # Show plot
    plt.show()
    
    return data, outliers_detected, ax

# Example usage
data, outliers_detected, ax = task_func()
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""
    def test_default_values(self):
        """Test the function with default values."""
        np.random.seed(0)
        data, _, _ = task_func()
        self.assertEqual(len(data), 105)
    def test_custom_values(self):
        """Test the function with custom values."""
        np.random.seed(1)
        data, outliers_detected, _ = task_func(num_samples=50, num_outliers=10)
        self.assertEqual(len(data), 60)
        # Replicate the IQR calculation for testing
        normal_data = data[:50]  # Assuming the first 50 are normal data
        q75, q25 = np.percentile(normal_data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - (iqr * 1.5)
        upper_bound = q75 + (iqr * 1.5)
        expected_outliers_count = len(
            [o for o in data if o < lower_bound or o > upper_bound]
        )
        self.assertEqual(len(outliers_detected), expected_outliers_count)
    def test_no_outliers(self):
        """Test the function with no outliers."""
        np.random.seed(2)
        data, outliers_detected, ax = task_func(num_samples=100, num_outliers=0)
        self.assertEqual(len(data), 100)
        # Adjust the expectation to consider possible false positives
        self.assertTrue(len(outliers_detected) <= 1)  # Allow for up to 1 false positive
    def test_only_outliers(self):
        """Test the function with only outliers."""
        np.random.seed(3)
        data, outliers_detected, _ = task_func(num_samples=0, num_outliers=100)
        self.assertEqual(len(data), 100)
        # Since no normal data is generated, IQR is not applied, and no outliers are detected.
        self.assertEqual(len(outliers_detected), 0)
    def test_negative_values(self):
        """Test the function with negative values."""
        np.random.seed(4)
        with self.assertRaises(ValueError):
            task_func(num_samples=-10, num_outliers=-5)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)