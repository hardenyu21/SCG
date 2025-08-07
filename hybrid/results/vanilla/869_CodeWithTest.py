import pandas as pd
from itertools import cycle
from random import randint, seed

def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):
    # Check if the list of students is empty
    if not students:
        raise ValueError("The list of students is empty.")
    
    # Set the random seed for reproducibility if provided
    if rng_seed is not None:
        seed(rng_seed)
    
    # Cycle through the list of students
    student_cycle = cycle(students)
    
    # Generate grades and compile them into a list of dictionaries
    grades_data = []
    for _ in range(n_grades):
        student = next(student_cycle)
        grade = randint(min(grade_range), max(grade_range))
        grades_data.append({'Student': student, 'Grade': grade})
    
    # Create a pandas DataFrame from the list of dictionaries
    grade_report = pd.DataFrame(grades_data)
    
    return grade_report

# Example usage
grade_report = task_func(5, rng_seed=12)
print(grade_report)
import unittest
from unittest.mock import patch
import pandas as pd
class TestCases(unittest.TestCase):
    # Helper function to compare DataFrames
    def are_dataframes_equal(self, df1, df2):
        if df1.equals(df2):
            return True
        else:
            # Check if the two dataframes have the same columns and values
            return df1.shape == df2.shape and (df1.columns == df2.columns).all() and (df1.values == df2.values).all()
    def test_case_1(self):
        # Simple case with minimum input
        result = task_func(1, ['Alice'], range(1, 2), rng_seed=32)
        expected = pd.DataFrame({'Student': ['Alice'], 'Grade': [1]})
        self.assertTrue(self.are_dataframes_equal(result, expected))
    def test_case_2(self):
        # Testing with multiple grades and checking the cycling feature of students
        result = task_func(5, ['Alice', 'Bob'], range(1, 3), rng_seed=1233)
        # Since grades are random, we check for correct students and valid grades only
        expected_students = ['Alice', 'Bob', 'Alice', 'Bob', 'Alice']
        self.assertEqual(list(result['Student']), expected_students)
        self.assertTrue(all(grade in [1, 2] for grade in result['Grade']))
    def test_case_3(self):
        # Testing with different grade range
        result = task_func(200, ['Alice'], range(100, 102), rng_seed=12)
        # Check if the grades are within the specified range
        self.assertTrue(all(100 <= grade <= 101 for grade in result['Grade']))
    def test_case_4(self):
        # Testing with a larger number of grades
        number_of_grades = 1000
        result = task_func(number_of_grades, ['Alice', 'Bob'], range(1, 5), rng_seed=42)
        self.assertEqual(len(result), number_of_grades)
        self.assertTrue(all(1 <= grade <= 4 for grade in result['Grade']))
    def test_case_5(self):
        # Testing with an empty list of students, which should handle the error gracefully
        with self.assertRaises(Exception):
            task_func(3, [], range(1, 3))
    def test_default(self):
        result = task_func(10, rng_seed=12)
        expected = pd.DataFrame({
            'Student': {0: 'Alice',
            1: 'Bob',
            2: 'Charlie',
            3: 'David',
            4: 'Eve',
            5: 'Alice',
            6: 'Bob',
            7: 'Charlie',
            8: 'David',
            9: 'Eve'},
            'Grade': {0: 8, 1: 5, 2: 9, 3: 6, 4: 3, 5: 7, 6: 1, 7: 6, 8: 8, 9: 5}
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)