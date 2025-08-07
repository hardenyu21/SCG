import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    euclidean_dist = distance.euclidean(a, b)
    
    # Create a Pandas DataFrame from the lists with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Plot the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    df.plot(ax=ax, marker='o')
    ax.set_title(f'Euclidean Distance: {euclidean_dist:.2f}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    # Return the computed distance, DataFrame, and Axes object
    return euclidean_dist, df, ax

# Example usage:
# a = [1, 2, 3]
# b = [4, 5, 6]
# dist, df, ax = task_func(a, b)
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 1.732, places=3)
        self.assertTrue('A' in df.columns)
        self.assertTrue('B' in df.columns)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_2(self):
        a = [1, 1, 1]
        b = [1, 1, 1]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertEqual(euclidean_distance, 0)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_3(self):
        a = [0, 5, 10]
        b = [10, 5, 0]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 14.142, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_4(self):
        a = [3, 3, 3, 3]
        b = [4, 4, 4, 4]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 2.0, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_5(self):
        a = [1, 2, 3, 4, 5]
        b = [5, 4, 3, 2, 1]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 6.325, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)