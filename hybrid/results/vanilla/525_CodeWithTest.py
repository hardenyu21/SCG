import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a defaultdict to store lists of values for each key
    values_dict = defaultdict(list)
    
    # Collect values for each key
    for entry in data:
        for key, value in entry.items():
            values_dict[key].append(value)
    
    # Calculate mean and median for each key
    result = {}
    for key, values in values_dict.items():
        mean_value = np.mean(values)
        median_value = np.median(values)
        result[key] = {'mean': mean_value, 'median': median_value}
    
    # Create bar charts for each key
    plots = []
    for key, stats in result.items():
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [stats['mean'], stats['median']])
        ax.set_title(f'Statistics for {key}')
        ax.set_ylabel('Value')
        plots.append(ax)
    
    # Return the results and plots
    return result, plots

# Example usage:
# result, plots = task_func('data.json')
# for plot in plots:
#     plot.show()
import matplotlib
import unittest
import tempfile
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_data = {
            "test_1.json": [{"a": 2, "b": 4}, {"a": 4, "b": 8}],
            "test_2.json": [{"x": 1}, {"y": 2}, {"z": 6}],
            "invalid.json": {"not": "valid"},
            "empty.json": [],
        }
        # Generate test files
        for filename, content in self.test_data.items():
            with open(os.path.join(self.temp_dir.name, filename), "w") as f:
                json.dump(content, f)
    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        # Check plot generation
        expected_titles = ["a", "b"]
        _, plots = task_func(os.path.join(self.temp_dir.name, "test_1.json"))
        self.assertEqual(len(plots), len(expected_titles))
        for plot, title in zip(plots, expected_titles):
            assert isinstance(plot, matplotlib.axes._axes.Axes)
            self.assertTrue(plot.get_title(), f"Statistics of {title}")
    def test_case_2(self):
        # Check result correctness
        results, _ = task_func(os.path.join(self.temp_dir.name, "test_1.json"))
        self.assertIn("a", results)
        self.assertIn("b", results)
        self.assertEqual(results["a"]["mean"], 3.0)
        self.assertEqual(results["a"]["median"], 3.0)
        self.assertEqual(results["b"]["mean"], 6.0)
        self.assertEqual(results["b"]["median"], 6.0)
    def test_case_3(self):
        # Test with invalid data structure (not a list of dicts)
        with self.assertRaises(AttributeError):
            task_func(os.path.join(self.temp_dir.name, "invalid.json"))
    def test_case_4(self):
        # Test with empty data
        results, plots = task_func(os.path.join(self.temp_dir.name, "empty.json"))
        self.assertEqual(results, {})
        self.assertEqual(len(plots), 0)
    def test_case_5(self):
        # Test handling nested dicts with one key each
        results, _ = task_func(os.path.join(self.temp_dir.name, "test_2.json"))
        self.assertIn("x", results)
        self.assertIn("y", results)
        self.assertIn("z", results)
        self.assertEqual(results["x"]["mean"], 1.0)
        self.assertEqual(results["x"]["median"], 1.0)
        self.assertEqual(results["y"]["mean"], 2.0)
        self.assertEqual(results["y"]["median"], 2.0)
        self.assertEqual(results["z"]["mean"], 6.0)
        self.assertEqual(results["z"]["median"], 6.0)
    def test_case_6(self):
        # Test with nonexistent filename
        with self.assertRaises(FileNotFoundError):
            task_func(os.path.join(self.temp_dir.name, "NOTEXISTS.json"))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)