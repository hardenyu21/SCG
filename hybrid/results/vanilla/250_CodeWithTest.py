import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Flatten the list of lists to handle any nested lists
    flattened_data = list(itertools.chain.from_iterable(data_list))
    
    # Filter out non-numeric values
    numeric_values = [value for value in flattened_data if isinstance(value, (int, float))]
    
    # Calculate the mean of the numeric values
    if numeric_values:
        mean_value = np.mean(numeric_values)
    else:
        mean_value = 0  # or handle the case where there are no numeric values
    
    # Create a dictionary with the mean value for each position
    result = {f'Position {i}': mean_value for i in range(len(data_list))}
    
    # Export the results to a JSON file if a file name is provided
    if json_file_name:
        with open(json_file_name, 'w') as json_file:
            json.dump(result, json_file, indent=4)
    
    return result

# Example usage:
data = [
    [1, 2, 3],
    [4, 5, 'a'],
    [7, 8, 9]
]

mean_values = task_func(data)
print(mean_values)
import unittest
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.json_file = tempfile.NamedTemporaryFile(delete=False)
    def tearDown(self):
        self.json_file.close()
    def test_case_1(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        expected_output = {'Position 1': 3.0, 'Position 2': 4.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
    def test_case_2(self):
        data_list = [('a', 10, 20), ('b', 20, 30), ('c', 30, 40)]
        expected_output = {'Position 1': 20.0, 'Position 2': 30.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
    def test_case_3(self):
        data_list = [('a', 5), ('b', 10), ('c', 15)]
        expected_output = {'Position 1': 10.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
    def test_case_4(self):
        data_list = [('a', 1, 2, 3), ('b', 4, 5, 6), ('c', 7, 8, 9)]
        expected_output = {'Position 1': 4.0, 'Position 2': 5.0, 'Position 3': 6.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
        
    def test_case_5(self):
        # Test with JSON file export
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4)]
        expected_output = {'Position 1': 2.0, 'Position 2': 3.0}
        result = task_func(data_list, json_file_name=self.json_file.name)
        self.assertEqual(result, expected_output)
        with open(self.json_file.name, "r") as f:
            json_output = json.load(f)
        self.assertEqual(json_output, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)