import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(rows=3, columns=2, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a matrix of random values
    random_matrix = np.random.rand(rows, columns)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Reshape the matrix to fit the scaler's input requirements
    reshaped_matrix = random_matrix.reshape(-1, 1)
    
    # Scale the matrix
    scaled_matrix = scaler.fit_transform(reshaped_matrix)
    
    # Reshape back to the original matrix dimensions
    scaled_matrix = scaled_matrix.reshape(rows, columns)
    
    return scaled_matrix

# Example usage
print(task_func(2, 2))
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = task_func()
        self.assertEqual(result.shape, (3, 2))
        self.assertTrue(np.all(result >= 0))
    
    def test_case_2(self):
        result = task_func(2, 2)
        self.assertEqual(result.shape, (2, 2))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
        
    def test_case_3(self):
        result = task_func(4, 3)
        self.assertEqual(result.shape, (4, 3))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
    
    def test_case_4(self):
        result = task_func(5, 1)
        self.assertEqual(result.shape, (5, 1))
        self.assertTrue(np.all(result >= 0))
        
    def test_case_5(self):
        result = task_func(1, 5)
        self.assertEqual(result.shape, (1, 5))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)