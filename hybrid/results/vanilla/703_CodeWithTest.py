import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Transform the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Initialize the DBSCAN model with the specified parameters
    dbscan = DBSCAN(eps=3, min_samples=2)
    
    # Fit the model and predict the clusters
    df['Cluster'] = dbscan.fit_predict(df)
    
    return df
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func([[5.1, 3.5], [4.9, 3.0], [4.7, 3.2]], ['x', 'y'])
        print(df)
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0])))
    def test_case_2(self):
        df = task_func([[1, 2], [3, 4], [5, 6]], ['x', 'y'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0])))
    def test_case_3(self):
        df = task_func([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]], ['x', 'y'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0, 1, 1, -1])))
    def test_case_4(self):
        df = task_func([[1, 2, 3], [2, 2, 2], [2, 3, 4], [8, 7, 6], [8, 8, 8], [25, 80, 100]], ['x', 'y', 'z'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0, 1, 1, -1])))
    def test_case_5(self):
        df = task_func([[-1, -2], [-2, -2], [-2, -3], [-8, -7], [-8, -8], [-25, -80]], ['x', 'y'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0, 1, 1, -1])))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)