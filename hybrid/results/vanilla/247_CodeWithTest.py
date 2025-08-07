import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Validate input
    if max_value < min_value:
        raise ValueError("max_value must be greater than or equal to min_value.")
    
    # Generate random floating point numbers
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_data = [round(num, 3) for num in data]
    
    # Convert to DataFrame
    df = pd.DataFrame(truncated_data, columns=['Original Value'])
    
    # Normalize the data using standard scaling
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(df[['Original Value']])
    
    # Create a new DataFrame with the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=['Normalized Value'])
    
    return normalized_df

# Example usage
if __name__ == "__main__":
    df = task_func()
    print(df.head())
import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        df = task_func()
        self.assertIsInstance(df, pd.DataFrame, "Return type should be a DataFrame.")
        self.assertEqual(len(df), 5000, "Default number of data points should be 5000.")
        self.assertAlmostEqual(df['Normalized Value'].mean(), 0, delta=0.1, msg="Mean should be close to 0.")
        self.assertAlmostEqual(df['Normalized Value'].std(), 1, delta=0.1, msg="Standard deviation should be close to 1.")
    def test_custom_parameters(self):
        random.seed(0)
        df = task_func(1000, 1.0, 5.0)
        self.assertEqual(len(df), 1000, "Number of data points should match the specified value.")
        self.assertTrue(df['Normalized Value'].min() >= -3, "Normalized values should be within a reasonable range.")
        self.assertTrue(df['Normalized Value'].max() <= 3, "Normalized values should be within a reasonable range.")
    def test_edge_case_empty(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            task_func(0)
    def test_negative_data_points(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            task_func(-100)
    def test_invalid_range(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            task_func(1000, 5.0, 1.0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)