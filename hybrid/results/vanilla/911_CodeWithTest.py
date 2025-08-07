from functools import reduce
import operator
import string

def task_func(letters):
    # Create a dictionary mapping each uppercase letter to its corresponding number
    letter_to_number = {letter: index for index, letter in enumerate(string.ascii_uppercase, start=1)}
    
    # Map the input letters to their corresponding numbers using the dictionary
    numbers = [letter_to_number[letter] for letter in letters]
    
    # Calculate the product of the numbers using reduce and operator.mul
    product = reduce(operator.mul, numbers, 1)
    
    return product

# Example usage
print(task_func(["A", "E", "I"]))  # Output: 45
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: ["A", "B", "C"]
        # Expected Output: 6 (1 * 2 * 3)
        result = task_func(["A", "B", "C"])
        self.assertEqual(result, 6)
        
    def test_case_2(self):
        # Input: ["A", "E", "I"]
        # Expected Output: 45 (1 * 5 * 9)
        result = task_func(["A", "E", "I"])
        self.assertEqual(result, 45)
    def test_case_3(self):
        # Input: ["Z"]
        # Expected Output: 26
        result = task_func(["Z"])
        self.assertEqual(result, 26)
    def test_case_4(self):
        # Input: ["X", "Y", "Z"]
        # Expected Output: 24 * 25 * 26
        result = task_func(["X", "Y", "Z"])
        self.assertEqual(result, 24 * 25 * 26)
        
    def test_case_5(self):
        # Input: ["A", "A", "A"]
        # Expected Output: 1 (1 * 1 * 1)
        result = task_func(["A", "A", "A"])
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)