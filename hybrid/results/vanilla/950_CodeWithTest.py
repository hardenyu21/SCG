import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a matrix of random values with specified dimensions
    matrix = np.random.rand(rows, columns)
    
    # Perform Singular Value Decomposition (SVD)
    U, s, Vh = svd(matrix)
    
    # Return the results as a tuple
    return U, s, Vh

# Example usage:
# U, s, Vh = task_func(3, 2, 0)
# print("U:\n", U)
# print("s:\n", s)
# print("Vh:\n", Vh)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with default 3x2 matrix
        U, s, Vh = task_func(seed=3)
        self.assertEqual(U.shape, (3, 3))
        self.assertEqual(s.shape, (2,))
        self.assertEqual(Vh.shape, (2, 2))
        self.assertTrue(np.all(s >= 0))
        
    def test_case_2(self):
        # Test with a 5x5 square matrix
        U, s, Vh = task_func(5, 5, seed=42)
        self.assertEqual(U.shape, (5, 5))
        self.assertEqual(s.shape, (5,))
        self.assertEqual(Vh.shape, (5, 5))
        self.assertTrue(np.all(s >= 0))
    
    def test_case_3(self):
        # Test with a 2x3 matrix (more columns than rows)
        U, s, Vh = task_func(2, 3, seed=12)
        self.assertEqual(U.shape, (2, 2))
        self.assertEqual(s.shape, (2,))
        self.assertEqual(Vh.shape, (3, 3))
        self.assertTrue(np.all(s >= 0))
        
    def test_case_4(self):
        # Test with a 1x1 matrix (a scalar)
        U, s, Vh = task_func(1, 1, seed=0)
        self.assertEqual(U.shape, (1, 1))
        self.assertEqual(s.shape, (1,))
        self.assertEqual(Vh.shape, (1, 1))
        self.assertTrue(np.all(s >= 0))
        
    def test_case_5(self):
        # Test with a 4x3 matrix
        U, s, Vh = task_func(4, 3, seed=1)
        self.assertEqual(U.shape, (4, 4))
        self.assertEqual(s.shape, (3,))
        self.assertEqual(Vh.shape, (3, 3))
        self.assertTrue(np.all(s >= 0))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)