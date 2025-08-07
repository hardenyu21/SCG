import pandas as pd
import random

# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS):
    if n_data_points == 0:
        return pd.DataFrame(columns=['Value'])
    
    # Generate random floating-point numbers
    random_values = [random.uniform(MIN_VALUE, MAX_VALUE) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_values = [round(value, 3) for value in random_values]
    
    # Create a DataFrame
    df = pd.DataFrame(truncated_values, columns=['Value'])
    
    return df
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_return_type(self):
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)
    def test_data_points_count(self):
        random.seed(0)
        result = task_func()
        self.assertEqual(len(result), 10000)
    def test_value_range(self):
        random.seed(0)
        result = task_func()
        within_range = result['Value'].apply(lambda x: 0.0 <= x <= 10.0)
        self.assertTrue(within_range.all())
    def test_value_truncation(self):
        random.seed(0)
        result = task_func()
        correctly_truncated = result['Value'].apply(lambda x: len(str(x).split('.')[1]) <= 3 if '.' in str(x) else True)
        self.assertTrue(correctly_truncated.all())
    def test_empty_data_frame(self):
        random.seed(0)
        result = task_func(n_data_points=0)
        self.assertTrue(result.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)