import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    # Check if the DataFrame contains the required columns
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError("The DataFrame must contain 'Name' and 'Score' columns.")
    
    # Group the DataFrame by 'Name' and calculate the average score for each name
    grouped = df.groupby('Name')['Score'].mean().reset_index()
    
    # Create a dictionary of generator objects
    gen_dict = {
        row['Name']: (lambda name=row['Name'], score=row['Score']: ((name, score),))()
        for _, row in grouped.iterrows()
    }
    
    return gen_dict

# Example usage
df_sample = pd.DataFrame({
    'Name': ['Micky', 'Donald', 'Girl'],
    'Score': [25.2, 9, -1]
})

gen_dict = task_func(df_sample)
print({key: next(value) for key, value in gen_dict.items()})
import unittest
import pandas as pd
from statistics import mean
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    def test_case_wrong_columns(self):
        df_sample1 = pd.DataFrame({
            'A': ['Tom', 'Nick', 'John', 'Tom', 'John'],
            'Score': [85, 79, 90, 88, 82]
        })
        self.assertRaises(Exception, task_func, df_sample1)
    
    def test_case_1(self):
        df_test = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John'],
            'Score': [85, 79, 90]
        })
        gen_dict = task_func(df_test)
        expected_result = {
            'John': ('John', 90),
            'Nick': ('Nick', 79),
            'Tom': ('Tom', 85)
        }
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_2(self):
        df_test = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
            'Score': [85, 79, 90, 88, 82]
        })
        gen_dict = task_func(df_test)
        expected_result = {
            'John': ('John', 86),
            'Nick': ('Nick', 79),
            'Tom': ('Tom', 86.5)
        }
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_3(self):
        df_test = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John', 'Anna', 'Elsa'],
            'Score': [85, 79, 90, 88, 82]
        })
        gen_dict = task_func(df_test)
        expected_result = {
            'Anna': ('Anna', 88),
            'Elsa': ('Elsa', 82),
            'John': ('John', 90),
            'Nick': ('Nick', 79),
            'Tom': ('Tom', 85)
        }
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_4(self):
        names = [fake.first_name() for _ in range(10)]
        scores = [fake.random_int(min=50, max=100) for _ in range(10)]
        df_test = pd.DataFrame({
            'Name': names,
            'Score': scores
        })
        gen_dict = task_func(df_test)
        grouped = df_test.groupby('Name')
        expected_result = {name: (name, mean(group['Score'])) for name, group in grouped}
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_5(self):
        df_test = pd.DataFrame({
            'Name': [],
            'Score': []
        })
        gen_dict = task_func(df_test)
        self.assertDictEqual(gen_dict, {})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)