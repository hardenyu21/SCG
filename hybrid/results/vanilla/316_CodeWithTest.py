import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    # Generate a random number of items within the specified range
    num_items = random.randint(value_range[0], value_range[1])
    
    # Randomly assign categories to each item
    category_assignments = [random.choice(CATEGORIES) for _ in range(num_items)]
    
    # Count the occurrences of each category
    category_counts = {category: category_assignments.count(category) for category in CATEGORIES}
    
    # Create a DataFrame from the category counts
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df

# Example usage
df = task_func((50, 100))
print(df)
import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test if the function returns a DataFrame."""
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)
    def test_columns(self):
        """Test if the DataFrame has the correct columns."""
        random.seed(0)
        result = task_func()
        self.assertListEqual(list(result.columns), ['Category', 'Count'])
    def test_value_range_default(self):
        """Test if the 'Count' values are within the default range."""
        random.seed(0)
        result = task_func()
        for count in result['Count']:
            self.assertTrue(0 <= count <= 100)
    def test_value_range_custom(self):
        """Test if the 'Count' values are within a custom range."""
        random.seed(0)
        test_range = (10, 50)
        result = task_func(value_range=test_range)
        for count in result['Count']:
            self.assertTrue(test_range[0] <= count <= test_range[1])
    def test_number_of_rows(self):
        """Test if the DataFrame contains the expected number of rows."""
        random.seed(0)
        result = task_func()
        self.assertEqual(len(result), len(CATEGORIES))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)