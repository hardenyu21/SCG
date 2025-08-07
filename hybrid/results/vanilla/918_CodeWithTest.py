import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    # Define a function to replace acronyms in a single string
    def replace_acronyms(text):
        if pd.isna(text):
            return text
        # Use regex to find acronyms and replace them with full words
        return re.sub(r'\b(' + '|'.join(re.escape(key) for key in mapping.keys()) + r')\b', 
                      lambda match: mapping[match.group(0)], text)
    
    # Apply the replacement function to each element in the DataFrame
    return data.applymap(replace_acronyms)

# Example usage:
# df = pd.DataFrame({
#     'Column1': ['NASA is exploring space.', 'The EU is a union of countries.'],
#     'Column2': ['I love AI.', 'ML is a subset of AI.']
# })
# acronym_mapping = {'NASA': 'National Aeronautics and Space Administration',
#                    'EU': 'European Union',
#                    'AI': 'Artificial Intelligence',
#                    'ML': 'Machine Learning'}
# result_df = task_func(df, acronym_mapping)
# print(result_df)
import unittest
# Unit tests for the task_func function
class TestCases(unittest.TestCase):
    def test_acronyms_single_column(self):
        data = {'text': ['NASA rocks', 'Visit the USA']}
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected = pd.DataFrame({'text': ['National Aeronautics and Space Administration rocks', 'Visit the United States of America']})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_acronyms_multiple_columns(self):
        data = {'col1': ['NASA exploration'], 'col2': ['Made in USA']}
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected = pd.DataFrame({'col1': ['National Aeronautics and Space Administration exploration'], 'col2': ['Made in United States of America']})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_no_acronyms(self):
        data = {'text': ['A sunny day', 'A rainy night']}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': ['A sunny day', 'A rainy night']})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_non_string_types(self):
        data = {'text': ['NASA mission', 2020, None]}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': ['National Aeronautics and Space Administration mission', 2020, None]})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_empty_dataframe(self):
        data = {'text': []}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': []})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)