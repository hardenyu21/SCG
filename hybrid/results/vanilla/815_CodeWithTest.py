import pandas as pd
import numpy as np

def task_func(test_scores, student):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(test_scores)
    
    # Check if the student is present in the DataFrame
    if student not in df['Student'].values:
        raise ValueError("student is not present in the test_scores dataframe")
    
    # Filter the DataFrame for the specific student
    student_scores = df[df['Student'] == student]['Score']
    
    # Calculate the average score and standard deviation
    average_score = student_scores.mean()
    std_deviation = student_scores.std()
    
    # Return the results as a numpy array and the DataFrame
    return np.array([average_score, std_deviation]), df

# Example usage:
# scores = {'Student': [1, 2, 1, 1], 'Score': [10, 1, 1, 1]}
# result, df = task_func(scores, 1)
# print(result)
# print(df)
import unittest
from faker import Faker
import numpy as np
import pandas as pd
fake = Faker()
class TestCases(unittest.TestCase):
    def setUp(self):
        self.student_ids = range(1, 6)
        self.students_sample = list(np.random.choice(self.student_ids, 50, replace=True))
        self.scores = {
            'Student': self.students_sample, 
            'Score': list(np.random.randint(50, 101, size=50))
        }
    def test_case_1(self):
        student_id = self.students_sample[0]
        scores_df = pd.DataFrame(self.scores)
        expected_avg = scores_df[scores_df['Student'] == student_id]['Score'].mean()
        expected_std = scores_df[scores_df['Student'] == student_id]['Score'].std()
        res, df = task_func(self.scores, student_id)
        avg, std = res
        self.assertIsInstance(res, np.ndarray)
        self.assertAlmostEqual(expected_avg, avg, places=2)
        self.assertAlmostEqual(expected_std, std, places=2)
        pd.testing.assert_frame_equal(pd.DataFrame(self.scores), df)
    def test_case_2(self):
        student_id = max(self.student_ids) + 1
        with self.assertRaises(ValueError):
            task_func(self.scores, student_id)
    def test_case_3(self):
        empty_df = dict.fromkeys(['Student', 'Score'])
        student_id = fake.random_int(min=1, max=100)
        with self.assertRaises(ValueError):
            task_func(empty_df, student_id)
    def test_case_4(self):
        scores = {
            'Student': list(self.student_ids), 
            'Score': [100] * len(self.student_ids)
        }
        student_id = self.student_ids[3]
        res, df = task_func(scores, student_id)
        avg, std = res
        self.assertIsInstance(res, np.ndarray)
        self.assertEqual(avg, 100.0)
        self.assertTrue(np.isnan(std))
        pd.testing.assert_frame_equal(pd.DataFrame(scores), df)
    def test_case_5(self):
        scores = {
            'Student': list(self.student_ids) * 10, 
            'Score': list(np.random.randint(50, 101, size=len(self.student_ids)*10))
        }
        student_id = self.student_ids[4]
        scores_df = pd.DataFrame(scores)
        expected_avg = scores_df[scores_df['Student'] == student_id]['Score'].mean()
        expected_std = scores_df[scores_df['Student'] == student_id]['Score'].std()
        res, df = task_func(scores, student_id)
        avg, std = res
        self.assertAlmostEqual(expected_avg, avg, places=2)
        self.assertAlmostEqual(expected_std, std, places=2)
        pd.testing.assert_frame_equal(pd.DataFrame(scores), df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)