import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Step 1: Input Validation
    required_keys = {'Salary_String', 'Experience'}
    if not required_keys.issubset(data.keys()):
        raise ValueError("Input data must contain 'Salary_String' and 'Experience' keys.")
    
    # Step 2: DataFrame Conversion
    df = pd.DataFrame(data)
    
    # Step 3: Empty Data Handling
    if df.empty:
        fig, ax = plt.subplots()
        ax.set_xlabel('Experience')
        ax.set_ylabel('Normalized Salary')
        return ax
    
    # Step 4: Salary Conversion
    try:
        df['Salary'] = df['Salary_String'].str.replace(',', '').astype(float)
    except ValueError as e:
        raise ValueError("Failed to convert 'Salary_String' to float.") from e
    
    # Step 5: Salary Normalization
    scaler = MinMaxScaler()
    df['Normalized_Salary'] = scaler.fit_transform(df[['Salary']])
    
    # Step 6: Data Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Normalized_Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    
    return ax
import unittest
import pandas as pd
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_valid_data(self):
        """Test with valid data."""
        data = {"Salary_String": ["1,000", "2,000", "3,000"], "Experience": [1, 2, 3]}
        result = task_func(data)
        self.assertIsInstance(result, Axes)
    def test_missing_key(self):
        """Test with missing key in input dictionary."""
        data = {"Salary_String": ["1,000", "2,000", "3,000"]}
        with self.assertRaises(ValueError):
            task_func(data)
    def test_empty_data(self):
        """Test with empty data."""
        data = {"Salary_String": [], "Experience": []}
        result = task_func(data)
        self.assertIsInstance(result, Axes)
    def test_invalid_salary_format(self):
        """Test with invalid salary format."""
        data = {
            "Salary_String": ["1.000", "2,000", "Three Thousand"],
            "Experience": [1, 2, 3],
        }
        with self.assertRaises(ValueError):
            task_func(data)
    def test_mismatched_lengths(self):
        """Test with mismatched lengths of salary and experience arrays."""
        data = {"Salary_String": ["1,000", "2,000"], "Experience": [1, 2, 3]}
        with self.assertRaises(ValueError):
            task_func(data)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)