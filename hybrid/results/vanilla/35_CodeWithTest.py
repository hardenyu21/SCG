import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, target_values=[1, 3, 4]):
    # Replace elements not in target_values with zeros
    for column in df.columns:
        df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Create a figure and axes for plotting
    fig, axes = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(8, 4 * len(df.columns)))
    
    # Plot the distribution of each column
    for i, column in enumerate(df.columns):
        sns.countplot(data=df, x=column, ax=axes[i])
        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Count')
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the Axes object
    return axes

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [3, 4, 5, 6, 7],
#     'C': [1, 3, 4, 5, 6]
# })
# task_func(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame({"A": [1, 4, 7, 6, 7, 3, 4, 4]})
        df1, ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [7, 4, 3, 3, 1]})
        df1, ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)
    def test_case_3(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        target_values = [1, 2, 3, 4, 5]
        df1, ax = task_func(df, target_values=target_values)
        mask = df1.isin(target_values) | (df1 == 0)
        self.assertTrue(mask.all().all())
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        df = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [50, 40, 10, 10, 30]})
        target_values = [10, 20, 30]
        df1, ax = task_func(df, target_values=target_values)
        mask = df1.isin(target_values) | (df1 == 0)
        self.assertTrue(mask.all().all())
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)
    def test_case_5(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        df1, ax = task_func(df, target_values=[])
        self.assertTrue(df1.eq(0).all().all())
        self.assertIsInstance(ax, plt.Axes)
    def test_case_7(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        df1, ax = task_func(df, target_values=[5, 6, 2, 9, 7, 3, 8, 1])
        self.assertTrue(df1.equals(df))
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)