import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset from the CSV file
    df = pd.read_csv(data_path)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data using the scaler
    # Assuming all columns need to be normalized
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)
    
    return df_normalized
import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Create data
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        # Run function
        df = task_func('data.csv')
        # Check result
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 1)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 1)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 1)
        # Remove data
        os.remove('data.csv')
    def test_case_2(self):
        # Create data
        data = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        # Run function
        df = task_func('data.csv')
        # Check result
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 0)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 0)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 0)
        # Remove data
        os.remove('data.csv')
    def test_case_3(self):
        # Create data
        data = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        # Run function
        df = task_func('data.csv')
        # Check result
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 0)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 0)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 0)
        # Remove data
        os.remove('data.csv')
    def test_case_4(self):
        # Create data
        data = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        # Run function
        df = task_func('data.csv')
        # Check result
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 1)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 1)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 1)
        # Remove data
        os.remove('data.csv')
    def test_case_5(self):
        # Create data
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        # Run function
        df = task_func('data.csv')
        # Check result
        self.assertEqual(df.shape, (2, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 1)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 1)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 1)
        # Remove data
        os.remove('data.csv')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)