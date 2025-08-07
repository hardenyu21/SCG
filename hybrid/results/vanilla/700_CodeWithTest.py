import pandas as pd
import numpy as np

def task_func(data, cols):
    # Convert the provided data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Calculate the correlation matrix of numeric columns
    correlation_matrix = df.corr()
    
    return correlation_matrix

# Example usage:
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# cols = ['A', 'B', 'C']
# print(task_func(data, cols))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], columns = ['x', 'y', 'z'])
        correlation_matrix = task_func([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))
    def test_case_2(self):
        df = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = task_func([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))
    def test_case_3(self):
        df = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = task_func([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))
    
    def test_case_4(self):
        df = pd.DataFrame([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = task_func([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))
    def test_case_5(self):
        df = pd.DataFrame([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0], [-7.0, -8.0, -9.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = task_func([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0], [-7.0, -8.0, -9.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)