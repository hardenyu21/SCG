import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, col1, col2):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the specified columns exist in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"The DataFrame does not contain the specified columns: {col1} and/or {col2}.")
    
    # Check if the specified columns contain numeric data
    if not pd.api.types.is_numeric_dtype(df[col1]) or not pd.api.types.is_numeric_dtype(df[col2]):
        raise TypeError(f"The specified columns {col1} and/or {col2} contain non-numeric data.")
    
    # Create a scatter plot with a regression line
    ax = sns.lmplot(x=col1, y=col2, data=df, aspect=1.5, height=6)
    
    # Return the seaborn axes object
    return ax.axes[0, 0]

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 3, 5, 7, 11]
# })
# ax = task_func(df, 'A', 'B')
# plt.show()
import unittest
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_numeric_data(self):
        # Create a DataFrame with numeric data
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1]
        })
        # Call the function with the DataFrame
        ax = task_func(df, 'A', 'B')
        
        # Assertions to validate the output
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        plt.close()
    def test_non_numeric_data(self):
        # Create a DataFrame with non-numeric data
        df = pd.DataFrame({
            'A': ['one', 'two', 'three', 'four', 'five'],
            'B': ['five', 'four', 'three', 'two', 'one']
        })
        # We expect a TypeError because non-numeric data can't be used to plot a regression line
        with self.assertRaises(TypeError, msg="The function should raise a TypeError for non-numeric data."):
            task_func(df, 'A', 'B')
        plt.close()
    def test_missing_data(self):
        # Create a DataFrame with missing data
        df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [5, None, 3, 2, 1]
        })
        # Call the function with the DataFrame
        ax = task_func(df, 'A', 'B')
        # Assertions to validate the output
        # We expect the function to handle missing data according to seaborn's default behavior
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        # Check if the data plotted is the same length as the original minus the NaNs
        non_na_length = df.dropna().shape[0]
        self.assertEqual(len(ax.collections[0].get_offsets().data), non_na_length)  # Check if there's only one data point in the collection
        plt.close()
    def test_large_dataset(self):
        # Create a large DataFrame
        df = pd.DataFrame({
            'A': range(10000),
            'B': range(10000, 20000)
        })
        # Call the function with the DataFrame
        ax = task_func(df, 'A', 'B')
        # Assertions to validate the output
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        plt.close()
    def test_single_data_point(self):
        # Create a DataFrame with a single data point
        df = pd.DataFrame({
            'A': [1],
            'B': [1]
        })
        # Call the function with the DataFrame
        ax = task_func(df, 'A', 'B')
        # Assertions to validate the output
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        self.assertEqual(len(ax.collections), 1)  # Check if there's only one collection of points in the plot
        self.assertEqual(len(ax.collections[0].get_offsets()), 1)  # Check if there's only one data point in the collection
        plt.close()
    
    def test_non_df(self):
        with self.assertRaises(ValueError):
            task_func("non_df", 'A', 'B')
    
    def test_empty_df(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame(), 'A', 'B')
    def test_column_df(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'A': [1]}), 'A', 'B')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)