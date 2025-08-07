import re
import hashlib

def task_func(input_str):
    # Remove all special characters, punctuation marks, and spaces
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
    
    # Hash the cleaned string with SHA256
    sha256_hash = hashlib.sha256(cleaned_str.encode()).hexdigest()
    
    return sha256_hash
import unittest
import hashlib
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with special characters and spaces
        result = task_func('Special $#! characters   spaces 888323')
        expected = hashlib.sha256('Specialcharactersspaces888323'.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test with a standard phrase
        result = task_func('Hello World!')
        expected = hashlib.sha256('HelloWorld'.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_3(self):
        # Test with numeric input
        result = task_func('1234567890')
        expected = hashlib.sha256('1234567890'.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_4(self):
        # Test with an empty string
        result = task_func('')
        expected = hashlib.sha256(''.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_5(self):
        # Test with a single word
        result = task_func('A')
        expected = hashlib.sha256('A'.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_6(self):
        # Test with only special characters
        result = task_func('$#!@%')
        expected = hashlib.sha256(''.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_7(self):
        # Test with leading and trailing whitespace
        result = task_func('   leading and trailing spaces   ')
        expected = hashlib.sha256('leadingandtrailingspaces'.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_8(self):
        # Test with mixed case and numbers
        result = task_func('Test123')
        expected = hashlib.sha256('Test123'.encode()).hexdigest()
        self.assertEqual(result, expected)
    def test_case_9(self):
        # Test with non-ASCII unicode characters
        result = task_func('Café123')
        expected = hashlib.sha256('Caf123'.encode()).hexdigest()  # Assumes non-ASCII chars are removed
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)