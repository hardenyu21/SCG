import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    # Convert the list of tuples into a DataFrame
    df = pd.DataFrame(tuples_list, columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled data
    df_scaled = pd.DataFrame(scaled_data, columns=columns)
    
    return df_scaled
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['A'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_2(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['B'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_3(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['C'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_4(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['D'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_5(self):
        df = task_func([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['A'].tolist(), [0.0, 0.0, 0.0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)