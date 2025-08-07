import random
from collections import Counter

def task_func(values, weights, n_samples):
    # Ensure the weights sum to 1
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]
    
    # Sample random numbers based on the weighted distribution
    samples = random.choices(values, weights=normalized_weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = Counter(samples)
    
    return dict(histogram)

# Example usage:
values = ['a', 'b', 'c']
weights = [0.1, 0.3, 0.6]
n_samples = 1000
histogram = task_func(values, weights, n_samples)
print(histogram)
import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        result = task_func([1, 2, 3], [3, 2, 1], 1000)
        self.assertTrue(set(result.keys()) == {1, 2, 3})
    def test_2(self):
        result = task_func([1, 2], [1, 1], 500)
        self.assertTrue(set(result.keys()) == {1, 2})
    def test_3(self):
        result = task_func([1], [1], 300)
        self.assertTrue(result == {1: 300})
    def test_4(self):
        result = task_func(list(range(1, 11)), list(range(10, 0, -1)), 5000)
        self.assertTrue(set(result.keys()) == set(range(1, 11)))
    def test_5(self):
        result = task_func([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 2500)
        self.assertTrue(set(result.keys()) == {1, 2, 3, 4, 5})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)