import re
import pandas as pd

def task_func(input_df):
    # Define a function to clean the text
    def clean_text(text):
        # Remove all special characters, punctuation marks, and spaces
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text)
        return cleaned

    # Apply the clean_text function to the 'text' column
    input_df['clean_text'] = input_df['text'].apply(clean_text)

    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].apply(len)

    return input_df
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'text': ['hello', 'world', 'Special $#! characters   spaces 888323', 'Hello, World!', '', None]})
    def test_clean_text_and_calculate_length(self):
        result = task_func(self.df)
        expected_clean_text = ['hello', 'world', 'Specialcharactersspaces888323', 'HelloWorld', '', '']
        expected_text_length = [5, 5, 29, 10, 0, 0]
        pd.testing.assert_series_equal(result['clean_text'], pd.Series(expected_clean_text, name='clean_text'), check_names=False)
        pd.testing.assert_series_equal(result['text_length'], pd.Series(expected_text_length, name='text_length'), check_names=False)
    def test_with_special_characters(self):
        df = pd.DataFrame({'text': ['@@@hello***', '%%%world$$$']})
        result = task_func(df)
        self.assertEqual(result['clean_text'].iloc[0], 'hello')
        self.assertEqual(result['clean_text'].iloc[1], 'world')
        self.assertEqual(result['text_length'].iloc[0], 5)
        self.assertEqual(result['text_length'].iloc[1], 5)
    def test_with_numeric_strings(self):
        df = pd.DataFrame({'text': ['123', '4567']})
        result = task_func(df)
        self.assertEqual(result['clean_text'].iloc[0], '123')
        self.assertEqual(result['clean_text'].iloc[1], '4567')
        self.assertEqual(result['text_length'].iloc[0], 3)
        self.assertEqual(result['text_length'].iloc[1], 4)
    def test_empty_and_none(self):
        df = pd.DataFrame({'text': ['', None]})
        result = task_func(df)
        self.assertEqual(result['clean_text'].iloc[0], '')
        self.assertEqual(result['clean_text'].iloc[1], '')
        self.assertEqual(result['text_length'].iloc[0], 0)
        self.assertEqual(result['text_length'].iloc[1], 0)
    def test_mixed_cases(self):
        df = pd.DataFrame({'text': ['HelloWorld', 'HELLOworld123']})
        result = task_func(df)
        self.assertEqual(result['clean_text'].iloc[0], 'HelloWorld')
        self.assertEqual(result['clean_text'].iloc[1], 'HELLOworld123')
        self.assertEqual(result['text_length'].iloc[0], 10)
        self.assertEqual(result['text_length'].iloc[1], 13)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)