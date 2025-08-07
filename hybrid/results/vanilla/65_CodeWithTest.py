import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the list of elements
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group by all columns except the last one and aggregate the last column
    grouped_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].sum().reset_index()
    
    # Create a line chart
    fig, ax = plt.subplots()
    for name, group in grouped_df.groupby(COLUMNS[:-1]):
        ax.plot(group.index, group[COLUMNS[-1]], marker='o', label=str(name))
    
    # Set the x-label and y-label
    x_label = '-'.join(COLUMNS[:-1])
    y_label = COLUMNS[-1]
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Add a legend
    ax.legend(title='-'.join(COLUMNS[:-1]))
    
    # Show the plot
    plt.show()
    
    return grouped_df, ax

# Example usage:
# data = [
#     ['A', 'X', 10],
#     ['A', 'X', 20],
#     ['B', 'Y', 15],
#     ['B', 'Y', 25]
# ]
# df, ax = task_func(data)
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        # Using the provided example as the first test case
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        analyzed_df, ax = task_func(data)
        # Assertions for the returned DataFrame
        expected_data = [[1, 1, 2], [1, 2, 1], [2, 1, 3], [2, 2, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        # Assertions for the returned plot
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [2, 1, 3, 1])
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
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [3, 1, 1])
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
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [1, 1, 1, 1])
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
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [1])
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
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)