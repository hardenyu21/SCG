import pandas as pd
import numpy as np
from random import randint

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    # Initialize a dictionary to store student data
    student_data = {student: [] for student in STUDENTS}
    
    # Generate random grades for each student in each course
    for student in STUDENTS:
        for course in COURSES:
            grade = randint(0, 100)  # Random grade between 0 and 100
            student_data[student].append(grade)
    
    # Calculate average grade for each student
    for student in STUDENTS:
        average_grade = np.mean(student_data[student])
        student_data[student].append(average_grade)
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(student_data, index=COURSES + ['Average'])
    
    # Transpose the DataFrame to have students as rows
    df = df.T
    
    # Rename the last column to 'Average'
    df.columns = COURSES + ['Average']
    
    return df

# Example usage
df = task_func()
print(df)
import unittest
from unittest.mock import patch
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        # Correctly set up the mock within the test execution context
        self.patcher = patch('random.randint', side_effect=[i % 100 for i in range(800)])  # Assuming 8 students and 100 course entries
        self.mock_randint = self.patcher.start()
        self.grades_df = task_func()
        self.patcher.stop()
    def test_dataframe_columns(self):
        # Ensure the DataFrame contains the correct columns
        expected_columns = ['Name'] + COURSES + ['Average Grade']
        self.assertListEqual(list(self.grades_df.columns), expected_columns, "DataFrame should have specific columns")
    def test_grade_range(self):
        # Check that all grades are within the valid range (0 to 100)
        course_columns = self.grades_df.columns[1:-1]  # Exclude 'Name' and 'Average Grade'
        for course in course_columns:
            self.assertTrue(self.grades_df[course].between(0, 100).all(),
                            f"All grades in {course} should be between 0 and 100")
    def test_average_grade_calculation(self):
        # Verify that the average grade is correctly calculated
        course_columns = self.grades_df.columns[1:-1]  # Exclude 'Name' and 'Average Grade'
        calculated_avg = self.grades_df[course_columns].mean(axis=1)
        np.testing.assert_array_almost_equal(self.grades_df['Average Grade'], calculated_avg, decimal=1,
                                             err_msg="Average grades should be correctly calculated")
    def test_all_students_included(self):
        # Ensure that all predefined students are included in the DataFrame
        self.assertTrue(set(STUDENTS).issubset(set(self.grades_df['Name'])),
                        "All predefined students should be included in the DataFrame")
    def test_deterministic_grades(self):
        # Verify the grades are deterministic under mocked conditions
        random.seed(0)
        expected_first_row_grades = [randint(0, 100) for _ in COURSES]
        actual_first_row_grades = self.grades_df.iloc[0, 1:-1].tolist()
        self.assertListEqual(actual_first_row_grades, expected_first_row_grades,
                             "The first row grades should be deterministic and match the expected pattern")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)