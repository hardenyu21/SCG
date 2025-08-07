import numpy as np
import datetime

def task_func(arr):
    # Ensure the input is a numpy array
    arr = np.array(arr)
    
    # Function to reverse the order of words in a string
    def reverse_words(s):
        return ' '.join(s.split()[::-1])
    
    # Apply the reverse_words function to each element in the array
    reversed_arr = np.vectorize(reverse_words)(arr)
    
    return reversed_arr

# Example usage:
# arr = np.array(["hello.world", "this.is.a.test", "numpy.array.reverse"])
# print(task_func(arr))
import numpy as np
import unittest
import re
class TestCases(unittest.TestCase):
    """
    Define test cases for the task_func function.
    """
    
    def test_case_1(self):
        # Test description: 
        # Test reversing of words separated by '.' for a typical input.
        arr = np.array(['apple.orange', 'red.green.yellow'])
        result = task_func(arr)
        expected = np.array(['orange.apple', 'yellow.green.red'])
        np.testing.assert_array_equal(result, expected)
    def test_case_2(self):
        # Test description: 
        # Test reversing of words separated by '.' for another typical input.
        arr = np.array(['hello.world', 'this.is.a.test'])
        result = task_func(arr)
        expected = np.array(['world.hello', 'test.a.is.this'])
        np.testing.assert_array_equal(result, expected)
    def test_case_3(self):
        # Test description: 
        # Test input where words are not separated by '.', so they should remain unchanged.
        arr = np.array(['hello', 'world'])
        result = task_func(arr)
        expected = np.array(['hello', 'world'])
        np.testing.assert_array_equal(result, expected)
    def test_case_4(self):
        # Test description: 
        # Test input with empty strings. The result should also be empty strings.
        arr = np.array(['', ''])
        result = task_func(arr)
        expected = np.array(['', ''])
        np.testing.assert_array_equal(result, expected)
    def test_case_5(self):
        # Test description: 
        # Test reversing of words with a mix of uppercase and lowercase letters.
        arr = np.array(['OpenAI.GPT', 'GPT-4.is.amazing'])
        result = task_func(arr)
        expected = np.array(['GPT.OpenAI', 'amazing.is.GPT-4'])
        np.testing.assert_array_equal(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)