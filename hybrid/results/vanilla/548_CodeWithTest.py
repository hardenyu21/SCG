import random
import string
import base64
import zlib

def task_func(string_length=100):
    # Generate a random string of specified length with uppercase letters and digits
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    
    # Compress the random string using zlib
    compressed_data = zlib.compress(random_string.encode('utf-8'))
    
    # Encode the compressed data in base64
    base64_encoded_data = base64.b64encode(compressed_data)
    
    # Convert the base64 bytes to a string and return
    return base64_encoded_data.decode('utf-8')

# Example usage:
# compressed_base64_string = task_func(100)
# print(compressed_base64_string)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        random.seed(1)
        result = task_func()
        self.assertEqual(result, 'eJwFwUEOhCAMAMAvLVBXONJooGqkUCDa/z/EmR3M0epjNwQ2sSr5P8a+3pkxcyPK9YwwnhRgv1RXdu85F5CJZEvq+t4sVkpD1DBLkmA6kPhRj+6jdcvPyeAPdLQbtg==')
    def test_case_2(self):
        random.seed(0)
        result = task_func(50)
        self.assertEqual(result, 'eJwzMQzwCvY38g4KMwv2Ngz3MrM0NvMxMIsMdAkIM7MIMvUyCnGM8jeOdAwy9fQxdQ/1tAAAVX8NdQ==')
    def test_case_3(self):
        random.seed(42)
        result = task_func(200)
        self.assertEqual(result, 'eJwFwVkCQCAQANArRZs+WzCTJIyU+x/Ee81GZF2F4uC20Agqt/zbl2kPQVTOyGTir3w+h5vHsL05Q9StrmzJpj1dDOhSBC1TO9QZ8YlVHWDu4MI7Fp8NTcJ+nWKbyznJeK9Kbq0uA41kk9WSJy+ncPlhmC+KsgAxSKaVe8a9IvgXlfDYYdbPNfI1lHKybsKxS1zPsqEukpwRP8dcNyU=')
    def test_case_4(self):
        random.seed(10)
        result = task_func(10)
        self.assertEqual(result, 'eJwLDQj1MDaOcAv2AQAQIQLm')
    def test_case_5(self):
        random.seed(1)
        result = task_func(1)
        self.assertEqual(result, 'eJxzBQAARgBG')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)