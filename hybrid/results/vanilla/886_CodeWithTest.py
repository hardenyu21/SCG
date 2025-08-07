import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the dictionary has the required keys
    required_keys = {'Name', 'Age', 'Scores'}
    if not all(key in data for key in required_keys):
        raise ValueError("The dictionary does not have the required keys.")
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Sort the DataFrame by 'Name' and 'Age' in ascending order
    df_sorted = df.sort_values(by=['Name', 'Age'], ascending=[True, True])
    
    # Calculate the average score per student
    df['Average Score'] = df['Scores'].apply(lambda scores: sum(scores) / len(scores) if scores else None)
    average_scores_series = df.set_index('Name')['Average Score']
    
    # Find the most common age
    if df['Age'].empty:
        most_common_age = None
    else:
        age_counts = Counter(df['Age'])
        most_common_age = age_counts.most_common(1)[0][0]
    
    return df_sorted, average_scores_series, most_common_age
import unittest
import pandas as pd
import os
class TestCases(unittest.TestCase):
    def test_wrong_keys(self):
        # Testing with incorrect dictionary keys
        data = {
            'Names': ['Tom', 'Nick'],
            'Ages': [20, 21],
            'Scores': [85, 79]
        }
        with self.assertRaises(ValueError):
            task_func(data)
    def test_correct_processing(self):
        # Testing with correctly formatted data
        data = {
            'Name': ['Tom', 'Nick', 'Tom', 'John'],
            'Age': [20, 21, 20, 19],
            'Score': [85, 79, 88, 92]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(df.iloc[0]['Name'], 'John')
        self.assertAlmostEqual(avg_scores['Tom'], 86.5)
        self.assertEqual(common_age, 20)
    def test_empty_data(self):
        # Testing with empty lists
        data = {'Name': [], 'Age': [], 'Score': []}
        df, avg_scores, common_age = task_func(data)
        self.assertTrue(df.empty)
        self.assertTrue(avg_scores.empty)
        self.assertIsNone(common_age)
    def test_all_same_age(self):
        # Testing with all students having the same age
        data = {
            'Name': ['Alice', 'Bob', 'Cindy'],
            'Age': [25, 25, 25],
            'Score': [88, 92, 85]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(common_age, 25)
    def test_no_common_age(self):
        # Testing with no common age, each student has a unique age
        data = {
            'Name': ['Alice', 'Bob', 'Cindy'],
            'Age': [24, 25, 26],
            'Score': [88, 92, 85]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(common_age, 24)  # Assuming the first element is taken if all are equally common
    def test_duplicate_names_different_ages(self):
        # Testing with duplicate names but different ages
        data = {
            'Name': ['Tom', 'Tom', 'Nick'],
            'Age': [20, 21, 21],
            'Score': [85, 88, 79]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(len(df[df['Name'] == 'Tom']), 2)
        self.assertNotEqual(df.iloc[0]['Age'], df.iloc[1]['Age'])
        self.assertTrue(df[df['Name'] == 'Tom'].Age.isin([20, 21]).all())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)