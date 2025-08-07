import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Remove punctuation using regex
    text_no_punctuation = re.sub(f"[{re.escape(PUNCTUATION)}]", "", text)
    # Convert text to lowercase
    text_lower = text_no_punctuation.lower()
    # Split text into words
    cleaned_words = text_lower.split()
    return cleaned_words

# Example usage:
# text = "Hello, World! This is a test."
# print(task_func(text))
# Output: ['hello', 'world', 'this', 'is', 'a', 'test']
import unittest
class TestCases(unittest.TestCase):
    def test_standard_input(self):
        """Test with standard input containing words, punctuation, and whitespaces"""
        input_text = "Hello, world! This is a test."
        expected_output = ['hello', 'world', 'this', 'is', 'a', 'test']
        self.assertEqual(task_func(input_text), expected_output)
    def test_empty_string(self):
        """Test with an empty string"""
        input_text = ""
        expected_output = ['']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_no_punctuation(self):
        """Test with a string that has no punctuation marks"""
        input_text = "Python is great"
        expected_output = ['python', 'is', 'great']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_numbers(self):
        """Test with a string that includes numbers and punctuation"""
        input_text = "1234! Test with numbers."
        expected_output = ['1234', 'test', 'with', 'numbers']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_special_characters(self):
        """Test with a string that includes special characters"""
        input_text = "Special chars @#$%^&*()"
        expected_output = ['special', 'chars', '']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_whitespaces(self):
        """Test with a string that includes extra whitespaces between words"""
        input_text = "   Extra   whitespaces   "
        expected_output = ['', 'extra', 'whitespaces', '']
        self.assertEqual(task_func(input_text), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)