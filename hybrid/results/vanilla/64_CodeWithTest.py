import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Count the occurrences of each value in 'col3' grouped by 'col1' and 'col2'
    grouped_data = df.groupby(['col1', 'col2', 'col3']).size().unstack(fill_value=0)
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(grouped_data, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Count'})
    plt.title('Distribution of col3 values grouped by col1 and col2')
    plt.xlabel('col3')
    plt.ylabel('col1 and col2')
    
    # Return the DataFrame and the Axes object
    return grouped_data, ax

# Example usage:
# data = [
#     ['A', 'X', 1],
#     ['A', 'X', 2],
#     ['A', 'Y', 1],
#     ['B', 'X', 2],
#     ['B', 'Y', 1],
#     ['B', 'Y', 1]
# ]
# df, ax = task_func(data)
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = task_func(df)
        expected_data = [[1, 1, 2], [1, 2, 1], [2, 1, 3], [2, 2, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_2(self):
        data = [
            [1, 1, 2],
            [1, 1, 3],
            [1, 2, 4],
            [1, 1, 5],
            [1, 3, 7]
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [1, 1, 3],
            [1, 2, 1],
            [1, 3, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_3(self):
        data = [
            [1, 1, 1],
            [1, 2, 3],
            [2, 1, 4],
            [2, 2, 5]
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [1, 1, 1],
            [1, 2, 1],
            [2, 1, 1],
            [2, 2, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_4(self):
        data = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [1, 1, 1],
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
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
        analyzed_df, ax = task_func(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 2],
            [1, 1, 2]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)