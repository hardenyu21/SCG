import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column_name="target_column"):
    # Convert JSON data to a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The specified column '{column_name}' does not exist in the DataFrame.")
    
    # Convert non-numeric columns to categorical and then to numeric codes
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        df[column_name] = pd.Categorical(df[column_name]).codes
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(df[column_name], bins=10, edgecolor='black')
    ax.set_title(f'Histogram of {column_name}')
    ax.set_xlabel(column_name)
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    return df, ax
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        # Sample data for testing
        self.sample_data = [
            {"userId": 1, "id": 1, "title": "A", "completed": False},
            {"userId": 1, "id": 2, "title": "B", "completed": True},
            {"userId": 2, "id": 3, "title": "A", "completed": False},
            {"userId": 2, "id": 4, "title": "B", "completed": True},
            {"userId": 3, "id": 5, "title": "A", "completed": False},
            {"userId": 3, "id": 6, "title": "B", "completed": True},
            {"userId": 3, "id": 7, "title": "B", "completed": True},
        ]
    def test_normal_case(self):
        """Test if the function returns correct DataFrame and histogram for a valid column."""
        df, ax = task_func(self.sample_data, "userId")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), len(self.sample_data))
        self.assertEqual(ax.get_title(), "Histogram of userId")
        self.assertEqual(ax.get_xlabel(), "userId")
    def test_non_existent_column(self):
        """Test if the function raises an error for a non-existent column."""
        with self.assertRaises(ValueError):
            task_func(self.sample_data, "non_existent_column")
    def test_empty_data(self):
        """Test the function with empty data."""
        with self.assertRaises(ValueError):
            task_func([], "userId")
    def test_non_numeric_data(self):
        """Test the function with a non-numeric column."""
        df, ax = task_func(self.sample_data, "title")
        self.assertTrue(pd.api.types.is_numeric_dtype(df["title"]))
        self.assertEqual(ax.get_title(), "Histogram of title")
        self.assertEqual(ax.get_xlabel(), "title")
    def test_duplicate_values(self):
        """Test the function with a column that has duplicate values."""
        df, ax = task_func(self.sample_data, "title")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(ax.get_title(), "Histogram of title")
        self.assertEqual(ax.get_xlabel(), "title")
    def tearDown(self):
        plt.clf()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)