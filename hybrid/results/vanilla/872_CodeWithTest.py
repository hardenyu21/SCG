import numpy as np
import itertools

def task_func(data_list):
    if not data_list:
        return []

    # Determine the maximum length of tuples
    max_length = max(len(t) for t in data_list)

    # Pad tuples with None to make them the same length
    padded_data = [t + (None,) * (max_length - len(t)) for t in data_list]

    # Unzip the padded data
    unzipped_data = list(itertools.zip_longest(*padded_data))

    # Calculate the mean for each position
    means = []
    for position in unzipped_data:
        numeric_values = [x for x in position if isinstance(x, (int, float))]
        if numeric_values:
            means.append(np.mean(numeric_values))
        else:
            means.append(np.nan)

    return means
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_regular_input(self):
        # Test with regular input data
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        expected_result = [np.nan, 3.0, 4.0]  # Expected mean values
        result = task_func(data_list)
        np.testing.assert_almost_equal(result, expected_result)
    def test_non_numeric_values(self):
        # Test with non-numeric values in the tuples
        data_list = [('a', 'x', 2), ('b', 2, 3), ('c', 'y', 4), ('d', 4, 'z'), ('e', 'k', 6)]
        expected_result = [np.nan, 3.0, 3.75]  # Expected mean values, non-numeric items are ignored
        result = task_func(data_list)
        np.testing.assert_equal(result, expected_result)
    def test_uneven_tuples(self):
        # Test with uneven tuple lengths
        data_list = [('a', 1), ('b', 2, 3), ('c',), ('d', 4, 5, 6), ('e', 5, 6)]
        expected_result = [np.nan, 3.0, 4.66666666, 6.0]  # Expected mean values
        result = task_func(data_list)
        np.testing.assert_almost_equal(result, expected_result)
    def test_all_non_numeric(self):
        # Test where all elements are non-numeric
        data_list = [('a', 'x'), ('b', 'y'), ('c', 'z'), ('d', 'k'), ('e', 'l')]
        expected_result = [np.nan, np.nan]  # No numeric data to calculate the mean
        result = task_func(data_list)
        np.testing.assert_equal(result, expected_result)
    def test_empty_input(self):
        # Test with an empty input list
        data_list = []
        expected_result = []  # No data to process
        result = task_func(data_list)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)