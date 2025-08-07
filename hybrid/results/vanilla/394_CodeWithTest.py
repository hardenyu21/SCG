import collections
import string
import random

def task_func(length, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Generate a random string of the given length using ASCII letters
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    
    # Calculate the frequency of each character in the generated string
    frequency = collections.Counter(random_string)
    
    return dict(frequency)

# Example usage:
# print(task_func(10))
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(0, 77)
        self.assertEquals(result, {})
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
    def test_case_2(self):
        result = task_func(1)
        self.assertIsInstance(result, dict)
        self.assertEqual(sum(result.values()), 1)
        self.assertEqual(len(result), 1)
    def test_case_3(self):
        length = 10000
        result = task_func(length, 34)
        self.assertIsInstance(result, dict)
        self.assertEqual(sum(result.values()), length)
        self.assertTrue(all(char in string.ascii_letters for char in result))
    def test_case_4(self):
        length = 10
        result = task_func(length, 77)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'Z': 1, 'q': 1, 'u': 1, 'm': 2, 'p': 1, 'h': 1, 's': 1, 'E': 1, 'J': 1})
        self.assertTrue(all(char in string.ascii_letters for char in result))
    def test_case_5(self):
        length = random.randint(1, 1000)
        result = task_func(length)
        self.assertIsInstance(result, dict)
        self.assertEqual(sum(result.values()), length)
        self.assertTrue(all(char in string.ascii_letters for char in result))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)