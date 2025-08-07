import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    # Check if the DataFrame is empty
    if df.empty:
        return None, None
    
    # Check if the specified columns are in the DataFrame
    if not all(col in df.columns for col in [col_a, col_b, col_c]):
        return None, None
    
    # Check if the specified columns contain numeric data
    if not pd.api.types.is_numeric_dtype(df[col_a]) or not pd.api.types.is_numeric_dtype(df[col_b]) or not pd.api.types.is_numeric_dtype(df[col_c]):
        return None, None
    
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[col_b] > 50) & (df[col_c] == 900)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None, None
    
    # Prepare the data for training
    X = filtered_df[[col_a]]
    y = filtered_df[col_b]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    
    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Generate predictions on the test set
    predictions = model.predict(X_test)
    
    return predictions, model
import unittest
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)  # Set a seed for reproducibility
    def test_normal_case(self):
        # Test with a normal DataFrame
        df = pd.DataFrame({'A': np.random.randint(0, 100, 100),
                           'B': np.random.randint(0, 100, 100),
                           'C': np.random.choice([900, 800], 100)})
        predictions, model = task_func(df, seed=12)
        self.assertIsInstance(model, LinearRegression)
        np.testing.assert_almost_equal(predictions, np.array([73.84, 73.74, 73.02, 73.32, 72.66]), decimal=2)
    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame()
        predictions = task_func(df)
        self.assertIsNone(predictions)
    def test_missing_columns(self):
        # Test with a DataFrame missing one or more columns
        df = pd.DataFrame({'A': np.random.randint(0, 100, 100),
                           'C': np.random.choice([900, 800], 100)})
        predictions = task_func(df)
        self.assertIsNone(predictions)
    def test_non_numeric_data(self):
        # Test with non-numeric data
        df = pd.DataFrame({'A': ['a', 'b', 'c'],
                           'B': [1, 2, 3],
                           'C': [900, 900, 900]})
        predictions = task_func(df)
        self.assertIsNone(predictions)
    def test_no_rows_matching_criteria(self):
        # Test with no rows matching the criteria
        df = pd.DataFrame({'A': np.random.randint(0, 100, 100),
                           'B': np.random.randint(0, 50, 100),  # B values are always < 50
                           'C': np.random.choice([800, 700], 100)})  # C values are never 900
        predictions = task_func(df)
        self.assertIsNone(predictions)
    def test_large_dataset_performance(self):
        # Test with a very large DataFrame (performance test)
        df = pd.DataFrame({'test': np.random.randint(0, 100, 10000),
                           'hi': np.random.randint(0, 100, 10000),
                           'hello': np.random.choice([900, 800], 10000)})
        predictions, model = task_func(df, col_a='test', col_b='hi', col_c='hello')
        self.assertIsInstance(model, LinearRegression)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions), 500)
    def test_single_value_column(self):
        # Test with a DataFrame where one column has the same value
        df = pd.DataFrame({'A': [50] * 100,
                           'B': np.random.randint(50, 100, 100),
                           'C': [900] * 100})
        predictions, model = task_func(df, seed=1)
        self.assertIsInstance(model, LinearRegression)
        np.testing.assert_almost_equal(
            predictions,
            np.array([73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61, 73.61]),
            decimal=2
            )
    def test_specific_return_values(self):
        # Test with known data to check specific return values
        df = pd.DataFrame({'A': [10, 20, 30, 40, 50],
                           'B': [60, 70, 80, 90, 100],
                           'C': [900, 900, 900, 900, 900]})
        predictions, model = task_func(df, seed=100)
        # Since the data is linear and simple, the model should predict close to the actual values
        expected_predictions = np.array([70])  # Assuming a perfect model
        np.testing.assert_almost_equal(predictions, expected_predictions)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)