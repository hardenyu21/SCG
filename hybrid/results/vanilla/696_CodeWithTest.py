import numpy as np
import math
import random
from random import uniform

def task_func(radius, num_points):
    points = []
    for _ in range(num_points):
        # Generate a random angle
        theta = uniform(0, 2 * math.pi)
        # Generate a random radius, ensuring points are uniformly distributed
        r = radius * math.sqrt(uniform(0, 1))
        # Convert polar coordinates to Cartesian coordinates
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    return points

# Example usage:
# radius = 5
# num_points = 10
# out = task_func(radius, num_points)
# print(out)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        points = task_func(1, 3)
        for x, y in points:
            self.assertTrue(x**2 + y**2 <= 1)
    def test_case_2(self):
        points = task_func(2, 3)
        for x, y in points:
            self.assertTrue(x**2 + y**2 <= 4)
    def test_case_3(self):
        points = task_func(3, 3)
        for x, y in points:
            self.assertTrue(x**2 + y**2 <= 9)
    def test_case_4(self):
        points = task_func(4, 3)
        for x, y in points:
            self.assertTrue(x**2 + y**2 <= 16)
    def test_case_5(self):
        points = task_func(5, 3)
        for x, y in points:
            self.assertTrue(x**2 + y**2 <= 25)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)