import itertools
import json

def task_func(json_list, r):
    try:
        # Parse the JSON string
        data = json.loads(json_list)
        
        # Check if 'number_list' key exists
        if 'number_list' not in data:
            raise Exception("JSON data does not contain 'number_list' key.")
        
        # Extract the number list
        number_list = data['number_list']
        
        # Check if the number list is empty
        if not number_list:
            raise Exception("The 'number_list' is empty.")
        
        # Generate all combinations of r elements
        combinations = list(itertools.combinations(number_list, r))
        
        return combinations
    
    except json.JSONDecodeError:
        raise Exception("Invalid JSON input.")
    except Exception as e:
        raise e

# Example usage:
# json_input = '{"number_list": [1, 2, 3, 4]}'
# r = 2
# print(task_func(json_input, r))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('{"number_list": [1, 2, 3, 4, 5]}', 3)
        expected = [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func('{"number_list": ["a", "b", "c"]}', 2)
        expected = [('a', 'b'), ('a', 'c'), ('b', 'c')]
        self.assertEqual(result, expected)
    def test_case_3(self):
        result = task_func('{"number_list": [1, 2, 3]}', 1)
        expected = [(1,), (2,), (3,)]
        self.assertEqual(result, expected)
    def test_case_4(self):
        with self.assertRaises(Exception):
            result = task_func('[]', 1)
    def test_case_5(self):
        result = task_func('{"number_list": [1, 2]}', 3)
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)