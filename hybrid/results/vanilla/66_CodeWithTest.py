import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Step 1: Build a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Step 2: Group the values in the column 'col3' by ['col1', 'col2']
    grouped_df = df.groupby(['col1', 'col2'])['col3'].mean().reset_index()
    
    # Step 3: Reset the index of the newly created dataframe
    grouped_df = grouped_df.reset_index(drop=True)
    
    # Step 4: Create a distribution plot of the 'col3' column
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(grouped_df['col3'], kde=True)
    ax.set_xlabel('col3')
    
    # Return the DataFrame and the plot object
    return grouped_df, ax

# Example usage:
# data = [[1, 'A', 10], [1, 'A', 15], [2, 'B', 20], [2, 'B', 25]]
# df, ax = task_func(data)
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        analyzed_df, plot = task_func(data)
        # Asserting the analyzed DataFrame
        expected_df = pd.DataFrame({
            'col1': [1, 1, 2, 2],
            'col2': [1, 2, 1, 2],
            'col3': [2, 1, 3, 1]
        })
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        # Asserting plot attributes (e.g., title, x-axis, y-axis)
        self.assertEqual(plot.get_xlabel(), 'col3')
    def test_case_2(self):
        # Testing with a different dataset
        data = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
        analyzed_df, plot = task_func(data)
        # Asserting the analyzed DataFrame
        expected_df = pd.DataFrame({
            'col1': [1, 1],
            'col2': [1, 2],
            'col3': [3, 1]
        })
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')
    def test_case_3(self):
        data = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [6, 7, 8]]
        analyzed_df, plot = task_func(data)
        # Asserting the analyzed DataFrame
        expected_df = pd.DataFrame({
            'col1': [1, 6],
            'col2': [2, 7],
            'col3': [3, 1]
        })
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')
    def test_case_4(self):
        data = [
            [0, 0, 1],
            [0, 0, 4],
            [0, 1, 1],
            [0, 1, 7],
            [1, 0, 0],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        analyzed_df, plot = task_func(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 1],
            [1, 1, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')
    def test_case_5(self):
        data = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        analyzed_df, plot = task_func(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 2],
            [1, 1, 2]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)