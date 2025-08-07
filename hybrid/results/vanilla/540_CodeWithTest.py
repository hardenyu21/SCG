from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the nested list using itertools.chain
    flattened_items = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each item
    item_counts = Counter(flattened_items)
    
    # Sort the items alphabetically
    sorted_items = sorted(item_counts.keys())
    
    # Prepare the data for plotting
    frequencies = [item_counts[item] for item in sorted_items]
    
    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.bar(sorted_items, frequencies, color=color, width=width)
    
    # Set the labels and title
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax

# Example usage:
# list_of_menuitems = [['burger', 'fries'], ['burger', 'soda'], ['fries', 'soda', 'soda']]
# ax = task_func(list_of_menuitems)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_data = [["Pizza", "Burger"], ["Pizza", "Coke"], ["Pasta", "Coke"]]
        ax = task_func(input_data)
        # Test default plot properties
        self.assertEqual(ax.get_title(), "Menu Distribution")
        self.assertEqual(ax.get_xlabel(), "Menu Items")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        for p in ax.patches:
            # RGBA color
            self.assertEqual(p.get_facecolor(), (0.0, 0.0, 1.0, 1.0))
            # bar width
            self.assertEqual(p.get_width(), 1.0)
    def test_case_2(self):
        input_data = [["Pizza", "Burger"], ["Pizza", "Coke"], ["Pasta", "Coke"]]
        ax = task_func(input_data, title="Custom Title", color="red", width=0.8)
        # Test custom plot properties
        self.assertEqual(ax.get_title(), "Custom Title")
        self.assertEqual(ax.get_xlabel(), "Menu Items")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        for p in ax.patches:
            # RGBA color
            self.assertEqual(p.get_facecolor(), (1.0, 0.0, 0.0, 1.0))
            # bar width
            self.assertEqual(p.get_width(), 0.8)
    def test_case_3(self):
        input_data = [["Burger"], ["Pizza"], ["Pasta"]]
        ax = task_func(input_data)
        # Test count
        bars = [p.get_height() for p in ax.patches]
        self.assertEqual(bars, [1, 1, 1])
    def test_case_4(self):
        input_data = [["Carrot", "Apple"], ["Apple", "Banana"], ["Banana"]]
        ax = task_func(input_data)
        # Test x-axis order
        self.assertEqual(
            [_._text for _ in ax.get_xticklabels() if _._text],
            ["Apple", "Banana", "Carrot"],
        )
    def test_case_5(self):
        # Test input edge case: some empty elements
        ax = task_func([[], ["Apple"]])
        self.assertEqual(len(ax.patches), 1)
        for p in ax.patches:
            # bar width
            self.assertEqual(p.get_width(), 1.0)
            self.assertEqual(p.get_height(), 1)
    def test_case_6(self):
        with self.assertRaises(ValueError):
            task_func([])
        with self.assertRaises(ValueError):
            task_func([[]])
        with self.assertRaises(ValueError):
            task_func("")
        with self.assertRaises(TypeError):
            task_func(None)
        with self.assertRaises(TypeError):
            task_func(1)
        with self.assertRaises(TypeError):
            task_func([1])
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)