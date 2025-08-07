import codecs
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    # Randomly select a hex string from the list
    random_hex = random.choice(hex_keys)
    
    # Convert the hex string to an integer
    int_value = int(random_hex, 16)
    
    # Convert the integer to a float using struct
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
    
    # Encode the float as a UTF-8 string
    float_str = str(float_value)
    utf8_encoded = float_str.encode('utf-8')
    
    return utf8_encoded

# Example usage
result = task_func()
print(result)
import unittest
class TestCases(unittest.TestCase):
    def test_default_functionality(self):
        """Test the function with default parameters."""
        result = task_func()
        self.assertIsInstance(result, bytes)  # Check if output is correctly encoded in UTF-8
    def test_custom_hex_keys(self):
        """Test the function with a custom list of hexadecimal keys."""
        custom_keys = ['1A2FC614', '1B0FC614', '1C9FC614']
        result = task_func(hex_keys=custom_keys)
        self.assertIsInstance(result, bytes)
    def test_empty_list(self):
        """Test the function with an empty list."""
        with self.assertRaises(IndexError):  # Assuming random.choice will raise IndexError on empty list
            task_func(hex_keys=[])
    def test_consistency_of_output(self):
        """Ensure that the output is consistent with a fixed seed."""
        random.seed(42)  # Set the seed for predictability
        first_result = task_func()
        random.seed(42)  # Reset seed to ensure same choice is made
        second_result = task_func()
        self.assertEqual(first_result, second_result)
    def test_invalid_hex_key(self):
        """Test with an invalid hex key."""
        invalid_keys = ['ZZZZZZZZ', 'XXXX']
        with self.assertRaises(ValueError):
            task_func(hex_keys=invalid_keys)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)