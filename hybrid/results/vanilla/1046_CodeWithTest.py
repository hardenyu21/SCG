from datetime import datetime, timedelta
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Parse the input date string to a datetime object
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Generate a list of the next 10 days starting from the input date
    date_list = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a Cartesian product of employees and dates
    employee_date_pairs = list(product(EMPLOYEES, date_list))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(employee_date_pairs, columns=['Employee', 'Date'])
    
    return df

# Example usage
if __name__ == "__main__":
    date_str = "2023-10-01"
    df = task_func(date_str)
    print(df)
import unittest
import pandas as pd
from datetime import datetime, timedelta
class TestCases(unittest.TestCase):
    """Test cases for the function."""
    def test_return_type(self):
        """Test if the function returns a Pandas DataFrame."""
        df_test = task_func("2023-01-01")
        self.assertIsInstance(df_test, pd.DataFrame)
    def test_correct_columns(self):
        """Test if the DataFrame has the correct columns: 'Employee' and 'Date'."""
        df_test = task_func("2023-01-01")
        self.assertListEqual(df_test.columns.tolist(), ["Employee", "Date"])
    def test_date_range(self):
        """Test if the function generates the correct date range for 10 days."""
        start_date = "2023-01-01"
        df_test = task_func(start_date)
        end_date = (
            datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=9)
        ).date()
        self.assertTrue(all(df_test["Date"] <= pd.Timestamp(end_date)))
    def test_number_of_rows(self):
        """Test if the DataFrame has the correct number of rows (10 days * number of employees)."""
        df_test = task_func("2023-01-01")
        expected_rows = 10 * len(EMPLOYEES)  # 10 days for each employee
        self.assertEqual(len(df_test), expected_rows)
    def test_leap_year(self):
        """Test if the function correctly handles the date range for a leap year."""
        df_test = task_func("2024-02-28")
        leap_year_end_date = (
            datetime.strptime("2024-02-28", "%Y-%m-%d") + timedelta(days=9)
        ).date()
        self.assertIn(pd.Timestamp(leap_year_end_date), df_test["Date"].values)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)