import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000

def task_func():
    # Generate random integers for 'X' and 'Y' columns
    data = {
        'X': np.random.randint(0, RANGE, SIZE),
        'Y': np.random.randint(0, RANGE, SIZE)
    }
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    # Plot the data using Seaborn
    sns.scatterplot(x='X', y='Y', data=df)
    plt.title('Scatter Plot of Random Integers')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    # Return the DataFrame
    return df

# Call the function to execute the task
task_func()
import unittest
class TestCases(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (SIZE, 2))
    def test_random_range(self):
        """Test that the random numbers fall within the specified range."""
        df = task_func()
        self.assertTrue(df['X'].between(0, RANGE-1).all())
        self.assertTrue(df['Y'].between(0, RANGE-1).all())
    def test_columns_existence(self):
        """Ensure both 'X' and 'Y' columns exist."""
        df = task_func()
        self.assertIn('X', df.columns)
        self.assertIn('Y', df.columns)
    def test_non_empty_dataframe(self):
        """Check that the DataFrame is not empty."""
        df = task_func()
        self.assertFalse(df.empty)
    def test_columns_type(self):
        """Test that 'X' and 'Y' columns are of integer type."""
        df = task_func()
        self.assertTrue(np.issubdtype(df['X'].dtype, np.integer))
        self.assertTrue(np.issubdtype(df['Y'].dtype, np.integer))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)