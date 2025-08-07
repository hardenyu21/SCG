import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    if num_digits > length:
        raise ValueError("Number of digits cannot be greater than the total length of the password.")
    
    # Generate the specified number of random digits
    digit_part = random.choices(DIGITS, k=num_digits)
    
    # Generate the remaining part of the password with random letters
    letter_part = random.choices(LETTERS, k=length - num_digits)
    
    # Combine both parts
    password_list = digit_part + letter_part
    
    # Shuffle the combined list to ensure randomness
    random.shuffle(password_list)
    
    # Join the list into a string and return
    return ''.join(password_list)

# Example usage:
# password = task_func(10, 3)
# print(password)
import unittest
class TestCases(unittest.TestCase):
    def test_valid_input(self):
        """
        Test Case 1: Valid Input
        - Verify that the function returns a password of the correct length.
        - Verify that the function returns a password with the correct number of digits.
        - Verify that the function returns a password with the correct number of letters.
        """
        password = task_func(10, 3)
        self.assertEqual(len(password), 10, "Password length should be 10")
        self.assertEqual(sum(c.isdigit() for c in password), 3, "Password should have 3 digits")
        self.assertEqual(sum(c.isalpha() for c in password), 7, "Password should have 7 letters")
    def test_length_zero(self):
        """
        Test Case 2: Length Zero
        - Verify that the function raises a ValueError when the length is zero.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for length 0"):
            task_func(0, 3)
    def test_negative_length(self):
        """
        Test Case 3: Negative Length
        - Verify that the function raises a ValueError when the length is negative.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for negative length"):
            task_func(-5, 3)
    def test_negative_num_digits(self):
        """
        Test Case 4: Negative Number of Digits
        - Verify that the function raises a ValueError when the number of digits is negative.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for negative num_digits"):
            task_func(10, -3)
    def test_num_digits_greater_than_length(self):
        """
        Test Case 5: Number of Digits Greater than Length
        - Verify that the function raises a ValueError when the number of digits is greater than the length.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError when num_digits > length"):
            task_func(5, 10)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)