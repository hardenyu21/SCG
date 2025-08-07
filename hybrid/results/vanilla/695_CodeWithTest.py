import numpy as np
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    # Convert the list of tuples into a numpy array
    data = np.array(tuples_list)
    
    # Initialize PCA with the specified number of components
    pca = PCA(n_components=n_components)
    
    # Fit PCA on the data and transform it
    transformed_data = pca.fit_transform(data)
    
    return transformed_data
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        transformed_data = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 2)
        self.assertEqual(transformed_data.shape, (3, 2))
    def test_case_2(self):
        transformed_data = task_func([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 2)
        self.assertEqual(transformed_data.shape, (3, 2))
        self.assertTrue(np.all(transformed_data == 0))
    def test_case_3(self):
        transformed_data = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 3)
        self.assertEqual(transformed_data.shape, (3, 3))
    def test_case_4(self):
        transformed_data = task_func([(0, 1)], 1)
        self.assertEqual(transformed_data.shape, (1, 1))
        self.assertTrue(np.all(transformed_data == 0))
    def test_case_5(self):
        transformed_data = task_func([(-1, -1, -1), (0, 0, 0), (1, 1, 1)], 1)
        self.assertEqual(transformed_data.shape, (3, 1))
        self.assertTrue(transformed_data[1][0] == 0)
        try:
            self.assertTrue(transformed_data[0][0] < 0)
            self.assertTrue(transformed_data[2][0] > 0)
        except:
            self.assertTrue(transformed_data[0][0] > 0)
            self.assertTrue(transformed_data[2][0] < 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)