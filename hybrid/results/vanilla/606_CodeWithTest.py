import pandas as pd
from scipy import stats

def task_func(matrix):
    # Convert the input matrix to a DataFrame
    df = pd.DataFrame(matrix)
    
    # Apply Z-score normalization to each column
    normalized_df = df.apply(stats.zscore)
    
    return normalized_df
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_extreme_values_shape(self):
        """Test the function with extreme values to ensure output shape is correct."""
        matrix = [[1, 2], [10000, 20000]]
        result_df = task_func(matrix)
        # Verify that the shape of the result is the same as the input
        self.assertEqual(result_df.shape, (2, 2))
    def test_case_2(self):
        matrix = np.array([[2, 5], [5, 2]])
        result = task_func(matrix)
        expected_result = pd.DataFrame({
            0: [-1.0, 1.0],
            1: [1.0, -1.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_3(self):
        matrix = np.array([[5]])
        result = task_func(matrix)
        expected_result = pd.DataFrame({
            0: [0.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_uniform_data(self):
        """Test a matrix where all elements are the same."""
        matrix = [[1, 1], [1, 1]]
        expected_result = pd.DataFrame({
            0: [0.0, 0.0],
            1: [0.0, 0.0]
        })
        pd.testing.assert_frame_equal(task_func(matrix), expected_result)
    def test_non_numeric_data(self):
        """Test the function with non-numeric data."""
        matrix = [['a', 'b'], ['c', 'd']]
        with self.assertRaises(TypeError):
            task_func(matrix)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)