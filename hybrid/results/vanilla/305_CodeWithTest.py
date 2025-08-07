from collections import Counter
import itertools
import random

# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def task_func(list_of_lists, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Fill empty lists with a random sample from the alphabet
    filled_lists = [
        sublist if sublist else random.sample(ALPHABET, len(ALPHABET))
        for sublist in list_of_lists
    ]
    
    # Flatten the list of lists into a single list of characters
    all_characters = list(itertools.chain.from_iterable(filled_lists))
    
    # Count the frequency of each letter
    letter_counter = Counter(all_characters)
    
    return letter_counter

# Example usage:
# list_of_lists = [['a', 'b', 'c'], [], ['d', 'e', 'f', 'g']]
# print(task_func(list_of_lists))
import unittest
from collections import Counter
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func([['a', 'b', 'c'], ['d', 'e', 'f']])
        expected = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func([['a', 'b', 'c'], [], ['d', 'e', 'f']])
        # Since the function can add random letters, we'll ensure that the known letters are counted correctly
        self.assertEqual(sum(result.values()), 16)  # 6 known letters + 10 random letters
    def test_case_3(self):
        result = task_func([[], [], []])
        # Here, the function should add 30 random letters (10 for each empty list)
        self.assertEqual(sum(result.values()), 30)
    def test_case_4(self):
        result = task_func([])
        # For an entirely empty input list, the result should also be an empty Counter
        self.assertEqual(result, Counter())
    def test_case_5(self):
        result = task_func([['x', 'y', 'z'], ['a', 'b', 'c']])
        expected = Counter({'x': 1, 'y': 1, 'z': 1, 'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)