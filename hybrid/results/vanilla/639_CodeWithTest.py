import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(num_samples=100, num_features=5):
    # Generate a DataFrame with random values
    data = np.random.rand(num_samples, num_features)
    columns = [f'Feature_{i+1}' for i in range(num_features)]
    df = pd.DataFrame(data, columns=columns)
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Visualize the correlation matrix using a heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Heatmap')
    plt.show()
    
    return df, ax

# Example usage
df, ax = task_func()
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        df, ax = task_func()
        self.assertEqual(df.shape, (100, 5))
        self.assertIsInstance(ax, plt.Axes)
        
    def test_case_2(self):
        df, ax = task_func(10, 3)
        self.assertEqual(df.shape, (10, 3))
        self.assertIsInstance(ax, plt.Axes)
    def test_case_3(self):
        df, ax = task_func(50, 2)
        self.assertEqual(df.shape, (50, 2))
        self.assertIsInstance(ax, plt.Axes)
        
    def test_case_4(self):
        df, ax = task_func(150, 6)
        self.assertEqual(df.shape, (150, 6))
        self.assertIsInstance(ax, plt.Axes)
        
    def test_case_5(self):
        df, ax = task_func(5, 10)
        self.assertEqual(df.shape, (5, 10))
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)