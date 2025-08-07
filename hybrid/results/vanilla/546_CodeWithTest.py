from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    # Sort the dictionary by keys
    sorted_dict = OrderedDict(sorted(my_dict.items()))
    
    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Key", "Value"]
    
    # Add rows to the table
    for key, value in sorted_dict.items():
        table.add_row([key, value])
    
    return table

# Example usage
if __name__ == "__main__":
    print(task_func({}))
import unittest
class TestCases(unittest.TestCase):
    def test_sort_and_display_dict(self):
        my_dict = {3: 'apple', 1: 'banana', 2: 'cherry'}
        table = task_func(my_dict)
        expected_header = '+-----+--------+'
        self.assertIn(expected_header, str(table))
        self.assertIn('banana', str(table))
    def test_empty_dict(self):
        table = task_func({})
        expected_header = '+-----+-------+'
        self.assertIn(expected_header, str(table))
    def test_single_element_dict(self):
        my_dict = {1: 'single'}
        table = task_func(my_dict)
        self.assertIn('single', str(table))
    def test_non_string_values(self):
        my_dict = {1: 100, 2: 200.5}
        table = task_func(my_dict)
        self.assertIn('100', str(table))
        self.assertIn('200.5', str(table))
    def test_string_keys(self):
        my_dict = {'a': 'apple', 'b': 'banana'}
        table = task_func(my_dict)
        self.assertIn('apple', str(table))
        self.assertIn('banana', str(table))
    def test_large_dict(self):
        my_dict = {i: str(i) for i in range(1000)}
        table = task_func(my_dict)
        self.assertEqual(len(table._rows), 1000)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)