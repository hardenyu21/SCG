import numpy as np
import math

# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        length = len(lst)
        # Select the first 'length' numbers from POSSIBLE_NUMBERS
        selected_numbers = POSSIBLE_NUMBERS[:length]
        # Calculate the sum of squares of the selected numbers
        sum_of_squares = np.sum(selected_numbers ** 2)
        sums.append(sum_of_squares)
    return sums

# Example usage:
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = task_func(list_of_lists)
print(result)  # Output: [14, 54, 130]
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with empty list
        result = task_func([])
        self.assertEqual(result, [])
    def test_case_2(self):
        # Testing with empty sublists
        result = task_func([[], [], []])
        self.assertEqual(result, [0, 0, 0])
        
    def test_case_3(self):
        # Testing with sublists of different lengths
        result = task_func([[1], [1, 2], [1, 2, 3]])
        self.assertEqual(result, [1, 5, 14])
    def test_case_4(self):
        # Testing with sublists containing the same element
        result = task_func([[1, 1, 1], [2, 2, 2, 2]])
        self.assertEqual(result, [14, 30])
        
    def test_case_5(self):
        # Testing with large sublists
        result = task_func([[1]*10, [2]*5])
        self.assertEqual(result, [385, 55])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)