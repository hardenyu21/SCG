import codecs
import random
import string
import hashlib

def task_func(password_length=10, salt="salty"):
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    # Mix the password with the salt
    salted_password = password + salt
    
    # Hash the salted password using SHA256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    
    return hashed_password

# Example usage:
# hashed = task_func(12, "my_salt")
# print(hashed)
import unittest
import codecs
import random
import string
import hashlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with default parameters
        random.seed(0)
        hashed_password = task_func()
        self.assertEqual(len(hashed_password), 64)  # SHA256 produces a 64-character long hash
    def test_case_2(self):
        # Testing with custom password length but default salt
        random.seed(0)
        hashed_password = task_func(15)
        self.assertEqual(len(hashed_password), 64)
    def test_case_3(self):
        # Testing with default password length but custom salt
        random.seed(0)
        hashed_password = task_func(salt="custom_salt")
        self.assertEqual(len(hashed_password), 64)
    def test_case_4(self):
        # Testing with both custom password length and salt
        random.seed(0)
        hashed_password = task_func(20, "another_salt")
        self.assertEqual(len(hashed_password), 64)
    def test_case_5(self):
        # Testing with edge value for password length (e.g., very small value)
        random.seed(0)
        hashed_password = task_func(1)
        self.assertEqual(len(hashed_password), 64)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)