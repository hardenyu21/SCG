import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    distances = []
    
    for _ in range(n):
        # Generate a random angle
        theta = random.uniform(0, 2 * math.pi)
        
        # Generate a random radius, considering the uniform distribution of points
        r = RADIUS * math.sqrt(random.uniform(0, 1))
        
        # Calculate the distance from the center (which is the radius itself)
        distance = r
        
        # Store the distance
        distances.append(distance)
    
    # Calculate the average distance
    average_distance = statistics.mean(distances)
    
    return average_distance

# Example usage:
# print(task_func(1000))
import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        avg_distance = task_func(1000)
        self.assertTrue(3.1 <= avg_distance <= 3.5, f"Expected average distance to be between 3.1 and 3.5, got {avg_distance}")
    def test_2(self):
        avg_distance = task_func(500)
        self.assertTrue(3.0 <= avg_distance <= 3.6, f"Expected average distance to be between 3.2 and 3.5, got {avg_distance}")
    def test_3(self):
        avg_distance = task_func(100)
        self.assertTrue(2.8 <= avg_distance <= 3.7, f"Expected average distance to be between 2.8 and 3.7, got {avg_distance}")
    def test_4(self):
        avg_distance = task_func(50)
        # Allowing a wider range due to higher variance with fewer points
        self.assertTrue(2.4 <= avg_distance <= 4.1, f"Expected average distance to be between 2.4 and 4.1, got {avg_distance}")
    def test_5(self):
        avg_distance = task_func(10)
        # Even wider range for very few points
        self.assertTrue(1.4 <= avg_distance <= 4.6, f"Expected average distance to be between 1.4 and 4.6, got {avg_distance}")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)