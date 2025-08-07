import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Flatten the tuple and convert elements to integers
    flat_list = list(itertools.chain.from_iterable(T1))
    int_list = [int(x) for x in flat_list]
    
    # Calculate the number of columns based on the sum of integers
    num_columns = sum(int_list)
    
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random numbers and create a DataFrame
    data = np.random.randint(0, 100, size=(row_num, num_columns))
    column_names = [f'Col_{i+1}' for i in range(num_columns)]
    df = pd.DataFrame(data, columns=column_names)
    
    return df
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_rng(self):
        T1 = (('13', '17', '18', '21', '32'))
        df1 = task_func(T1, row_num=50, seed=2022)
        df2 = task_func(T1, row_num=50, seed=2022)
        pd.testing.assert_frame_equal(df1, df2)
        df4 = task_func(T1, row_num=50, seed=12)
        try:
            pd.testing.assert_frame_equal(df1, df4)
        except AssertionError:
            pass
        else:
            raise AssertionError('frames are equal but should not be')
    def test_case_1(self):
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([13, 17, 18, 21, 32, 7, 11, 13, 14, 28, 1, 5, 6, 8, 15, 16])))
    def test_case_2(self):
        T1 = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    def test_case_3(self):
        T1 = (('10', '20', '30'), ('40', '50', '60'), ('70', '80', '90'))
        df = task_func(T1, row_num=70, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (70, sum([10, 20, 30, 40, 50, 60, 70, 80, 90])))
    def test_case_4(self):
        T1 = ()
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, 0))
    def test_case_5(self):
        T1 = (('1', '2', '3'), (), ('7', '8', '9'))
        df = task_func(T1, row_num=50, seed=21)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([1, 2, 3, 7, 8, 9])))
    def test_non_int(self):
        a = (('1', '2.45'))
        self.assertRaises(Exception, task_func, a, 120, 21)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)