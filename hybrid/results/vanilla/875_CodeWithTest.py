import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Create a list of dictionaries from the data
    records = []
    for row in data:
        record = {columns[i]: value for i, value in enumerate(row)}
        records.append(record)
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(records, columns=columns)
    
    # Fill missing values if fill_missing is True
    if fill_missing:
        for col in columns:
            if df[col].isnull().any():
                if pd.api.types.is_numeric_dtype(df[col]):
                    # Fill numeric missing values with random numbers in the specified range
                    df[col].fillna(random.randint(*num_range), inplace=True)
                else:
                    # Fill non-numeric missing values with None
                    df[col].fillna(None, inplace=True)
    
    return df

# Example usage
data = [('Mango', 20), ('Apple', ), ('Banana', )]
df = task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=42)
print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_basic_functionality(self):
        # Testing basic functionality with complete data for each column
        data = [('John', 25, 'Engineer'), ('Alice', 30, 'Doctor')]
        df = task_func(data)
        expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_uneven_tuples(self):
        # Handling tuples of uneven length, missing elements should be filled with None
        data = [('John', 25, 'Engineer'), ('Alice', 30, 'Doctor'), ('Bob', )]
        df = task_func(data)
        expected_df = pd.DataFrame([['John', 25, 'Engineer'], ['Alice', 30, 'Doctor'], ['Bob', None, None]], columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_custom_columns(self):
        # Specifying custom column names
        data = [('Mango', 20), ('Apple', 30)]
        df = task_func(data, columns=['Fruit', 'Quantity'])
        expected_df = pd.DataFrame(data, columns=['Fruit', 'Quantity'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_empty_list(self):
        # Providing an empty list, resulting in an empty DataFrame with only the specified columns
        data = []
        df = task_func(data)
        expected_df = pd.DataFrame(columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_all_none(self):
        # All elements missing for a particular record
        data = [('John', 25, 'Engineer'), (None, None, None)]
        df = task_func(data)
        expected_df = pd.DataFrame([['John', 25, 'Engineer'], [None, None, None]], columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_random_fill(self):
        # Testing random data filling functionality
        data = [('John', 25, None), (None, None, None)]
        df = task_func(data, fill_missing=True, num_range=(1, 100), seed=42)
        # Check if missing values are filled and if the filled values are within the specified range
        self.assertTrue(df.loc[0, 'Occupation'] is None)
        self.assertTrue(df.loc[1, 'Name'] is None)
        self.assertTrue(df.loc[1, 'Age'] is not None and 1 <= df.loc[1, 'Age'] <= 100)
    def test_seed_reproducibility(self):
        # Testing if the seed parameter provides reproducible results
        data = [('John', None, None)]
        df1 = task_func(data, fill_missing=True, num_range=(1, 100), seed=42)
        df2 = task_func(data, fill_missing=True, num_range=(1, 100), seed=42)
        pd.testing.assert_frame_equal(df1, df2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)