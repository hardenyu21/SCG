import numpy as np
from itertools import combinations

def task_func(array1, array2):
    # Check if the input arrays have different lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length.")
    
    # If the arrays are empty, return 0
    if len(array1) == 0:
        return 0.0
    
    # Combine elements from both arrays to form points
    points = list(zip(array1, array2))
    
    # Initialize the maximum distance
    max_distance = 0.0
    
    # Calculate the Euclidean distance between all pairs of points
    for (x1, y1), (x2, y2) in combinations(points, 2):
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance > max_distance:
            max_distance = distance
    
    return max_distance
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_non_empty_arrays(self):
        # Test with non-empty arrays containing positive values
        # Expected result is the maximum Euclidean distance between any two points
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = task_func(array1, array2)
        self.assertAlmostEqual(result, 2.8284271247461903, places=6)
    def test_empty_arrays(self):
        # Test with empty arrays
        # Expected result is 0 since there are no points to calculate the distance between
        array1 = np.array([])
        array2 = np.array([])
        result = task_func(array1, array2)
        self.assertEqual(result, 0)
    def test_single_element_arrays(self):
        # Test with arrays that each contain a single element
        # Expected result is 0 since there is only one point
        array1 = np.array([1])
        array2 = np.array([2])
        result = task_func(array1, array2)
        self.assertEqual(result, 0)
    def test_negative_values(self):
        # Test with non-empty arrays containing negative values
        # Expected result is the maximum Euclidean distance between any two points
        array1 = np.array([-1, -2, -3])
        array2 = np.array([-4, -5, -6])
        result = task_func(array1, array2)
        self.assertAlmostEqual(result, 2.8284271247461903, places=6)
    def test_mixed_values(self):
        # Test with non-empty arrays containing a mix of positive and negative values
        # Expected result is the maximum Euclidean distance between any two points
        array1 = np.array([1, -2, 3])
        array2 = np.array([-4, 5, -6])
        result = task_func(array1, array2)
        self.assertAlmostEqual(result, 12.083045973594572, places=6)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)