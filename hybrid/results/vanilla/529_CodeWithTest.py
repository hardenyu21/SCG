from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize a list to store the sums of the dice rolls
    sums = []
    
    # Simulate rolling the dice
    for _ in range(num_rolls):
        # Roll the dice and calculate the sum
        roll_sum = sum(random.randint(1, 6) for _ in range(num_dice))
        sums.append(roll_sum)
    
    # Count the occurrences of each sum
    sum_counter = Counter(sums)
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(sum_counter.keys(), sum_counter.values(), color='blue')
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')
    
    # Save the plot if a path is provided
    if plot_path:
        plt.savefig(plot_path)
    
    # Return the Counter object and the Axes object
    return sum_counter, ax

# Example usage:
# counter, ax = task_func(num_rolls=1000, num_dice=2, plot_path='dice_distribution.png')
# plt.show()
import unittest
import os
from collections import Counter
import tempfile
import shutil
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store plots
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Close matplotlib plots and remove temporary directory
        plt.close("all")
    def test_case_1(self):
        # Test basic functionality with 100 rolls and 2 dice
        result, ax = task_func(100, 2, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_2(self):
        # Test plot saving functionality
        plot_path = os.path.join(self.test_dir, "test_plot.png")
        result, ax = task_func(1000, 1, plot_path, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(os.path.exists(plot_path))
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_3(self):
        # Test with a larger number of dice
        result, ax = task_func(500, 5, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_4(self):
        # Test with the minimum possible inputs
        result, ax = task_func(1, 1, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(result), 1)  # Only one possible sum with 1 roll of 1 die
    def test_case_5(self):
        # Test the effect of different random seeds on the result consistency
        result1, _ = task_func(100, 2, random_seed=42)
        result2, _ = task_func(100, 2, random_seed=43)
        self.assertNotEqual(
            result1, result2, "Results should differ with different seeds"
        )
    def test_case_6(self):
        # Test plot detail correctness (labels, title)
        plot_path = os.path.join(self.test_dir, "test_plot_detail.png")
        _, ax = task_func(10, 2, plot_path, random_seed=42)
        self.assertTrue(
            "sum of dice roll" in ax.get_xlabel().lower(), "X-axis label is incorrect"
        )
        self.assertEqual(ax.get_ylabel(), "Count", "Y-axis label is incorrect")
        self.assertTrue(
            "distribution of dice roll sums" in ax.get_title().lower(),
            "Plot title is incorrect",
        )
    def test_case_7(self):
        # Test data correctness with a manually calculated example
        result, _ = task_func(2, 1, random_seed=42)
        expected = Counter({6: 1, 1: 1})
        self.assertEqual(
            result, expected, "Data distribution does not match expected outcome"
        )
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)