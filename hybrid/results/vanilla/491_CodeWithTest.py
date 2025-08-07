import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    # Set the random seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Convert epoch milliseconds to a datetime object
    start_date = datetime.utcfromtimestamp(epoch_milliseconds / 1000.0)
    current_date = datetime.utcnow()
    
    # Validate the start date
    if epoch_milliseconds < 0 or start_date > current_date:
        raise ValueError("The start time is negative or after the current time.")
    
    # Calculate the number of days between the start date and the current date
    num_days = (current_date - start_date).days + 1
    
    # Define the categories
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Initialize sales data
    sales_data = {category: [] for category in categories}
    
    # Generate random sales data for each day
    for day in range(num_days):
        for category in categories:
            sales = random.randint(10, 50)
            sales_data[category].append(sales)
    
    # Plot the sales trend
    fig, ax = plt.subplots(figsize=(10, 6))
    for category in categories:
        ax.plot(range(num_days), sales_data[category], label=category)
    
    ax.set_xlabel('Days since ({})'.format(start_date.strftime('%Y-%m-%d')))
    ax.set_ylabel('Sales Units')
    ax.set_title('Sales Trend Over Time')
    ax.legend()
    ax.grid(True)
    
    # Show the plot
    plt.show()
    
    return sales_data, ax

# Example usage:
# epoch_milliseconds = 1609459200000  # Example epoch milliseconds for January 1, 2021
# sales_data, ax = task_func(epoch_milliseconds, seed=42)
import unittest
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
class TestCases(unittest.TestCase):
    def _check_sales_data(self, sales_data, expected_days):
        """Utility function to validate sales data."""
        self.assertIsInstance(sales_data, dict)
        self.assertEqual(
            set(sales_data.keys()),
            set(["Electronics", "Clothing", "Home", "Books", "Sports"]),
        )
        for category, sales in sales_data.items():
            self.assertEqual(len(sales), expected_days)
            for sale in sales:
                self.assertGreaterEqual(sale, 10)
                self.assertLessEqual(sale, 50)
    def test_case_1(self):
        # Basic test on manual example - Jan 1 2021
        sales_data, ax = task_func(1609459200000, seed=1)
        self.assertIsInstance(sales_data, dict)
        self.assertIsInstance(ax, plt.Axes)
        self._check_sales_data(
            sales_data,
            (datetime.now() - datetime.utcfromtimestamp(1609459200000 / 1000.0)).days,
        )
        self.assertEqual(ax.get_ylabel(), "Sales")
    def test_case_2(self):
        # Basic test on current date - should raise error
        current_epoch = int(datetime.now().timestamp() * 1000)
        with self.assertRaises(ValueError):
            task_func(current_epoch, seed=2)
    def test_case_3(self):
        # Test random seed
        t = 1609459200000
        sales_data1, _ = task_func(t, seed=42)
        sales_data2, _ = task_func(t, seed=42)
        sales_data3, _ = task_func(t, seed=3)
        self.assertEqual(sales_data1, sales_data2)
        self.assertNotEqual(sales_data1, sales_data3)
    def test_case_4(self):
        # Test that future date raises ValueError
        future_epoch = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)
        with self.assertRaises(ValueError):
            task_func(future_epoch, seed=4)
    def test_case_5(self):
        # Test that negative epoch milliseconds raise an error
        with self.assertRaises(ValueError):
            task_func(-1609459200000, seed=5)
    def test_case_6(self):
        # Test that non-integer types for epoch milliseconds raise a TypeError
        with self.assertRaises(TypeError):
            task_func("1609459200000", seed=6)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)