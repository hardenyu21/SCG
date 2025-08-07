import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def task_func(df, dict_mapping, plot_histogram=False):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Check if FEATURES and TARGET are in the DataFrame
    missing_features = [feature for feature in FEATURES if feature not in df.columns]
    if missing_features:
        raise ValueError(f"Missing features in DataFrame: {missing_features}")
    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' is not in the DataFrame.")
    
    # Replace values according to dict_mapping
    df_replaced = df.replace(dict_mapping)
    
    # Standardize specified features
    scaler = StandardScaler()
    df_replaced[FEATURES] = scaler.fit_transform(df_replaced[FEATURES])
    
    # Plot histogram of the target variable if requested
    ax = None
    if plot_histogram:
        ax = df_replaced[TARGET].hist()
        plt.title('Histogram of Target Variable')
        plt.xlabel(TARGET)
        plt.ylabel('Frequency')
        plt.show()
    
    return df_replaced, ax
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_value_replacement(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        dict_mapping = {1: 11, 0: 22}
        result_df, _ = task_func(df, dict_mapping)
        self.assertTrue(11 in result_df.values)
        self.assertTrue(22 in result_df.values)
    def test_feature_standardization(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        result_df, _ = task_func(df, {})
        for feature in ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']:
            self.assertAlmostEqual(result_df[feature].mean(), 0, places=1)
            self.assertAlmostEqual(int(result_df[feature].std()), 1, places=1)
    def test_no_histogram_plotting(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        result, _ = task_func(df, {}, plot_histogram=False)
        self.assertIsInstance(result, pd.DataFrame)
    def test_missing_features_handling(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'target': [0, 1, 1]
        })
        with self.assertRaises(ValueError):
            task_func(df, {})
    def test_histogram_plotting(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        result_df, ax = task_func(df, {}, plot_histogram=True)
        self.assertTrue(hasattr(ax, 'hist'))
        self.assertIsInstance(ax, plt.Axes)
        plt.close()
    
    def test_non_df(self):
        with self.assertRaises(ValueError):
            task_func("non_df", {})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)