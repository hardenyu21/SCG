import binascii
import string
import random

def task_func(length):
    # Generate a random hexadecimal string of the given length
    hex_string = ''.join(random.choices('0123456789abcdef', k=length))
    
    try:
        # Decode the hexadecimal string to ASCII
        ascii_string = binascii.unhexlify(hex_string).decode('ascii')
    except (binascii.Error, UnicodeDecodeError):
        # If decoding fails, return an empty string
        ascii_string = ''
    
    return ascii_string

# Example usage:
# print(task_func(10))
import unittest
import string
import random
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_correct_length(self):
        """Test the length of the hexadecimal string before decoding."""
        random.seed(2)
        length = 8
        HEX_CHARS = string.hexdigits.lower()
        hex_string = "".join(random.choice(HEX_CHARS) for _ in range(length))
        result = task_func(length)
        # Check if the length of the hexadecimal string before decoding is correct
        self.assertEqual(len(hex_string), length)
        self.assertEqual(result, "]")
    def test_correct_type(self):
        """Test the type of the output."""
        random.seed(4)
        result = task_func(6)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "y<")
    def test_non_empty_string_positive_length(self):
        """Test the output for a positive length."""
        random.seed(6)
        result = task_func(6)
        self.assertNotEqual(result, "")
        self.assertEqual(result, "\x10")
    def test_zero_length(self):
        """Test the output for a zero length."""
        random.seed(8)
        result = task_func(0)
        self.assertEqual(result, "")
    def test_negative_length_handling(self):
        """Test the output for a negative length."""
        random.seed(10)
        result = task_func(-1)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)