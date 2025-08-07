import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    # Define the categories for the stacked bar chart
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    
    # Check if the number of columns exceeds the number of available categories
    if cols > len(categories):
        raise ValueError("The number of columns exceeds the number of available categories.")
    
    # Generate random numerical data
    data = np.random.rand(rows, cols)
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=categories[:cols])
    
    # Plot the stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart of Random Data')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func(rows=5, cols=3)
import unittest
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def tearDown(self):
        # Cleanup any opened figures in matplotlib
        plt.close('all')
    def test_case_1(self):
        ax = task_func(5, 5)
        self.assertEqual(len(ax.patches), 25)  # 5 bars with 5 segments each, each segment represents a stacked part
    def test_case_2(self):
        ax = task_func(7, 3)
        self.assertEqual(len(ax.patches), 21)  # 7 bars with 3 segments each
    def test_case_3(self):
        ax = task_func(10, 2)
        self.assertEqual(len(ax.patches), 20)  # 10 bars with 2 segments each
    def test_case_4(self):
        with self.assertRaises(ValueError):  # Testing for more columns than categories
            ax = task_func(5, 6)
    def test_case_5(self):
        ax = task_func(3, 1)
        self.assertEqual(len(ax.patches), 3)  # 3 bars with 1 segment each


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)