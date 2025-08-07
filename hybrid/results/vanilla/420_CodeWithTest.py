import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        try:
            # Try to convert the column to float
            df[column] = df[column].astype(float)
            # Scale the column if it is numeric
            df[column] = scaler.fit_transform(df[[column]])
        except ValueError:
            # If conversion to float fails, leave the column unchanged
            continue
    
    return df
import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        """Test the correctness of the scaling applied by the function."""
        # Creating a sample dataframe with three numeric columns
        data = {
                "a": [10.5, 23.4, 15.6, 78.9],
                "b": [45.6, 67.8, 89.0, 12.3],
                "c": [12.3, 45.6, 78.9, 0.1],
            }
        df = pd.DataFrame(
            data
        )
        result = task_func(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
    def test_case_2(self):
        """Test with an empty DataFrame."""
        # Creating an empty dataframe
        data = {}
        df = pd.DataFrame(data)
        result = task_func(data)
        # Ensuring the result is also an empty dataframe
        self.assertTrue(result.empty)
    def test_case_3(self):
        """Test with a DataFrame that doesn't have any columns to scale."""
        # Creating a dataframe with a single non-numeric column
        data = {"c": ["foo", "bar"]}
        df = pd.DataFrame(data)
        result = task_func(data)
        # Ensuring the output dataframe is unchanged
        pd.testing.assert_frame_equal(result, df, check_dtype=False)
    def test_case_4(self):
        """Test with a DataFrame where all columns are to be scaled."""
        # Creating a dataframe with two numeric columns
        data = {"a": [10.5, 23.4, 15.6, 78.9], "b": [45.6, 67.8, 89.0, 12.3]}
        df = pd.DataFrame(
            data
        )
        result = task_func(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
    def test_case_5(self):
        """Test with a DataFrame with single rows."""
        # Creating a dataframe with a single row and three columns
        data = {"a": [5.5], "b": [8.6], "c": [7.7]}
        df = pd.DataFrame(data)
        result = task_func(data)
        self.assertDictEqual(result.to_dict(), {'a': {0: 0.0}, 'b': {0: 0.0}, 'c': {0: 0.0}})
    def test_case_6(self):
        """Test with a DataFrame with mixed datatypes."""
        # Creating a dataframe with mixed data types (both floats and strings) in columns
        data = {
                "a": [10.5, 23.4, 15.6, "78.9"],
                "b": [45.6, "67.8", 89.0, 12.3],
                "c": [12.3, 45.6, 78.9, "0.1"],
            }
        df = pd.DataFrame(
            data
        )
        result = task_func(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
    def test_case_7(self):
        """Test with a DataFrame with negative values."""
        # Creating a dataframe with negative values in columns
        data = {"a": [-1, -2, -3, -4], "b": [-4, -5, -6, -7], "c": [-7, -8, -9, -10]}
        df = pd.DataFrame(
            data
        )
        result = task_func(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)