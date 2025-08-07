import random
import string

def task_func(max_length, n_samples, seed=None):
    if max_length < 1:
        raise ValueError("max_length must be at least 1.")
    
    if seed is not None:
        random.seed(seed)
    
    random_strings = []
    for _ in range(n_samples):
        length = random.randint(1, max_length)
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
        random_strings.append(random_string)
    
    return random_strings
"""
This script contains tests for the function task_func.
Each test checks a specific aspect of the function's behavior.
"""
import unittest
import random
class TestCases(unittest.TestCase):
    def test_length_and_content(self):
        """Test the length of the output and whether it contains valid strings."""
        seed = 1  # for reproducibility
        max_length = 5
        result = task_func(max_length, n_samples=10, seed=seed)
        
        # All outputs should be strings
        self.assertTrue(all(isinstance(item, str) for item in result))
        # All strings should be of length <= max_length and > 0
        self.assertTrue(all(1 <= len(item) <= max_length for item in result))
        expected = ['ou', 'g', 'tmjf', 'avlt', 's', 'sfy', 'aao', 'rzsn', 'yoir', 'yykx']
        self.assertCountEqual(result, expected)
    def test_randomness(self):
        """Test that setting a seed produces reproducible results."""
        seed = 2
        result1 = task_func(3, seed=seed, n_samples=100)
        result2 = task_func(3, seed=seed, n_samples=100)
        self.assertEqual(result1, result2)  # results should be same with same seed
    def test_varying_length(self):
        """Test with varying n to check the function's robustness with different input sizes."""
        seed = 3
        for n in range(1, 15):  # testing multiple sizes
            result = task_func(n, seed=seed, n_samples=10)
            self.assertTrue(all(1 <= len(item) <= n for item in result))
    def test_negative_input(self):
        """Test how the function handles negative input. It should handle it gracefully."""
        with self.assertRaises(ValueError):
            task_func(-1, n_samples=22)  # negative numbers shouldn't be allowed
    def test_zero_length(self):
        """Test how the function handles zero input. It should handle it gracefully or according to its specification."""
        self.assertRaises(ValueError, task_func, 0, n_samples=5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)