from functools import reduce
from itertools import combinations
import numpy as np

def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if high <= low:
        raise ValueError("high must be greater than low")
    
    if seed is not None:
        np.random.seed(seed)
    
    # Generate the matrix with random numbers within the specified range
    matrix = np.random.randint(low, high, size=shape)
    
    # Flatten the matrix to a 1D array to easily generate all possible pairs
    flat_matrix = matrix.flatten()
    
    # Generate all possible combinations of two numbers from the matrix
    pairs = combinations(flat_matrix, 2)
    
    # Calculate the sum of the products of all pairs
    sum_of_products = sum(a * b for a, b in pairs)
    
    return sum_of_products, matrix

# Example usage
result = task_func((5, 4), seed=1)
print(result)
import unittest
class TestCases(unittest.TestCase):
    def _calculate_sum_of_product_pairs(self, matrix):
        values = matrix.flatten()
        all_pairs = list(combinations(values, 2))
        sum_of_products = reduce(lambda a, b: a + b, [np.prod(pair) for pair in all_pairs])
        return sum_of_products
    def test_case_1(self):
        # Testing with default parameters
        result, matrix = task_func(seed=1)
        self.assertAlmostEqual(result, self._calculate_sum_of_product_pairs(matrix))
    def test_case_2(self):
        # Testing with a specific seed for reproducibility
        seed = 42
        result1, matrix1 = task_func(seed=seed)
        result2, matrix2 = task_func(seed=seed)
        self.assertEqual(result1, result2)
        self.assertEqual(list(matrix1.flatten()), list(matrix2.flatten()))
    def test_case_3(self):
        # Testing with a different matrix shape
        shape = (4, 4)
        result, matrix = task_func(shape=shape, seed=1)
        self.assertAlmostEqual(result, self._calculate_sum_of_product_pairs(matrix))
    def test_case_4(self):
        # Testing with different number ranges
        low, high = 10, 20
        result, matrix = task_func(low=low, high=high, seed=12)
        val = matrix.flatten()
        self.assertTrue(((val >= low) & (val < high)).all())
        self.assertAlmostEqual(result, self._calculate_sum_of_product_pairs(matrix))
    def test_case_5(self):
        # Testing the scenario where the random number range is invalid (high <= low)
        with self.assertRaises(ValueError):
            task_func(low=5, high=5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)