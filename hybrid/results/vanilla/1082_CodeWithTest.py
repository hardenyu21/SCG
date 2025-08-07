import pandas as pd
from scipy.stats import pearsonr
import numpy as np

def task_func(data):
    # Check if the data frame has less than 2 rows
    if len(data) < 2:
        return np.nan
    
    # Convert scores from string format to floats
    data['scores'] = data['scores'].astype(float)
    
    # Encode categorical grades into numerical values based on their rank order
    grade_mapping = {grade: rank for rank, grade in enumerate(data['grades'].unique())}
    data['encoded_grades'] = data['grades'].map(grade_mapping)
    
    # Compute the Pearson correlation coefficient
    correlation, _ = pearsonr(data['scores'], data['encoded_grades'])
    
    return correlation
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_normal_operation(self):
        """
        Test normal operation with valid input.
        """
        data = {"Score_String": ["80.5", "85.7", "90.2"], "Grade": ["B", "B+", "A-"]}
        result = task_func(data)
        self.assertIsInstance(result, float)
    def test_empty_input(self):
        """
        Test the function with empty input.
        """
        data = {"Score_String": [], "Grade": []}
        result = task_func(data)
        self.assertTrue(pd.isna(result))
    def test_invalid_score_format(self):
        """
        Test the function with invalid score format.
        """
        data = {"Score_String": ["eighty", "85.7", "90.2"], "Grade": ["B", "B+", "A-"]}
        with self.assertRaises(ValueError):
            task_func(data)
    def test_mismatched_lengths(self):
        """
        Test the function with mismatched lengths of scores and grades.
        """
        data = {"Score_String": ["80.5", "85.7"], "Grade": ["B", "B+", "A-"]}
        with self.assertRaises(ValueError):
            task_func(data)
    def test_non_ordinal_grades(self):
        """
        Test the function with non-ordinal grade inputs.
        """
        data = {
            "Score_String": ["80.5", "85.7", "90.2"],
            "Grade": ["Pass", "Fail", "Pass"],
        }
        result = task_func(data)
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)