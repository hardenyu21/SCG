import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Flatten the list of lists and fill empty lists with random integers
    all_values = []
    for lst in list_of_lists:
        if not lst:
            lst.extend(random.randint(0, 100) for _ in range(size))
        all_values.extend(lst)
    
    # Calculate mean
    mean_value = np.mean(all_values)
    
    # Calculate median
    median_value = np.median(all_values)
    
    # Calculate mode
    mode_result = stats.mode(all_values)
    mode_value = mode_result.mode[0] if mode_result.count[0] > 0 else None
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }

# Example usage:
# list_of_lists = [[1, 2, 3], [], [4, 5, 6]]
# result = task_func(list_of_lists)
# print(result)
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with a mix of non-empty and empty lists.
        input_data = [[1, 2, 3], [], [4, 5, 6]]
        result = task_func(input_data)
        self.assertTrue(result["mean"] < 100)
        self.assertTrue(result["median"] < 100)
        self.assertTrue(result["mode"] < 100)
    def test_case_2(self):
        # Test with all non-empty lists.
        input_data = [[7, 8, 9], [10, 11, 12], [13, 14, 15]]
        result = task_func(input_data, 4)
        combined_data = [7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(result["mean"], np.mean(combined_data))
        self.assertEqual(result["median"], np.median(combined_data))
        self.assertEqual(result["mode"], stats.mode(combined_data).mode)
    def test_case_3(self):
        # Test with all empty lists.
        input_data = [[], [], []]
        result = task_func(input_data)
        self.assertTrue(result["mean"] < 100)
        self.assertTrue(result["median"] < 100)
        self.assertTrue(result["mode"] < 100)
    def test_case_4(self):
        # Test with lists containing both negative and positive integers.
        input_data = [[-1, -2, -3], [4, 5, 6], [-7, -8, -9]]
        result = task_func(input_data, 2)
        combined_data = [-1, -2, -3, 4, 5, 6, -7, -8, -9]
        self.assertEqual(result["mean"], np.mean(combined_data))
        self.assertEqual(result["median"], np.median(combined_data))
        self.assertEqual(result["mode"], stats.mode(combined_data).mode)
    def test_case_5(self):
        # Test with a single list.
        input_data = [[1, 2, 3, 4, 5]]
        result = task_func(input_data)
        self.assertEqual(result["mean"], np.mean(input_data[0]))
        self.assertEqual(result["median"], np.median(input_data[0]))
        self.assertEqual(result["mode"], stats.mode(input_data[0]).mode)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)