import string
import random

def task_func(text, seed=None):
    if not text:
        raise ValueError("The input text is empty.")
    
    if seed is not None:
        random.seed(seed)
    
    password = []
    
    for char in text:
        if char.isalpha():
            password.append(random.choice(string.ascii_lowercase))
        elif char.isdigit():
            password.append(str(random.randint(0, 9)))
        elif char.isspace():
            password.append(random.choice(string.ascii_lowercase + string.digits))
        else:
            password.append(char)
    
    return ''.join(password)

# Example usage:
# print(task_func("Hello World! 123", seed=42))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        result = task_func("Hello123", seed=1)
        self.assertEqual(len(result), 8)
        for i, char in enumerate("Hello123"):
            if char.isalpha():
                self.assertTrue(result[i].isalpha())
            elif char.isdigit():
                self.assertTrue(result[i].isdigit())
    def test_case_2(self):
        # Test basic case with alphabet only
        result = task_func("ABC", seed=2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(char.isalpha() for char in result))
    def test_case_3(self):
        # Test basic case with digit only
        result = task_func("123", seed=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(char.isdigit() for char in result))
    def test_case_4(self):
        # Test basic case with whitespace, alphabet, number, special char
        text = "Hello, world!"
        result = task_func(text, seed=4)
        self.assertEqual(len(result), 13)
        for i, char in enumerate(text):
            result_char = result[i]
            if char.isalpha():
                self.assertTrue(result_char.isalpha())
            elif char.isdigit():
                self.assertTrue(result_char.isdigit())
            elif char == " ":
                self.assertTrue(result_char.isalnum())
            else:
                self.assertEqual(result[i], char)
    def test_case_5(self):
        # Test handling empty string
        with self.assertRaises(Exception):
            task_func("", seed=5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)