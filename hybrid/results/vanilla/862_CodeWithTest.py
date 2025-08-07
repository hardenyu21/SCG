import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Create a defaultdict with list as the default factory
    letter_dict = defaultdict(list)
    
    # Generate 'n' random letters
    for _ in range(n):
        # Randomly choose a letter from the alphabet
        letter = random.choice(string.ascii_lowercase)
        # Append the letter to its corresponding list in the dictionary
        letter_dict[letter].append(letter)
    
    return letter_dict

# Example usage
print(task_func(30, seed=1))
import unittest
from collections import defaultdict
import string
import random
class TestCases(unittest.TestCase):
    def test_return_type(self):
        result = task_func(10, seed=1)
        self.assertIsInstance(result, defaultdict)
        for key, value in result.items():
            self.assertIsInstance(value, list)
    def test_dictionary_keys(self):
        result = task_func(100, seed=2)
        for key in result.keys():
            self.assertTrue('a' <= key <= 'z')
    def test_random_seed_effect(self):
        result1 = task_func(50, seed=3)
        result2 = task_func(50, seed=3)
        self.assertEqual(result1, result2)
    def test_letters_distribution(self):
        n = 60
        result = task_func(n, seed=4)
        total_letters = sum(len(lst) for lst in result.values())
        self.assertEqual(total_letters, n)
    def test_edge_cases(self):
        result = task_func(0, seed=5)
        for lst in result.values():
            self.assertEqual(len(lst), 0)
        large_n = 10000
        result = task_func(large_n, seed=6)
        total_letters = sum(len(lst) for lst in result.values())
        self.assertEqual(total_letters, large_n)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)