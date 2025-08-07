import math
from sympy import isprime

def task_func(input_list):
    # Filter the prime numbers from the input list
    prime_numbers = [num for num in input_list if isprime(num)]
    
    # Sort the prime numbers based on their radian value converted to degrees
    sorted_primes = sorted(prime_numbers, key=lambda x: math.degrees(x))
    
    return sorted_primes

# Example usage
print(task_func([101, 102, 103, 104]))  # Output: [101, 103]
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_data = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 3, 5, 7]
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_2(self):
        input_data = [2, 3, 5, 7, 11, 13, 17, 19]
        expected_output = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_3(self):
        input_data = [4, 6, 8, 9, 10, 12, 14, 15, 16]
        expected_output = []
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_4(self):
        input_data = []
        expected_output = []
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_5(self):
        input_data = [89, 90, 91, 97, 98, 99, 100]
        expected_output = [89, 97]
        self.assertEqual(task_func(input_data), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)