import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)
    
    # Calculate statistics for each array
    mean1 = np.mean(array1)
    median1 = np.median(array1)
    std_dev1 = np.std(array1)
    
    mean2 = np.mean(array2)
    median2 = np.median(array2)
    std_dev2 = np.std(array2)
    
    # Create a DataFrame to store the statistics
    statistics = pd.DataFrame({
        'Array1': [mean1, median1, std_dev1],
        'Array2': [mean2, median2, std_dev2]
    }, index=['Mean', 'Median', 'Standard Deviation'])
    
    # Plot a bar chart to compare the statistics
    ax = statistics.plot(kind='bar', figsize=(10, 6))
    ax.set_title('Comparison of Statistics for Two Random Arrays')
    ax.set_ylabel('Value')
    ax.set_xlabel('Statistics')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
    return statistics, ax

# Example usage
df, ax = task_func(100)
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    
    def test_default_length(self):
        df, ax = task_func()
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(all(df.index == ['Mean', 'Median', 'Standard Deviation']))
        self.assertTrue(all(df.columns == ['Array1', 'Array2']))
        self.assertIsInstance(ax, plt.Axes)
    
    def test_custom_length(self):
        df, ax = task_func(200)
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(all(df.index == ['Mean', 'Median', 'Standard Deviation']))
        self.assertTrue(all(df.columns == ['Array1', 'Array2']))
        self.assertIsInstance(ax, plt.Axes)
    
    def test_statistics_values(self):
        np.random.seed(42)  # Setting seed for reproducibility
        df, _ = task_func(1000)
        self.assertAlmostEqual(df['Array1']['Mean'], 0.4903, places=3)
        self.assertAlmostEqual(df['Array2']['Mean'], 0.5068, places=3)
        self.assertAlmostEqual(df['Array1']['Median'], 0.4968, places=3)
        self.assertAlmostEqual(df['Array2']['Median'], 0.5187, places=3)
        self.assertAlmostEqual(df['Array1']['Standard Deviation'], 0.2920, places=3)
        self.assertAlmostEqual(df['Array2']['Standard Deviation'], 0.2921, places=3)
    
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            task_func(-50)
    
    def test_zero_length(self):
        df, ax = task_func(0)
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(all(df.index == ['Mean', 'Median', 'Standard Deviation']))
        self.assertTrue(all(df.columns == ['Array1', 'Array2']))
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)