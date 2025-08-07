from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    # Handle the case where the list is empty or contains only one point
    if len(points) < 2:
        return []
    
    # Normalize points to ensure each is a tuple of two numbers
    normalized_points = [(x, x) if isinstance(x, (int, float)) else x for x in points]
    
    # Calculate Euclidean distances between consecutive points
    distances = [
        distance.euclidean(p1, p2)
        for p1, p2 in zip_longest(normalized_points, normalized_points[1:])
    ]
    
    return distances

# Example usage
print(task_func([(1, 2), (4), (-1.2, 4)]))  # Output: [3.605551275463989, 5.2]
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        # Testing with no points
        self.assertEqual(task_func([]), [])
    def test_single_point(self):
        # Testing with a single point (no distances can be calculated)
        self.assertEqual(task_func([(0, 0)]), [])
    def test_zero_distance(self):
        # Testing with multiple points at the same location (zero distance)
        self.assertEqual(task_func([(3, 4), (3, 4)]), [0.0])
    def test_various_distances(self):
        # Testing with points at various distances
        points = [(1, 2), (4, 6), (4, 6), (10, 20)]
        # The distances between the points are approximately:
        results = task_func(points)
        self.assertTrue(all(isinstance(x, float) for x in results))
        self.assertAlmostEqual(results[0], 5.0, places=4)
        self.assertAlmostEqual(results[1], 0.0, places=4)
        self.assertAlmostEqual(results[2], 15.2315421, places=4)
    def test_negative_coordinates(self):
        # Testing with points in negative coordinates
        points = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
        results = task_func(points)
        expected = [1.4142135623730951] * 3  # repeating 3 times
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)