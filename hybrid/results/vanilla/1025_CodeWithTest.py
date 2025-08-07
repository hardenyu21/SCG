import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    # Plot the scaled data
    ax = scaled_df.plot(kind='line', title=PLOT_TITLE)
    ax.set_xlabel('Index')
    ax.set_ylabel('Scaled Value')
    plt.grid(True)
    plt.show()
    
    # Return the scaled DataFrame and the Axes object
    return scaled_df, ax

# Example usage:
# data_dict = {'feature1': [1, 2, 3, 4, 5], 'feature2': [5, 4, 3, 2, 1]}
# scaled_df, ax = task_func(data_dict)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Unit tests for the function."""
    def test_empty_data(self):
        """
        Test with an empty dictionary. Should return an empty DataFrame and a plot object.
        """
        result_df, result_ax = task_func({})
        self.assertTrue(result_df.empty)
        self.assertIsNotNone(result_ax)
    def test_all_none_data(self):
        """
        Test with a dictionary where all values are None. Should return an empty DataFrame and a plot object.
        """
        data = {"a": [None, None], "b": [None, None]}
        result_df, result_ax = task_func(data)
        self.assertTrue(result_df.empty)
        self.assertIsNotNone(result_ax)
    def test_normal_data(self):
        """
        Test with a normal data dictionary. Should return a non-empty DataFrame and a plot object.
        """
        data = {"a": [1, 2, 3], "b": [4, 5, 6]}
        result_df, result_ax = task_func(data)
        self.assertEqual(result_ax.get_title(), "Scaled Values")
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape, (3, 2))
        self.assertIsNotNone(result_ax)
    def test_with_missing_values(self):
        """
        Test data with some missing values. Missing values should be dropped, and scaled data should be returned.
        """
        data = {"a": [1, None, 3], "b": [4, 5, None]}
        result_df, result_ax = task_func(data)
        self.assertEqual(result_df.shape, (1, 2))  # Only one row without missing values
        self.assertIsNotNone(result_ax)
    def test_with_negative_values(self):
        """
        Test data with negative values. Should handle negative values correctly and return scaled data.
        """
        data = {"a": [-1, -2, -3], "b": [1, 2, 3]}
        result_df, result_ax = task_func(data)
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape, (3, 2))
        self.assertIsNotNone(result_ax)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)