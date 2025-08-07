import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Calculate the correlation matrix
    corr_matrix = data.corr()
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    
    # Set the title of the heatmap
    ax.set_title('Correlation Matrix')
    
    # Return the Axes object
    return ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [5, 4, 3, 2, 1],
#     'C': [2, 3, 4, 5, 6]
# })
# ax = task_func(df)
# plt.show()
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_2(self):
        data = {'a': [1, 2, 3], 'b': [-4, -5, -6], 'c': [-7, -8, -9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_3(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [-7, -8, -9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_4(self):
        data = {'a': [1, 1, 1], 'b': [2, 2, 2], 'c': [3, 3, 3]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_5(self):
        data = {'a': [1, 2, None], 'b': [4, None, 6], 'c': [None, 8, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)