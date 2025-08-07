import pandas as pd
import os
import sys

def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column {column_name} does not exist in the DataFrame.")
    
    # Replace all occurrences of '\n' with '<br>' in the specified column
    df[column_name] = df[column_name].str.replace('\n', '<br>', regex=False)
    
    # Return the cleaned DataFrame
    return df
import unittest
import pandas as pd
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        os.mkdir('test')
        data = {
            'ID': [1, 2, 3],
            'Value': ["Hello\nWorld", "Python\nis\nawesome", "No newlines here"]
        }
        df = pd.DataFrame(data)
        df.to_csv('test/test_data_1.csv', index=False)
        data = {
            'ID': [1, 2],
            'Comments': ["Good\nMorning", "Happy\nCoding"]
        }
        df = pd.DataFrame(data)
        df.to_csv('test/test_data_2.csv', index=False)
        data = {
            'ID': [1, 2],
            'Text': ["Line 1", "Line 2\nLine 3"]
        }
        df = pd.DataFrame(data)
        df.to_csv('test/test_data_3.csv', index=False)
    def tearDown(self):
        os.remove('test/test_data_1.csv')
        os.remove('test/test_data_2.csv')
        os.remove('test/test_data_3.csv')
        os.rmdir('test')
    def test_case_1(self):
        df = task_func('test/test_data_1.csv', 'Value')
        self.assertEqual(df['Value'].iloc[0], "Hello<br>World")
        self.assertEqual(df['Value'].iloc[1], "Python<br>is<br>awesome")
        self.assertEqual(df['Value'].iloc[2], "No newlines here")
        
    def test_case_2(self):
        df = task_func('test/test_data_2.csv', 'Comments')
        self.assertEqual(df['Comments'].iloc[0], "Good<br>Morning")
        self.assertEqual(df['Comments'].iloc[1], "Happy<br>Coding")
        
    def test_case_3(self):
        df = task_func('test/test_data_3.csv', 'Text')
        self.assertEqual(df['Text'].iloc[0], "Line 1")
        self.assertEqual(df['Text'].iloc[1], "Line 2<br>Line 3")
        
    def test_case_4(self):
        df1 = task_func('test/test_data_1.csv', 'Value')
        df2 = task_func('test/test_data_1.csv', '')
        self.assertEqual(df1['Value'].iloc[0], "Hello<br>World")
        self.assertEqual(df2['Value'].iloc[0], "Hello\nWorld")
        
    def test_case_5(self):
        df1 = task_func('test/test_data_1.csv', 'Value')
        df2 = task_func('test/test_data_1.csv', 'NonExistentColumn')
        self.assertEqual(df1['Value'].iloc[0], "Hello<br>World")
        self.assertEqual(df2['Value'].iloc[0], "Hello\nWorld")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)