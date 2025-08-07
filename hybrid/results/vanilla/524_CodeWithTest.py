from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is empty
    if not data:
        raise ValueError("The input data is empty.")
    
    # Check if the input is a list of dictionaries
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("The input must be a list of dictionaries.")
    
    # Check if all values in the dictionaries are numeric
    for d in data:
        for value in d.values():
            if not isinstance(value, (int, float)):
                raise TypeError("All values in the dictionaries must be numeric.")
    
    # Calculate mean and standard deviation for each key
    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)
    
    results = {}
    for key, values in stats.items():
        mean_value = np.mean(values)
        std_value = np.std(values)
        results[key] = {'mean': mean_value, 'std': std_value}
    
    # Visualize mean and standard deviation with bar charts
    fig, axes = plt.subplots(len(results), 2, figsize=(10, 5 * len(results)))
    axes = axes.flatten() if len(results) > 1 else [axes]
    
    for i, (key, stats) in enumerate(results.items()):
        axes[2 * i].bar(key, stats['mean'], color='blue')
        axes[2 * i].set_title(f'Mean of {key}')
        axes[2 * i].set_ylabel('Mean Value')
        
        axes[2 * i + 1].bar(key, stats['std'], color='green')
        axes[2 * i + 1].set_title(f'Standard Deviation of {key}')
        axes[2 * i + 1].set_ylabel('Standard Deviation')
    
    plt.tight_layout()
    
    return results, axes

# Example usage:
# data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
# results, axes = task_func(data)
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        data = [{"cat": 1, "dog": 3}, {"cat": 2, "dog": 5}, {"cat": 3, "dog": 7}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats["cat"]["mean"], 2.0)
        self.assertAlmostEqual(stats["cat"]["std"], 0.816496580927726)
        self.assertAlmostEqual(stats["dog"]["mean"], 5.0)
        self.assertAlmostEqual(stats["dog"]["std"], 1.632993161855452)
        
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        self.assertEqual(axes[1].get_title(), "Statistics of dog")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_2(self):
        # Test other keys (animals)
        data = [{"bird": 5, "fish": 10}, {"bird": 6, "fish": 8}, {"bird": 7, "fish": 9}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats["bird"]["mean"], 6.0)
        self.assertAlmostEqual(stats["bird"]["std"], 0.816496580927726)
        self.assertAlmostEqual(stats["fish"]["mean"], 9.0)
        self.assertAlmostEqual(stats["fish"]["std"], 0.816496580927726)
        self.assertEqual(axes[0].get_title(), "Statistics of bird")
        self.assertEqual(axes[1].get_title(), "Statistics of fish")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_3(self):
        # Test handling negatives
        data = [{"cat": -1, "dog": -3}, {"cat": -2, "dog": -5}, {"cat": -3, "dog": -7}]
        stats, axes = task_func(data)
        self.assertAlmostEqual(stats["cat"]["mean"], -2.0)
        self.assertAlmostEqual(stats["cat"]["std"], 0.816496580927726)
        self.assertAlmostEqual(stats["dog"]["mean"], -5.0)
        self.assertAlmostEqual(stats["dog"]["std"], 1.632993161855452)
        
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        self.assertEqual(axes[1].get_title(), "Statistics of dog")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_4(self):
        # Test single input
        data = [{"cat": 1}]
        stats, axes = task_func(data)
        self.assertEqual(stats, {"cat": {"mean": 1.0, "std": 0.0}})
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_5(self):
        # Test handling zero
        data = [{"cat": 0, "dog": 0}, {"cat": 0, "dog": 0}, {"cat": 0, "dog": 0}]
        stats, axes = task_func(data)
        self.assertEqual(
            stats, {"cat": {"mean": 0.0, "std": 0.0}, "dog": {"mean": 0.0, "std": 0.0}}
        )
        self.assertEqual(axes[0].get_title(), "Statistics of cat")
        self.assertEqual(axes[1].get_title(), "Statistics of dog")
        for ax, key in zip(axes, stats):
            heights = [rect.get_height() for rect in ax.patches]
            self.assertListEqual(heights, list(stats[key].values()))
    def test_case_6(self):
        # Test correct handling of empty input
        with self.assertRaises(ValueError):
            task_func([])
    def test_case_7(self):
        # Test correct handling of incorrect input types
        with self.assertRaises(TypeError):
            task_func("not a list")
        with self.assertRaises(TypeError):
            task_func([123])
        with self.assertRaises(TypeError):
            task_func([{"cat": "not numeric"}])
    def test_case_8(self):
        # Test with a mix of positive and negative integers
        data = [
            {"apple": -2, "banana": 4},
            {"apple": -4, "banana": 6},
            {"apple": -6, "banana": 8},
        ]
        stats, _ = task_func(data)
        self.assertAlmostEqual(stats["apple"]["mean"], -4.0)
        self.assertAlmostEqual(stats["apple"]["std"], 1.632993161855452)
        self.assertAlmostEqual(stats["banana"]["mean"], 6.0)
        self.assertAlmostEqual(stats["banana"]["std"], 1.632993161855452)
    def test_case_9(self):
        # Test with floating point numbers
        data = [{"x": 0.5, "y": 1.5}, {"x": 2.5, "y": 3.5}, {"x": 4.5, "y": 5.5}]
        stats, _ = task_func(data)
        self.assertAlmostEqual(stats["x"]["mean"], 2.5)
        self.assertAlmostEqual(stats["x"]["std"], 1.632993161855452)
        self.assertAlmostEqual(stats["y"]["mean"], 3.5)
        self.assertAlmostEqual(stats["y"]["std"], 1.632993161855452)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)