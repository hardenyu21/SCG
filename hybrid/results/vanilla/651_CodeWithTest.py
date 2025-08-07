import pandas as pd
import matplotlib.pyplot as plt

def task_func(input_dict, target_value):
    # Convert the input dictionary of lists to a DataFrame
    df = pd.DataFrame(input_dict)
    
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None
    
    # Search for rows with cells equal to the provided target_value
    target_rows = df[df == target_value]
    
    # Count the occurrences of the target value per column
    counts = target_rows.count()
    
    # Plot the counts of such rows per column
    ax = counts.plot(kind='bar', title=f'Count of {target_value} per Column')
    ax.set_ylabel('Count')
    ax.set_xlabel('Columns')
    
    # Show the plot
    plt.show()
    
    return counts, ax

# Example usage:
# input_dict = {'A': [1, 2, 3, 4], 'B': [2, 3, 4, 5], 'C': [3, 4, 5, 6]}
# target_value = 3
# counts, ax = task_func(input_dict, target_value)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test case with default example data
        df = {
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 1)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 1)
    def test_case_2(self):
        # Test case with no occurrences of the target value
        df = {
            'Column1': ['0', 'a', '331', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '331']
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 0)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 0)
    def test_case_3(self):
        # Test case with multiple occurrences of the target value in a single column
        df = {
            'Column1': ['332', 'a', '332', '33'],
            'Column2': ['1', '332', '332', '22'],
            'Column3': ['2', '332', '2', '332']
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 2)
        self.assertEqual(counts['Column2'], 2)
        self.assertEqual(counts['Column3'], 2)
    def test_case_4(self):
        # Test case with an empty DataFrame
        df = pd.DataFrame()
        counts, ax = task_func(df, '332')
        self.assertEqual(len(counts), 0)
    def test_case_5(self):
        # Test case with different data types in the DataFrame
        df = {
            'Column1': [0, 'a', 332, '33'],
            'Column2': [1.0, 'bb', 33.0, 22.2],
            'Column3': [2, 'ccc', 2, 332]
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 1)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)