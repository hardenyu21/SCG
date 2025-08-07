import random
import math
import matplotlib.pyplot as plt

def task_func(points_count=1000, radius=1):
    # Generate random points within a circle
    points = []
    for _ in range(points_count):
        # Generate a random angle
        theta = random.uniform(0, 2 * math.pi)
        # Generate a random radius, ensuring uniform distribution
        r = radius * math.sqrt(random.uniform(0, 1))
        # Convert polar coordinates to Cartesian coordinates
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    
    # Unpack the points into x and y coordinates
    x_coords, y_coords = zip(*points)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_coords, y_coords)
    
    # Set the aspect ratio to 'equal'
    ax.set_aspect('equal')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax
import unittest
import matplotlib.pyplot as plt
import random 
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        ax = task_func()
        self.assertEqual(len(ax.collections[0].get_offsets()), 1000, "Default parameter points count mismatch")
        self.assertEqual(ax.get_aspect(), 1.0, "Aspect ratio mismatch in default parameters test")
        plt.close()
    def test_custom_parameters(self):
        random.seed(0)
        ax = task_func(500, 0.5)
        self.assertEqual(len(ax.collections[0].get_offsets()), 500, "Custom parameter points count mismatch")
        self.assertEqual(ax.get_aspect(), 1.0, "Aspect ratio mismatch in custom parameters test")
        plt.close()
    def test_radius_accuracy(self):
        random.seed(0)
        radius = 2
        ax = task_func(100, radius)
        points = ax.collections[0].get_offsets()
        for point in points[:1]:
            self.assertTrue(math.sqrt(point[0]**2 + point[1]**2) <= radius, "Point outside specified radius")
        plt.close()
    def test_plot_title(self):
        random.seed(0)
        ax = task_func()
        ax.set_title("Test Plot")
        self.assertEqual(ax.get_title(), "Test Plot", "Plot title mismatch")
        plt.close()
    def test_axes_labels(self):
        random.seed(0)
        ax = task_func()
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        self.assertEqual(ax.get_xlabel(), "X Axis", "X-axis label mismatch")
        self.assertEqual(ax.get_ylabel(), "Y Axis", "Y-axis label mismatch")
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)