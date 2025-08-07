import numpy as np
from scipy.stats import iqr

def task_func(L):
    # Flatten the nested list
    flat_list = [item for sublist in L for item in sublist]
    
    # Calculate the interquartile range
    iqr_value = iqr(flat_list)
    
    return iqr_value
import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        result = task_func([[1,2,3],[4,5,6]])
        expected = 2.5
        self.assertAlmostEqual(result, expected, places=2)
    def test_2(self):
        result = task_func([[1,1,1],[2,2,2]])
        expected = 1.0
        self.assertAlmostEqual(result, expected, places=2)
    def test_3(self):
        result = task_func([[1,5,3]])
        expected = 2.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_4(self):
        result = task_func([[1],[2],[3],[4],[5]])
        expected = 2.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_5(self):
        result = task_func([[1,-2,3],[-4,5,6]])
        expected = 5.75
        self.assertAlmostEqual(result, expected, places=2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)