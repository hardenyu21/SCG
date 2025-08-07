import itertools
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
SHAPES = [
    "Circle",
    "Square",
    "Triangle",
    "Rectangle",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
]
COLORS = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
]

def task_func(num_pairs=10):
    # Generate all possible shape-color combinations
    all_combinations = list(itertools.product(SHAPES, COLORS))
    
    # Select the specified number of unique combinations
    selected_combinations = all_combinations[:num_pairs]
    
    # Flatten the list of tuples into a single list of strings
    combination_labels = [f"{shape}-{color}" for shape, color in selected_combinations]
    
    # Create a countplot
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(y=combination_labels, order=combination_labels)
    
    # Set plot title and labels
    ax.set_title(f"Countplot of {num_pairs} Shape-Color Combinations")
    ax.set_xlabel("Count")
    ax.set_ylabel("Shape-Color Pair")
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax

# Example usage
ax = task_func(10)
import unittest
import matplotlib.pyplot as plt
import random
class TestCases(unittest.TestCase):
    """Tests for task_func."""
    def tearDown(self):
        plt.clf()
    def test_basic_functionality(self):
        """Test basic functionality with default parameters."""
        random.seed(0)
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
    def test_pair_count(self):
        """Test if the number of displayed shape-color pairs matches the input."""
        random.seed(1)
        num_pairs = 7
        ax = task_func(num_pairs)
        displayed_pairs = len(set(tick.get_text() for tick in ax.get_xticklabels()))
        self.assertEqual(displayed_pairs, num_pairs)
    def test_valid_pairs(self):
        """Ensure displayed shape-color pairs are valid combinations."""
        random.seed(2)
        ax = task_func(10)
        displayed_pairs = [tick.get_text() for tick in ax.get_xticklabels()]
        for pair in displayed_pairs:
            shape, color = pair.split(":")
            self.assertIn(shape, SHAPES)
            self.assertIn(color, COLORS)
    def test_max_pairs(self):
        """Test with the maximum number of pairs possible."""
        random.seed(3)
        max_pairs = len(SHAPES) * len(COLORS)
        ax = task_func(max_pairs)
        displayed_pairs = len(set(tick.get_text() for tick in ax.get_xticklabels()))
        self.assertEqual(displayed_pairs, max_pairs)
    def test_min_pairs(self):
        """Test with the minimum number of pairs, which is 1."""
        random.seed(4)
        ax = task_func(1)
        displayed_pairs = len(set(tick.get_text() for tick in ax.get_xticklabels()))
        self.assertEqual(displayed_pairs, 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)