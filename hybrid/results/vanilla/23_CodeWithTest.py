import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD=0.5):
    # Combine elements from l1 and l2 alternately
    combined = []
    for a, b in zip_longest(l1, l2):
        if a is not None:
            combined.append(a)
        if b is not None:
            combined.append(b)
    
    # Calculate the absolute difference from the threshold
    differences = [abs(x - THRESHOLD) for x in combined]
    
    # Find the element with the minimum difference
    min_diff_index = np.argmin(differences)
    closest_element = combined[min_diff_index]
    
    return closest_element

# Example usage:
l1 = [0.1, 0.6, 0.9]
l2 = [0.3, 0.8]
print(task_func(l1, l2))  # Output: 0.6
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with two lists of equal length where one element exactly matches the threshold.
        l1 = [0, 0.5, 2, 3, 4]
        l2 = [10, 11, 12, 13, 14]
        self.assertEqual(task_func(l1, l2), 0.5)
    def test_case_2(self):
        # Test with the first list longer than the second, where the closest value is below the threshold.
        l1 = [0, 0.4, 0.6, 3, 4, 5]
        l2 = [10, 11, 12]
        self.assertEqual(task_func(l1, l2), 0.4)
        
    def test_case_3(self):
        # Test with the second list longer than the first, where the closest value is just above the threshold.
        l1 = [0, 0.51]
        l2 = [10, 11, 12, 13]
        self.assertEqual(task_func(l1, l2), 0.51)
        
    def test_case_4(self):
        # Test where one list is empty and the function must choose the closest value from a single non-empty list.
        l1 = []
        l2 = [10, 11, 12, 13]
        self.assertEqual(task_func(l1, l2), 10)
        
    def test_case_5(self):
        # Test with negative and positive numbers where the closest value to the threshold is zero.
        l1 = [-10, -5, 0, 5, 10]
        l2 = [-1, 0, 1]
        self.assertEqual(task_func(l1, l2), 0)
    def test_empty_lists(self):
        # Test with both lists empty to check function's behavior in absence of any elements.
        with self.assertRaises(ValueError):
            task_func([], [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)