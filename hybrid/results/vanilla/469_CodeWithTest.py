import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Normalize grades to be case-insensitive
    normalized_grades = [grade.strip().upper() for grade in student_grades]
    
    # Filter out grades that are not in the possible grades list
    valid_grades = [grade for grade in normalized_grades if grade in possible_grades]
    
    # Count the occurrences of each grade
    grade_counts = Counter(valid_grades)
    
    # Create a DataFrame with the grade counts
    grade_df = pd.DataFrame(list(grade_counts.items()), columns=['Grade', 'Count'])
    grade_df.set_index('Grade', inplace=True)
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    grade_df.plot(kind='bar', y='Count', ax=ax, legend=False)
    ax.set_title('Grade Distribution')
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    plt.xticks(rotation=0)
    
    # Return the DataFrame and the Axes object
    return grade_df, ax

# Example usage:
# student_grades = ["A", "b", "C", "d", "F", "A", "B", "c", "d", "E", "F", "A", "B", "C", "D", "F"]
# df, ax = task_func(student_grades)
# plt.show()
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def _validate_plot(self, ax):
        self.assertEqual(ax.get_title(), "Grade Distribution")
        self.assertEqual(ax.get_xlabel(), "Grade")
        self.assertEqual(ax.get_ylabel(), "Number of Students")
    def _test_helper(self, grades, expected_counts):
        expected_df = pd.DataFrame(
            {"Count": expected_counts}, index=["A", "B", "C", "D", "F"]
        )
        expected_df.index.name = "Grade"
        report_df, ax = task_func(grades)
        pd.testing.assert_frame_equal(report_df, expected_df)
        self._validate_plot(ax)
    def test_case_1(self):
        # Test with a mix of grades
        self._test_helper(
            ["A", "B", "B", "C", "A", "D", "F", "B", "A", "C"], [3, 3, 2, 1, 1]
        )
    def test_case_2(self):
        # Test with only one type of grade
        self._test_helper(["A", "A", "A", "A", "A"], [5, 0, 0, 0, 0])
    def test_case_3(self):
        # Test with an empty list of grades
        with self.assertRaises(Exception):
            task_func([], [0, 0, 0, 0, 0])
    def test_case_4(self):
        # Test correctly ignoring invalid grades
        self._test_helper(["A", "X", "Y", "Z"], [1, 0, 0, 0, 0])
    def test_case_5(self):
        # Test custom grades
        grades = ["A", "C", "G", "G"]
        expected_counts = [1, 0, 1, 0, 0, 2]
        possible_grades = ["A", "B", "C", "D", "F", "G"]
        expected_df = pd.DataFrame(
            {"Count": expected_counts},
            index=[*dict.fromkeys(g.upper() for g in possible_grades)],
        )
        expected_df.index.name = "Grade"
        report_df, ax = task_func(grades, possible_grades=possible_grades)
        pd.testing.assert_frame_equal(report_df, expected_df)
        self._validate_plot(ax)
    def test_case_6(self):
        # Test case insensitivity
        self._test_helper(["a", "b", "C"], [1, 1, 1, 0, 0])
    def test_case_7(self):
        # Test whitespace sensitivity
        self._test_helper(["A ", "b", " C"], [0, 1, 0, 0, 0])
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)