import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random values for the DataFrame
    data = np.random.randint(0, 100, size=(n_rows, len(columns)))
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Check if there are any columns to scale
    if scale_cols:
        # Initialize the StandardScaler
        scaler = StandardScaler()
        
        # Scale the specified columns
        df.iloc[:, scale_cols] = scaler.fit_transform(df.iloc[:, scale_cols])
    
    return df

# Example usage
df = task_func(5, [1, 2, 3], random_seed=12)
print(df)
import unittest
import pandas as pd
from sklearn.preprocessing import StandardScaler
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func(10, [0], random_seed=42)
        self.assertEqual(len(df), 10)
        self.assertEqual(list(df.columns), ['A', 'B', 'C', 'D', 'E'])
        self.assertAlmostEqual(df['A'].mean(), 0.0, delta=0.2)
        self.assertAlmostEqual(df['A'].std(), 1.0, delta=0.5)
        expected = pd.DataFrame({
            'A': {0: -0.20549386391116023,
              1: -1.343049181990797,
              2: 1.1155381183748696,
              3: -0.16879853106988163,
              4: -2.0402605059750907,
             5: 0.6751941242795263,
             6: 1.2256241168987054,
             7: 0.8219754556446407,
             8: 0.16145946450162582,
             9: -0.24218919675243883},
            'B': {0: 92, 1: 82, 2: 99, 3: 1, 4: 63, 5: 57, 6: 58, 7: 14, 8: 50, 9: 6},
            'C': {0: 14, 1: 86, 2: 23, 3: 87, 4: 59, 5: 21, 6: 41, 7: 61, 8: 54, 9: 20},
            'D': {0: 71, 1: 74, 2: 2, 3: 29, 4: 20, 5: 88, 6: 91, 7: 61, 8: 63, 9: 72},
            'E': {0: 60, 1: 74, 2: 21, 3: 37, 4: 32, 5: 48, 6: 59, 7: 46, 8: 2, 9: 38}}
        )
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)
    def test_case_2(self):
        df = task_func(500, [1, 3], random_seed=1)
        self.assertEqual(len(df), 500)
        self.assertAlmostEqual(df['B'].mean(), 0.0, places=5)
        self.assertAlmostEqual(df['B'].std(), 1.0, places=1)
        self.assertAlmostEqual(df['D'].mean(), 0.0, places=5)
        self.assertAlmostEqual(df['D'].std(), 1.0, places=1)
    def test_case_3(self):
        df = task_func(50, [])
        self.assertEqual(len(df), 50)
        self.assertNotEqual(df['A'].mean(), 0.0)
        self.assertNotEqual(df['A'].std(), 1.0)
    def test_case_4(self):
        df = task_func(200, [0, 1, 2, 3, 4])
        self.assertEqual(len(df), 200)
        for col in ['A', 'B', 'C', 'D', 'E']:
            self.assertAlmostEqual(df[col].mean(), 0.0, places=5)
            self.assertAlmostEqual(df[col].std(), 1.0, places=1)
    def test_case_5(self):
        df = task_func(1, [2])
        self.assertEqual(len(df), 1)
        self.assertEqual(df['C'].iloc[0], 0.0)
        # For a single-row DataFrame, the standard deviation will be NaN.
        self.assertTrue(pd.isna(df['C'].std()))
    def test_rng(self):
        df1 = task_func(50, [1, 2], random_seed=2)
        df2 = task_func(50, [1, 2], random_seed=2)
        pd.testing.assert_frame_equal(df1, df2)
    def test_custom_columns(self):
        df = task_func(10, [1], columns=['test', 'scale'], random_seed=12)
        expected = pd.DataFrame({
            'test': {0: 75, 1: 6, 2: 3, 3: 76, 4: 22, 5: 52, 6: 13, 7: 34, 8: 74, 9: 76},
            'scale': {0: -0.33880664428931573,
            1: -1.1454891306924484,
            2: 0.9518853339556965,
            3: 0.33880664428931573,
            4: 0.37107394374544106,
            5: -1.0486872323240726,
            6: 1.6617659219904533,
            7: 1.210023729604699,
            8: -1.210023729604699,
            9: -0.79054883667507}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)