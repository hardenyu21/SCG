import re
import pandas as pd

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    # Helper function to reverse words matching the pattern
    def reverse_matching_words(text: str, pattern: str) -> str:
        # Split the text into words
        words = text.split()
        
        # Function to check if a word matches the pattern
        def matches_pattern(word: str) -> bool:
            return re.match(pattern, word) is not None
        
        # Separate words into matching and non-matching
        matching_words = [word for word in words if matches_pattern(word)]
        non_matching_words = [word for word in words if not matches_pattern(word)]
        
        # Reverse the order of matching words
        matching_words.reverse()
        
        # Merge the words back together, maintaining original order for non-matching
        result = []
        matching_index = 0
        for word in words:
            if matches_pattern(word):
                result.append(matching_words[matching_index])
                matching_index += 1
            else:
                result.append(word)
        
        return ' '.join(result)
    
    # If the pattern is empty, return the original DataFrame
    if not pattern:
        return df.copy()
    
    # Apply the helper function to the specified column
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].apply(lambda x: reverse_matching_words(x, pattern))
    
    return df_copy
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Example df to test for error handling
        self.df = pd.DataFrame(
            {"A": ["blue car red", "green apple yellow"], "B": [3, 4]}
        )
    def test_case_1(self):
        # Test case where no words match the pattern
        df = pd.DataFrame({"Text": ["apple orange", "blue red"], "Number": [1, 2]})
        pattern = r"\b(?:banana|green)\b"
        expected = df.copy()
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_2(self):
        # Test case where all words in a column match the pattern
        df = pd.DataFrame({"Text": ["apple banana", "banana apple"], "Number": [1, 2]})
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame(
            {"Text": ["banana apple", "apple banana"], "Number": [1, 2]}
        )
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_3(self):
        # Test case with a mix of matching and non-matching words
        df = pd.DataFrame(
            {"Text": ["apple orange banana", "blue apple green"], "Number": [1, 2]}
        )
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame(
            {"Text": ["banana orange apple", "blue apple green"], "Number": [1, 2]}
        )
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_4(self):
        # Test case where the column contains an empty string
        df = pd.DataFrame({"Text": ["", "apple banana"], "Number": [1, 2]})
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame({"Text": ["", "banana apple"], "Number": [1, 2]})
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_5(self):
        # Test case where the pattern is an empty string (matches nothing)
        df = pd.DataFrame({"Text": ["apple orange", "banana apple"], "Number": [1, 2]})
        pattern = ""
        expected = df.copy()
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_6(self):
        # Test the function with a column name that does not exist in the DataFrame
        with self.assertRaises(KeyError):
            task_func(self.df, "NonexistentColumn", r"\b(?:car|apple|yellow)\b")
    def test_case_7(self):
        # Test the function with a non-string column name
        with self.assertRaises(KeyError):
            task_func(self.df, 123, r"\b(?:car|apple|yellow)\b")
    def test_case_8(self):
        # Test the function with an invalid regular expression pattern
        with self.assertRaises(re.error):
            task_func(self.df, "A", r"\b(?:car|apple|yellow")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)