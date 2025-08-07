import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def task_func(ax):
    # Generate random parameters for the sine wave
    amplitude = random.uniform(0.5, 1.5)
    frequency = random.uniform(1, 5)
    phase = random.uniform(0, 2 * np.pi)
    
    # Generate theta values
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the sine wave
    r = amplitude * np.sin(frequency * theta + phase)
    
    # Select a random color
    color = random.choice(COLORS)
    
    # Plot the sine wave on the polar subplot
    ax.plot(theta, r, color=color)
    
    # Set random positions for radial labels
    ax.set_rlabel_position(random.uniform(0, 360))
    
    # Return the color code of the plotted function
    return color

# Example usage
if __name__ == "__main__":
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    color = task_func(ax)
    print(f"Plotted color: {color}")
    plt.show()
import matplotlib.pyplot as plt
import unittest
import random
class TestCases(unittest.TestCase):
    def test_color_returned(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        color = task_func(ax)
        self.assertIn(color, ['b', 'g', 'r', 'c', 'm', 'y', 'k'])
        plt.close()
    def test_random_color(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        colors = set(task_func(ax) for _ in range(10))
        self.assertTrue(len(colors) > 1)
        plt.close()
    def test_plot_exists(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        task_func(ax)
        self.assertTrue(len(ax.lines) > 0)
        plt.close()
    def test_plot_properties(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        color = task_func(ax)
        line = ax.lines[0]
        self.assertEqual(line.get_color(), color)
        plt.close()
    def test_label_position(self):
        random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        task_func(ax)
        position = ax.get_rlabel_position()
        self.assertTrue(position>1.0)
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)