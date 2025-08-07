import pandas as pd
import numpy as np
from random import choice, seed as set_seed

def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    # Validate the number of students
    if num_of_students <= 0:
        raise ValueError("num_of_students must be a positive integer.")
    
    # Set the random seed for reproducibility
    set_seed(seed)
    np.random.seed(seed)
    
    # Default lists if none are provided
    if name_list is None:
        name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    if gender_list is None:
        gender_list = ["Male", "Female", "Other"]
    
    # Generate random data
    names = [choice(name_list) for _ in range(num_of_students)]
    ages = np.random.randint(age_range[0], age_range[1] + 1, size=num_of_students)
    genders = [choice(gender_list) for _ in range(num_of_students)]
    scores = np.random.randint(score_range[0], score_range[1] + 1, size=num_of_students)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Name': names,
        'Age': ages,
        'Gender': genders,
        'Score': scores
    })
    
    return df
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_with_seed(self):
        df1 = task_func(5, seed=42)        
        df_list = df1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        expect = ['John,18,Male,78', 'Sara,17,Male,57', 'Mike,19,Male,70', 'John,16,Male,68', 'Nick,17,Female,60']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
        
    def test_reproducibility_with_seed(self):
        df1 = task_func(3, seed=123)
        df2 = task_func(3, seed=123)
        pd.testing.assert_frame_equal(df1, df2)
    def test_positive_num_students(self):
        df = task_func(5)
        self.assertEqual(len(df), 5)
    def test_invalid_num_students(self):
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_column_names(self):
        df = task_func(1)
        self.assertListEqual(list(df.columns), ['Name', 'Age', 'Gender', 'Score'])
    def test_age_range(self):
        df = task_func(10, age_range=(18, 22))
        self.assertTrue(all(18 <= age <= 22 for age in df['Age']))
    def test_custom_name_and_gender_list(self):
        custom_names = ['Alex', 'Bob']
        custom_genders = ['Non-Binary']
        df = task_func(2, name_list=custom_names, gender_list=custom_genders)
        self.assertIn(df.iloc[0]['Name'], custom_names)
        self.assertIn(df.iloc[0]['Gender'], custom_genders)
    def test_score_range(self):
        df = task_func(10, score_range=(60, 70))
        self.assertTrue(all(60 <= score <= 70 for score in df['Score']))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)