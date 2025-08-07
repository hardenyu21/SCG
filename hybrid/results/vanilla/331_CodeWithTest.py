import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=100):
    # Generate a random sorted list of integers
    random_list = sorted(random.randint(min_value, max_value) for _ in range(list_length))
    
    # Insert the number into the sorted list while maintaining order
    bisect.insort(random_list, num)
    
    # Return the original random list and the new sorted list
    return (random_list[:-1], random_list)

# Example usage:
# result = task_func(42)
# print(result)
import unittest
from unittest.mock import patch
import random
class TestCases(unittest.TestCase):
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_into_empty_list(self, mock_randint):
        random.seed(0)
        result = task_func(15, 0, 5, 60)
        self.assertEqual(result, ([], [15]))
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_into_existing_list(self, mock_randint):
        random.seed(0)
        result = task_func(15, 5, 10, 60)
        self.assertEqual(result, ([12, 23, 34, 45, 56], [12, 15, 23, 34, 45, 56]))
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_at_beginning(self, mock_randint):
        random.seed(0)
        result = task_func(4, 4, 10, 60)
        self.assertEqual(result, ([12, 23, 34, 45], [4, 12, 23, 34, 45]))
    # @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_at_end(self):
        random.seed(0)
        result = task_func(15, 4, 10, 10)
        self.assertEqual(result, ([10, 10, 10, 10], [10, 10, 10, 10, 15]))
    @patch('random.randint', side_effect=[12, 34, 56])
    def test_insert_in_middle(self, mock_randint):
        random.seed(0)
        result = task_func(15, 3, 10, 60)
        self.assertEqual(result, ([12, 34, 56], [12, 15, 34, 56]))
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_random_list_length(self, mock_randint):
        random.seed(0)
        result = task_func(15, 5, 10, 20)
        self.assertEqual(len(result[0]), 5)
        self.assertIn(15, result[1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)