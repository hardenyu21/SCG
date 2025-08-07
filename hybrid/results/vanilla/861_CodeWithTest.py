from collections import Counter
from random import choice, seed

# Constants
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def task_func(list_of_lists, seed_value=None):
    if seed_value is not None:
        seed(seed_value)
    
    baskets = []
    for lst in list_of_lists:
        cart = Counter()
        for _ in range(len(lst)):
            item = choice(POSSIBLE_ITEMS)
            cart[item] += 1
        baskets.append(cart)
    
    return baskets

# Example usage:
# list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# print(task_func(list_of_lists, seed_value=42))
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with empty list
        result = task_func([])
        self.assertEqual(result, [])
    def test_case_2(self):
        # Testing with empty sublists
        result = task_func([[], [], []])
        for basket in result:
            self.assertEqual(basket, Counter())
        
    def test_case_3(self):
        # Testing with sublists of different lengths
        result = task_func([[1], [1, 2], [1, 2, 3]])
        self.assertEqual(len(result), 3)
        self.assertEqual(sum(result[0].values()), 1)
        self.assertEqual(sum(result[1].values()), 2)
        self.assertEqual(sum(result[2].values()), 3)
    def test_case_4(self):
        # Testing with sublists containing the same element
        result = task_func([[1, 1, 1], [2, 2, 2, 2]])
        self.assertEqual(len(result), 2)
        self.assertEqual(sum(result[0].values()), 3)
        self.assertEqual(sum(result[1].values()), 4)
        
    def test_case_5(self):
        # Testing with large sublists
        result = task_func([[1]*100, [2]*200])
        self.assertEqual(len(result), 2)
        self.assertEqual(sum(result[0].values()), 100)
        self.assertEqual(sum(result[1].values()), 200)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)