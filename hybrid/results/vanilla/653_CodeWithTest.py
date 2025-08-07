import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    bool_df = dataframe == target_value
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(bool_df, cmap='viridis', cbar=False)
    
    # Set the title of the heatmap
    ax.set_title(f'Heatmap of occurrences of target value: {target_value}')
    
    # Show the plot
    plt.show()
    
    # Return the Boolean DataFrame and the Axes object
    return bool_df, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 332, 4],
#     'B': [332, 5, 6, 7],
#     'C': [8, 9, 10, 332]
# })
# bool_df, ax = task_func(df, target_value=332)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        """Create a sample DataFrame for testing."""
        self.df = pd.DataFrame({
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        })
    def test_target_value_occurrence(self):
        """Test if the function correctly identifies the target value."""
        mask, _ = task_func(self.df, '332')
        self.assertTrue(mask.iloc[2, 0], "Mask should be True where target value '332' exists.")
    def test_target_value_absence(self):
        """Test if the function correctly identifies absence of the target value."""
        mask, _ = task_func(self.df, '332')
        self.assertFalse(mask.iloc[0, 0], "Mask should be False where target value '332' does not exist.")
    def test_return_type(self):
        """Test the return type of the function."""
        mask, ax = task_func(self.df, '332')
        self.assertIsInstance(mask, pd.DataFrame, "First return value should be a DataFrame.")
        self.assertTrue(hasattr(ax, 'get_figure'), "Second return value should be an Axes object with a 'get_figure' method.")
    def test_default_target_value(self):
        """Test the function with the default target value."""
        mask, _ = task_func(self.df)
        self.assertEqual(mask.sum().sum(), 2, "There should be exactly 2 occurrences of the default target value '332'.")
    def test_custom_target_value(self):
        """Test the function with a custom target value."""
        mask, _ = task_func(self.df, 'a')
        self.assertEqual(mask.sum().sum(), 1, "There should be exactly 1 occurrence of the custom target value 'a'.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)