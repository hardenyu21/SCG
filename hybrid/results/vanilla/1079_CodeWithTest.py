import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert string prices to float, handling commas as thousand separators
    data['Price'] = data['Price_String'].str.replace(',', '').astype(float)
    
    # Calculate statistical measures
    mean_price = data['Price'].mean()
    median_price = data['Price'].median()
    std_dev_price = data['Price'].std()
    
    # Create a dictionary with the calculated statistics
    stats = {
        'mean': mean_price,
        'median': median_price,
        'std_dev': std_dev_price
    }
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data['Price'], bins='auto', color='blue', alpha=0.7, rwidth=0.85)
    ax.set_title('Histogram of Product Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')
    
    # Return the statistics and the Axes object
    return stats, ax

# Example usage:
# data = pd.DataFrame({
#     'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
#     'Price_String': ['1,200', '1,500', '1,800', '2,100']
# })
# stats, ax = task_func(data)
# plt.show()
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_basic_functionality(self):
        """Test basic functionality."""
        sample_data = {
            "Product": ["James", "Olivia", "Jamie", "Angela", "Jennifer"],
            "Price_String": ["2,213.00", "6,083.00", "5,461.00", "884.00", "2,783.00"],
        }
        float_prices = [
            float(price.replace(",", "")) for price in sample_data["Price_String"]
        ]
        expected_mean = np.mean(float_prices)
        expected_median = np.median(float_prices)
        expected_std_dev = np.std(float_prices, ddof=1)
        result, _ = task_func(sample_data)
        self.assertAlmostEqual(result["mean"], expected_mean)
        self.assertAlmostEqual(result["median"], expected_median)
        self.assertAlmostEqual(result["std_dev"], expected_std_dev)
    def test_large_sample_size(self):
        """Test large sample size."""
        sample_data = {
            "Product": [
                "Adam",
                "Lisa",
                "Scott",
                "Bianca",
                "Ashlee",
                "Shannon",
                "Michelle",
                "Robert",
                "Joseph",
                "Joshua",
                "Traci",
                "Jacob",
                "Daniel",
                "Timothy",
                "Paul",
            ],
            "Price_String": [
                "1,691.00",
                "967.00",
                "5,789.00",
                "6,806.00",
                "3,301.00",
                "5,319.00",
                "7,619.00",
                "134.00",
                "7,883.00",
                "5,028.00",
                "3,330.00",
                "5,253.00",
                "8,551.00",
                "1,631.00",
                "7,637.00",
            ],
        }
        float_prices = [
            float(price.replace(",", "")) for price in sample_data["Price_String"]
        ]
        expected_mean = np.mean(float_prices)
        expected_median = np.median(float_prices)
        expected_std_dev = np.std(float_prices, ddof=1)
        result, _ = task_func(sample_data)
        self.assertAlmostEqual(result["mean"], expected_mean)
        self.assertAlmostEqual(result["median"], expected_median)
        self.assertAlmostEqual(result["std_dev"], expected_std_dev)
    def test_invalid_input(self):
        """Test invalid input."""
        with self.assertRaises(Exception):
            task_func({})
        with self.assertRaises(Exception):
            task_func({"Product": ["Apple"], "Price_WrongKey": ["1,234.00"]})
    def test_all_zero_prices(self):
        """Test all zero prices."""
        sample_data = {
            "Product": ["Apple", "Banana", "Cherry"],
            "Price_String": ["0.00", "0.00", "0.00"],
        }
        result, _ = task_func(sample_data)
        self.assertEqual(result["mean"], 0)
        self.assertEqual(result["median"], 0)
        self.assertEqual(result["std_dev"], 0)
    def test_non_uniform_distribution(self):
        """Test non-uniform distribution."""
        sample_data = {
            "Product": ["Apple", "Banana", "Cherry", "Date", "Fig"],
            "Price_String": ["1,000.00", "500.00", "1,500.00", "2,000.00", "2,500.00"],
        }
        float_prices = [
            float(price.replace(",", "")) for price in sample_data["Price_String"]
        ]
        expected_mean = np.mean(float_prices)
        expected_median = np.median(float_prices)
        expected_std_dev = np.std(float_prices, ddof=1)
        result, _ = task_func(sample_data)
        self.assertAlmostEqual(result["mean"], expected_mean)
        self.assertAlmostEqual(result["median"], expected_median)
        self.assertAlmostEqual(result["std_dev"], expected_std_dev)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)