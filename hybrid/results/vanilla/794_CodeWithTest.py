import string
import random

BRACKETS = "(){}[]"

def task_func(length, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Create a pool of characters including lowercase letters and brackets
    char_pool = string.ascii_lowercase + BRACKETS
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(char_pool) for _ in range(length))
    
    return random_string

# Example usage:
string1 = task_func(34, random_seed=42)
print(string1)  # Output: hbrpoigf)cbfnobm(o{rak)vrjnvgfygww

string2 = task_func(23, random_seed=1)
print(string2)  # Output: ieqh]{[yng]by)a{rogubbb
import unittest
import string
class TestCases(unittest.TestCase):
    def setUp(self):
        self.BRACKETS = "(){}[]"
        return 
    def test_rng(self):
        # rng reproducability
        res1 = task_func(100, random_seed=42)
        res2 = task_func(100, random_seed=42)
        self.assertEqual(res1, res2)
    def test_case_1(self):
        # Testing with length = 5
        result = task_func(5, random_seed=1)
        self.assertEqual(len(result), 5)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
    def test_case_2(self):
        # Testing with length = 0 (edge case)
        result = task_func(0, random_seed=2)
        self.assertEqual(len(result), 0)
    def test_case_3(self):
        # Testing with length = 10
        result = task_func(10, random_seed=3)
        self.assertEqual(len(result), 10)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
    def test_case_4(self):
        # Testing with length = 1 (edge case)
        result = task_func(1, random_seed=34)
        self.assertEqual(len(result), 1)
        self.assertIn(result, string.ascii_lowercase + self.BRACKETS)
    def test_case_5(self):
        # Testing with length = 50
        result = task_func(50, random_seed=777)
        self.assertEqual(len(result), 50)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)