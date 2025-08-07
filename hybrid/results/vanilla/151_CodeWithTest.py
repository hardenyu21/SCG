import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Check if any of the keys in data_keys are present in data_dict
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in `data_keys` are found in `data_dict`.")
    
    # Extract the data for the specified keys
    data = {key: data_dict[key] for key in data_keys if key in data_dict}
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(df)
    
    # Create a DataFrame with the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
    
    # Plot the normalized data
    ax = normalized_df.plot(kind='line', title='Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    
    # Show the plot
    plt.show()
    
    # Return the normalized DataFrame and the Axes object
    return normalized_df, ax
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Sample data dictionary
        self.data_dict = {
            'A': [10, 20, 30, 40],
            'B': [20, 30, 40, 50],
            'C': [30, 40, 50, 60]
        }
    def test_normalization_single_key(self):
        # Test normalization with a single key
        data_keys = ['A']
        normalized_df, ax = task_func(self.data_dict, data_keys)
        self.assertTrue((normalized_df >= 0).all().all() and (normalized_df <= 1).all().all(),
                        "Normalized data should be in the range [0, 1]")
    def test_normalization_multiple_keys(self):
        # Test normalization with multiple keys
        data_keys = ['A', 'B']
        normalized_df, ax = task_func(self.data_dict, data_keys)
        self.assertEqual(len(normalized_df.columns), 2, "Normalized DataFrame should have 2 columns")
        self.assertTrue({'A', 'B'}.issubset(normalized_df.columns), "DataFrame should contain specified keys")
    def test_normalization_all_keys(self):
        # Test normalization with all keys in the dictionary
        data_keys = list(self.data_dict.keys())
        normalized_df, ax = task_func(self.data_dict, data_keys)
        self.assertEqual(len(normalized_df.columns), 3, "Normalized DataFrame should have 3 columns")
        self.assertTrue({'A', 'B', 'C'}.issubset(normalized_df.columns), "DataFrame should contain all keys")
    def test_empty_keys(self):
        # Test with no keys specified
        data_keys = []
        with self.assertRaises(ValueError):
            task_func(self.data_dict, data_keys)
    def test_key_not_in_dict(self):
        # Test with a key that's not in the dictionary
        data_keys = ['D']  # Assuming 'D' is not in `data_dict`
        with self.assertRaises(ValueError):
            task_func(self.data_dict, data_keys)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)