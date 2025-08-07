import pandas as pd
import numpy as np

def task_func(df, col):
    """
    Process a Pandas DataFrame by removing a specific column and adding a 'IsEvenIndex' column.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    col (str): The name of the column to be removed.
    
    Returns:
    pd.DataFrame: The processed DataFrame with the specified column removed and a new 'IsEvenIndex' column added.
    """
    # Remove the specified column
    if col in df.columns:
        df = df.drop(columns=[col])
    
    # Add 'IsEvenIndex' column
    df['IsEvenIndex'] = df.index % 2 == 0
    
    return df
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'A')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('A' in df.columns)
    def test_case_2(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'B')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('B' in df.columns)
    def test_case_3(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'C')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('C' in df.columns)
    def test_case_4(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'D')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('D' in df.columns)
    def test_case_5(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = task_func(df, 'A')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('A' in df.columns)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)