import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def task_func(x, y, labels):
    # Create a DataFrame from the x and y values
    df = pd.DataFrame({'x': x, 'y': y})
    
    # Create a pivot table to prepare data for heatmap
    pivot_table = df.pivot_table(index='x', columns='y', aggfunc='size', fill_value=0)
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", xticklabels=labels, yticklabels=labels)
    
    # Set labels and title
    ax.set_xlabel('Y Values')
    ax.set_ylabel('X Values')
    ax.set_title('Heatmap of X vs Y')
    
    # Show the plot
    plt.show()
    
    return ax, df

# Example usage
x = np.random.randint(0, 5, 100)
y = np.random.randint(0, 5, 100)
ax, df = task_func(x, y, LABELS)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
        y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
        labels = ['H₂O', 'O₂', 'CO₂']
        ax, df = task_func(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (3, 6))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[1,2,3,4,5,6], [4,5,6,7,8,9], [7,8,9,10,11,12]])
        np.testing.assert_array_equal(df.values, expected_data)
    def test_case_2(self):
        x = [np.array([1,1]), np.array([2,2])]
        y = [np.array([3,3]), np.array([4,4])]
        labels = ['H₂O', 'O₂']
        ax, df = task_func(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (2, 4))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[1,1,3,3], [2,2,4,4]])
        np.testing.assert_array_equal(df.values, expected_data)
    def test_case_3(self):
        x = [np.array([10])]
        y = [np.array([20])]
        labels = ['H₂O']
        ax, df = task_func(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (1, 2))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[10, 20]])
        np.testing.assert_array_equal(df.values, expected_data)
    def test_case_4(self):
        x = [np.array([5,6,7]), np.array([8,9,10]), np.array([11,12,13])]
        y = [np.array([15,16,17]), np.array([18,19,20]), np.array([21,22,23])]
        labels = ['A', 'B', 'C']
        ax, df = task_func(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (3, 6))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[5,6,7,15,16,17], [8,9,10,18,19,20], [11,12,13,21,22,23]])
        np.testing.assert_array_equal(df.values, expected_data)
    def test_case_5(self):
        x = [np.array([2,3]), np.array([5,6])]
        y = [np.array([8,9]), np.array([11,12])]
        labels = ['X', 'Y']
        ax, df = task_func(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (2, 4))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[2,3,8,9], [5,6,11,12]])
        np.testing.assert_array_equal(df.values, expected_data)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)