import base64
import pandas as pd

def task_func(data_dict):
    # Convert the dictionary to a Pandas DataFrame
    df = pd.DataFrame(data_dict)
    
    # Convert the DataFrame to CSV format
    csv_data = df.to_csv(index=False)
    
    # Encode the CSV data to bytes
    csv_bytes = csv_data.encode('utf-8')
    
    # Encode the bytes to a Base64 string
    base64_encoded = base64.b64encode(csv_bytes).decode('utf-8')
    
    return base64_encoded
import unittest
from io import StringIO
class TestCases(unittest.TestCase):
    def test_encode_basic_dataframe(self):
        df = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_with_different_columns(self):
        df = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_empty_dataframe(self):
        df = {'X': [], 'Y': []}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv, check_dtype=False, check_index_type=False)
    def test_encode_with_specific_values(self):
        df = {'ID': [101, 102, 103], 'Score': [85, 90, 88]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_with_string_values(self):
        df = {'City': ['NY', 'LA'], 'Population': [8000000, 4000000]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)