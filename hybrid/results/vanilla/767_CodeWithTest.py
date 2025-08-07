from collections import Counter
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    # Replace each sublist with a random letter
    random_letters = [random.choice(LETTERS) for _ in list_of_lists]
    
    # Count each letter in the final list
    letter_count = Counter(random_letters)
    
    return dict(letter_count)

# Example usage:
# nested_list = [[1, 2], [3, 4], [5, 6]]
# print(task_func(nested_list))
import unittest
class TestCases(unittest.TestCase):
    # Input 1: Standard nested list with string values
    def test_case_1(self):
        result = task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        assert isinstance(result, dict)
        assert sum(result.values()) == 3
    # Input 2: Nested list with numerical values
    def test_case_2(self):
        result = task_func([[1, 2], [3, 4], [5, 6]])
        assert isinstance(result, dict)
        assert sum(result.values()) == 3
    # Input 3: Nested list with mixed string and numerical values
    def test_case_3(self):
        result = task_func([['Pizza', 1], [2, 'Coke'], ['Pasta', 3]])
        assert isinstance(result, dict)
        assert sum(result.values()) == 3
    # Input 4: Empty list
    def test_case_4(self):
        result = task_func([])
        assert isinstance(result, dict)
        assert sum(result.values()) == 0
    # Input 5: Nested list with a single sublist
    def test_case_5(self):
        result = task_func([['Pizza']])
        assert isinstance(result, dict)
        assert sum(result.values()) == 1


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)