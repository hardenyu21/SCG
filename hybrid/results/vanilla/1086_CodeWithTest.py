import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples

def task_func():
    # Generate random strings of 10 ASCII letters
    random_strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(NUM_SAMPLES)]
    
    # Generate random floats between 0 and 10000
    random_floats = [random.uniform(0, 10000) for _ in range(NUM_SAMPLES)]
    
    # Format floats with two decimal places and a comma as the thousands separator
    formatted_floats = [f"{num:,.2f}" for num in random_floats]
    
    # Create a DataFrame
    df = pd.DataFrame({
        'String Field': random_strings,
        'Float Field': formatted_floats
    })
    
    return df

# Example usage
df = task_func()
print(df.head())
import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_dataframe_creation(self):
        """
        Test if the function returns a pandas DataFrame.
        """
        random.seed(1)
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)
    def test_row_count(self):
        """
        Test if the DataFrame contains the correct number of rows.
        """
        random.seed(2)
        result = task_func()
        self.assertEqual(len(result), NUM_SAMPLES)
    def test_column_count(self):
        """
        Test if the DataFrame contains exactly two columns.
        """
        random.seed(3)
        result = task_func()
        self.assertEqual(len(result.columns), 2)
    def test_string_field_format(self):
        """
        Test if the 'String Field' contains strings of 10 ASCII letters.
        """
        random.seed(4)
        result = task_func()
        all_strings = all(result["String Field"].str.match("^[A-Za-z]{10}$"))
        self.assertTrue(all_strings)
    def test_float_field_format(self):
        """
        Test if the 'Float Field' contains formatted float strings.
        """
        random.seed(5)
        result = task_func()
        all_floats = all(
            isinstance(float(val.replace(",", "")), float)
            for val in result["Float Field"]
        )
        self.assertTrue(all_floats)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)