import pandas as pd
import numpy as np

def task_func(list_of_lists):
    series_list = []
    for sub_list in list_of_lists:
        # Create a list of integers from 1 to the length of the sub-list
        values = list(range(1, len(sub_list) + 1))
        # Shuffle the list of integers
        np.random.shuffle(values)
        # Create a pandas Series with the shuffled values and the sub-list as the index
        series = pd.Series(values, index=sub_list)
        # Append the Series to the list
        series_list.append(series)
    return series_list

# Example usage:
# list_of_lists = [['a', 'b', 'c'], ['x', 'y'], ['m', 'n', 'o', 'p']]
# series_list = task_func(list_of_lists)
# for series in series_list:
#     print(series)
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""
    def test_basic_functionality(self):
        """Test basic functionality of the function."""
        np.random.seed(0)
        input_data = [["x", "y", "z"], ["a", "b", "c"]]
        result = task_func(input_data)
        self.assertEqual(len(result), 2)
        expected_indexes = [["x", "y", "z"], ["a", "b", "c"]]
        for i, s in enumerate(result):
            self.assertIsInstance(s, pd.Series)
            self.assertListEqual(list(s.index), expected_indexes[i])
    def test_different_lengths(self):
        """Test with sub-lists of different lengths."""
        np.random.seed(1)
        input_data = [["m", "n"], ["p", "q", "r", "s"]]
        result = task_func(input_data)
        self.assertEqual(len(result), 2)
        expected_indexes = [["m", "n"], ["p", "q", "r", "s"]]
        for i, s in enumerate(result):
            self.assertIsInstance(s, pd.Series)
            self.assertListEqual(list(s.index), expected_indexes[i])
    def test_single_element_list(self):
        """Test with a single-element sub-list."""
        np.random.seed(2)
        input_data = [["a"]]
        result = task_func(input_data)
        self.assertEqual(len(result), 1)
        expected_indexes = [["a"]]
        for i, s in enumerate(result):
            self.assertIsInstance(s, pd.Series)
            self.assertListEqual(list(s.index), expected_indexes[i])
    def test_mixed_lengths(self):
        """Test with sub-lists of different lengths."""
        np.random.seed(3)
        input_data = [["x", "y", "z"], ["a", "b"]]
        result = task_func(input_data)
        self.assertEqual(len(result), 2)
        expected_indexes = [["x", "y", "z"], ["a", "b"]]
        for i, s in enumerate(result):
            self.assertIsInstance(s, pd.Series)
            self.assertListEqual(list(s.index), expected_indexes[i])
    def test_multiple_series(self):
        """Test with multiple sub-lists."""
        np.random.seed(4)
        input_data = [["x", "y"], ["a", "b"], ["m", "n", "o"]]
        result = task_func(input_data)
        self.assertEqual(len(result), 3)
        expected_indexes = [["x", "y"], ["a", "b"], ["m", "n", "o"]]
        for i, s in enumerate(result):
            self.assertIsInstance(s, pd.Series)
            self.assertListEqual(list(s.index), expected_indexes[i])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)