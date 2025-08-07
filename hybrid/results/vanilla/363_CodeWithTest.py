from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)

def task_func(numbers: list) -> dict:
    # Validate input
    if not all(isinstance(n, int) and n >= 0 for n in numbers):
        raise ValueError("All elements in the input list must be non-negative integers.")
    
    # Use multiprocessing to calculate factorials in parallel
    with Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
    
    # Convert list of tuples to dictionary
    return dict(results)

# Example usage:
# numbers = [0, 1, 2, 3, 4, 5]
# print(task_func(numbers))
import unittest
import math
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a dictionary."""
        result = task_func([3, 4, 5])
        self.assertIsInstance(result, dict)
    def test_empty_list(self):
        """Test function with an empty list."""
        result = task_func([])
        self.assertEqual(result, {})
    def test_single_element(self):
        """Test function with a single-element list."""
        result = task_func([5])
        self.assertEqual(result, {5: 120})
    def test_non_integer_input(self):
        """Test function with non-integer input."""
        with self.assertRaises(ValueError):
            task_func(["a"])
    def test_large_numbers(self):
        """Test function with large numbers."""
        result = task_func([10])
        self.assertEqual(result[10], math.factorial(10))
    def test_negative_numbers(self):
        """Test function with a negative number."""
        with self.assertRaises(ValueError):
            task_func([-1])  # Assuming we want to enforce non-negative integers only
    def test_very_large_number(self):
        """Test function with a very large number to check for performance or overflow issues."""
        number = 20  # A reasonable choice to avoid excessive computation time in tests
        result = task_func([number])
        self.assertEqual(result[number], math.factorial(number))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)