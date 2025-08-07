import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    # Validate inputs
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer.")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer.")
    
    # Set random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Define colors to cycle through
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    color_cycle = itertools.cycle(colors)
    
    # Generate random walks
    walks = np.cumsum(np.random.choice([-1, 1], size=(n_walks, n_steps)), axis=1)
    
    # Plot the walks
    fig, ax = plt.subplots()
    for walk in walks:
        ax.plot(walk, color=next(color_cycle))
    
    # Set plot labels and title
    ax.set_xlabel('Step')
    ax.set_ylabel('Position')
    ax.set_title(f'{n_walks} Random Walks with {n_steps} Steps Each')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func(5, 100, seed=42)
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic setup
        ax = task_func(5, 100, seed=42)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        # Test number of walks
        for n_walk in [0, 1, 2, 10, 50]:
            ax = task_func(n_walk, 10, seed=42)
            lines = ax.get_lines()
            self.assertEqual(len(lines), n_walk)
    def test_case_3(self):
        # Test number of steps
        for n_steps in [0, 1, 10, 100, 500]:
            ax = task_func(2, n_steps, seed=42)
            lines = ax.get_lines()
            self.assertEqual(len(lines[0].get_ydata()), n_steps)
    def test_case_4(self):
        # Test random seed
        ax1 = task_func(5, 100, seed=42)
        ax2 = task_func(5, 100, seed=42)
        ax3 = task_func(5, 100, seed=0)
        lines1 = ax1.get_lines()
        lines2 = ax2.get_lines()
        lines3 = ax3.get_lines()
        self.assertTrue(
            all(
                np.array_equal(line1.get_ydata(), line2.get_ydata())
                for line1, line2 in zip(lines1, lines2)
            )
        )
        self.assertFalse(
            all(
                np.array_equal(line1.get_ydata(), line3.get_ydata())
                for line1, line3 in zip(lines1, lines3)
            ),
            "Random walks are not reproducible using the same seed.",
        )
    def test_case_5(self):
        # Test invalid n_walks
        with self.assertRaises(ValueError):
            task_func(-1, 100, seed=42)
    def test_case_6(self):
        # Test negative n_steps
        with self.assertRaises(ValueError):
            task_func(1, -100, seed=42)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)