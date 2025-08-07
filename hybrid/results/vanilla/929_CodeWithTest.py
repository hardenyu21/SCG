import numpy as np
from scipy import stats

def task_func(word: str) -> (np.ndarray, float):
    # Calculate the differences between ASCII values of adjacent letters
    differences = np.array([ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)])
    
    # Calculate the entropy of the differences
    # First, calculate the probability distribution of the differences
    value_counts = np.bincount(differences)
    probabilities = value_counts / len(differences)
    
    # Calculate entropy using the formula: H(X) = -sum(p(x) * log2(p(x)))
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))  # Adding a small epsilon to avoid log(0)
    
    return differences, entropy
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('abcdef')
        expected_diff = np.array([1, 1, 1, 1, 1])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 1.6094379124341005)
        
    def test_case_2(self):
        result = task_func('hell')
        expected_diff = np.array([-3, 7, 0])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], -np.inf)
        
    def test_case_3(self):
        result = task_func('az')
        expected_diff = np.array([25])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 0.0)
        
    def test_case_4(self):
        result = task_func('a')
        expected_diff = np.array([])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 0.0)
        
    def test_case_5(self):
        result = task_func('i love Python')
        expected_diff = np.array([-73,  76,   3,   7, -17, -69,  48,  41,  -5, -12,   7,  -1])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], -np.inf)
        
    def test_case_6(self):
        result = task_func('Za')
        expected_diff = np.array([7])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 0.0)
    def test_case_7(self):
        result = task_func('racecar')
        expected_diff = np.array([-17, 2, 2, -2, -2, 17])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], -np.inf)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)