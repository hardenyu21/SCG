import pandas as pd
import re
import numpy as np

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def task_func(df, column):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"The column '{column}' does not exist in the DataFrame.")
    
    # Initialize a list to store all matches
    all_matches = []
    
    # Compile the regex pattern for efficiency
    regex = re.compile(PATTERN)
    
    # Iterate over each entry in the specified column
    for entry in df[column]:
        # Find all matches in the current entry
        matches = regex.findall(str(entry))
        # Extend the list of all matches
        all_matches.extend(matches)
    
    # Count the occurrences of each unique match
    match_counts = pd.Series(all_matches).value_counts()
    
    return match_counts

# Example usage:
# df = pd.DataFrame({'data': ['1234567890abcdef1234567890abcdef', 'abcdef1234567890abcdef1234567890', '1234567890abcdef1234567890abcdef']})
# print(task_func(df, 'data'))
import unittest
import pandas as pd
import re
from faker import Faker
# Constants for the test cases
PATTERN = r"([a-fA-F\d]{32})"
def generate_mock_dataframe(num_rows, include_hex=True):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        if include_hex:
            sentence = fake.sentence() + " " + fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', upper=False)
        else:
            sentence = fake.sentence()
        data.append(sentence)
    return pd.DataFrame({"text": data})
class TestCases(unittest.TestCase):
    def test_typical_use_case(self):
        df = generate_mock_dataframe(10, include_hex=True)
        result = task_func(df, "text")
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)
    def test_default(self):
        df = pd.DataFrame({"text": ["6f96cfdfe5ccc627cadf24b41725caa4 gorilla", 
                            "6f96cfdfe5ccc627cadf24b41725caa4 banana",
                            "1234567890abcdef1234567890abcdef apple"]})
        result = task_func(df, "text")
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)
    def test_no_matches(self):
        df = generate_mock_dataframe(10, include_hex=False)
        result = task_func(df, "text")
        self.assertTrue(result.empty)
    def test_mixed_data(self):
        df = generate_mock_dataframe(10, include_hex=True)
        df.loc[0, "text"] += " some-non-hex-string"
        result = task_func(df, "text")
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)
    def test_incorrect_column(self):
        df = generate_mock_dataframe(10, include_hex=True)
        with self.assertRaises(KeyError):
            task_func(df, "nonexistent_column")
    def test_large_dataset(self):
        df = generate_mock_dataframe(1000, include_hex=True)
        result = task_func(df, "text")
        self.assertIsInstance(result, pd.Series)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)