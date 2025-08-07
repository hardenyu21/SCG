import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()
    
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Fit and transform the column with LabelEncoder
    df[column_name] = label_encoder.fit_transform(df[column_name])
    
    # Return the DataFrame with the encoded column
    return df
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'apple', 'banana']})
        encoded_df = task_func(df, 'fruit')
        self.assertEqual(encoded_df['fruit'].tolist(), [0, 1, 2, 0, 1])
    def test_case_2(self):
        df = pd.DataFrame({'animal': ['cat', 'dog', 'bird', 'cat', 'bird']})
        encoded_df = task_func(df, 'animal')
        self.assertEqual(encoded_df['animal'].tolist(), [1, 2, 0, 1, 0])
    def test_case_3(self):
        df = pd.DataFrame({'color': ['red', 'blue', 'green', 'red', 'green']})
        encoded_df = task_func(df, 'color')
        self.assertEqual(encoded_df['color'].tolist(), [2, 0, 1, 2, 1])
    def test_case_4(self):
        df = pd.DataFrame({'vehicle': ['car', 'bus', 'train', 'car', 'train']})
        encoded_df = task_func(df, 'vehicle')
        self.assertEqual(encoded_df['vehicle'].tolist(), [1, 0, 2, 1, 2])
    def test_case_5(self):
        df = pd.DataFrame({'city': ['NYC', 'LA', 'SF', 'NYC', 'SF']})
        encoded_df = task_func(df, 'city')
        self.assertEqual(encoded_df['city'].tolist(), [1, 0, 2, 1, 2])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)