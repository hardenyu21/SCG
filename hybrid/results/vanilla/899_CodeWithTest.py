import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length must be non-negative.")
    
    random.seed(seed)
    steps = [random.choice([-1, 1]) for _ in range(length)]
    walk = np.cumsum([0] + steps)
    
    return walk

# Example usage:
# walk = task_func(10)
# print(walk)
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)  # Setting seed for reproducibility
    def test_default_length(self):
        walk = task_func(seed=42)
        self.assertEqual(len(walk), 10001)  # Includes starting point
    def test_custom_length(self):
        walk = task_func(5000, seed=42)
        self.assertEqual(len(walk), 5001)  # Includes starting point
    def test_first_step_zero(self):
        walk = task_func(1, seed=42)
        self.assertEqual(walk[0], 0)  # First position should be 0
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_output_type(self):
        walk = task_func(5, seed=42)
        self.assertEqual(walk.tolist(), [0, 1, 0, -1, -2, -1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)