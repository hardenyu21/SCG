import pandas as pd
import string

def task_func(word):
    # Check if the input word is in lowercase and contains only alphabetic characters
    if not word.islower() or not word.isalpha():
        raise ValueError("The input word must be in lowercase and contain only alphabetic characters.")
    
    # Create a list of tuples containing each letter and its 1-based position in the alphabet
    data = [(letter, string.ascii_lowercase.index(letter) + 1) for letter in word]
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Letter', 'Position'])
    
    return df

# Example usage:
# df = task_func('zoo')
# print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_abc(self):
        """Test with the word 'abc'."""
        result = task_func('abc')
        expected = pd.DataFrame({'Letter': ['a', 'b', 'c'], 'Position': [1, 2, 3]})
        pd.testing.assert_frame_equal(result, expected)
    def test_xyz(self):
        """Test with the word 'xyz'."""
        result = task_func('xyz')
        expected = pd.DataFrame({'Letter': ['x', 'y', 'z'], 'Position': [24, 25, 26]})
        pd.testing.assert_frame_equal(result, expected)
    def test_mixed_case_error(self):
        """Test with a mixed case word, expecting a ValueError."""
        with self.assertRaises(ValueError):
            task_func('AbC')
    def test_non_alpha_error(self):
        """Test with a non-alphabetic word, expecting a ValueError."""
        with self.assertRaises(ValueError):
            task_func('123')
    def test_empty_string(self):
        """Test with an empty string, expecting an empty DataFrame."""
        result = task_func('')
        expected = pd.DataFrame({'Letter': [], 'Position': []})
        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)