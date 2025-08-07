import numpy as np
from scipy import stats

def task_func(L):
    # Flatten the nested list
    flat_list = [item for sublist in L for item in sublist]
    
    # Calculate the mode
    mode_result = stats.mode(flat_list)
    
    # Extract the mode value
    mode = mode_result.mode[0]
    
    return mode
import unittest
class TestCases(unittest.TestCase):
    
    def test_1(self):
        result = task_func([[1, 2, 3], [4, 5, 6]])
        expected = 1
        self.assertEqual(result, expected)
    
    def test_2(self):
        result = task_func([[1, 2, 3], [4, 5, 6, 6]])
        expected = 6
        self.assertEqual(result, expected)
        
    def test_3(self):
        result = task_func([[1, 1, 2, 2], [3, 4, 5]])
        expected = 1
        self.assertEqual(result, expected)
    
    def test_4(self):
        result = task_func([[1, 1, 2, 2]])
        expected = 1
        self.assertEqual(result, expected)
    
    def test_5(self):
        result = task_func([[-1, -1, -2, -3], [0, 1, 2, 3]])
        expected = -1
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)