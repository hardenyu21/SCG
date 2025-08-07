import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The CSV file at '{file_path}' does not exist.")
    
    # Read the CSV file
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")
    
    # Clean the data: select numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    
    # Flatten the data to a single series if it has multiple columns
    if not numeric_data.empty:
        numeric_data = numeric_data.stack()
    
    # Calculate mean and median
    mean_value = numeric_data.mean() if not numeric_data.empty else np.nan
    median_value = numeric_data.median() if not numeric_data.empty else np.nan
    
    # Generate a plot
    plt.figure(figsize=(10, 6))
    plt.plot(numeric_data.index, numeric_data.values, marker='o', linestyle='-')
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    
    # Save the plot
    plt.savefig(plot_path)
    plt.close()
    
    return mean_value, median_value, plot_path
import unittest
import os
import numpy as np
import pandas as pd
import shutil
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        # Create a directory for test files if it doesn't exist
        self.test_dir = "mnt/data/task_func_data_test"
        os.makedirs(self.test_dir, exist_ok=True)
        # Create a valid data file
        self.valid_data_path = os.path.join(self.test_dir, "valid_data.csv")
        pd.DataFrame({"data": np.random.rand(100)}).to_csv(
            self.valid_data_path, index=False
        )
        # Create an empty data file
        self.empty_data_path = os.path.join(self.test_dir, "empty_data.csv")
        with open(self.empty_data_path, "w") as f:
            f.write("")
        # Create a non-numeric data file
        self.non_numeric_data_path = os.path.join(self.test_dir, "non_numeric_data.csv")
        pd.DataFrame({"data": ["a", "b", "c", "d"]}).to_csv(
            self.non_numeric_data_path, index=False
        )
        # Create a large data file
        self.large_data_path = os.path.join(self.test_dir, "large_data.csv")
        pd.DataFrame({"data": np.random.rand(10000)}).to_csv(
            self.large_data_path, index=False
        )
        # Create a data file with NaN values
        self.nan_data_path = os.path.join(self.test_dir, "nan_data.csv")
        pd.DataFrame({"data": [1, np.nan, 2, np.nan, 3]}).to_csv(
            self.nan_data_path, index=False
        )
        # Create a data file with a single value
        self.single_value_path = os.path.join(self.test_dir, "single_value.csv")
        pd.DataFrame({"data": [42]}).to_csv(self.single_value_path, index=False)
        # Create a data file where all values are NaN
        self.all_nan_path = os.path.join(self.test_dir, "all_nan.csv")
        pd.DataFrame({"data": [np.nan, np.nan, np.nan]}).to_csv(
            self.all_nan_path, index=False
        )
    def test_valid_input(self):
        """Test that the function runs without errors and returns the correct output."""
        plot_path = os.path.join(self.test_dir, "valid_plot.png")
        mean, median, plot_path = task_func(self.valid_data_path, plot_path)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertTrue(os.path.exists(plot_path))
    def test_file_not_found(self):
        """Test that the function raises a FileNotFoundError when the specified file does not exist."""
        plot_path = os.path.join(self.test_dir, "not_found_plot.png")
        with self.assertRaises(FileNotFoundError):
            task_func(os.path.join(self.test_dir, "non_existent_file.csv"), plot_path)
    def test_empty_file(self):
        """Test that the function returns NaN for mean and median when the file is empty."""
        plot_path = os.path.join(self.test_dir, "empty_plot.png")
        mean, median, returned_plot_path = task_func(self.empty_data_path, plot_path)
        self.assertTrue(np.isnan(mean))
        self.assertTrue(np.isnan(median))
        self.assertFalse(
            os.path.exists(returned_plot_path)
        )  # Plot should not exist for empty file
    def test_non_numeric_data(self):
        """Test that the function returns NaN for mean and median when the file contains non-numeric data."""
        plot_path = os.path.join(self.test_dir, "non_numeric_plot.png")
        mean, median, returned_plot_path = task_func(self.non_numeric_data_path, plot_path)
        self.assertTrue(np.isnan(mean))
        self.assertTrue(np.isnan(median))
        self.assertTrue(os.path.exists(returned_plot_path))
    def test_large_data(self):
        """Test that the function runs without errors and returns the correct output for a large data file."""
        plot_path = os.path.join(self.test_dir, "large_data_plot.png")
        mean, median, returned_plot_path = task_func(self.large_data_path, plot_path)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertTrue(os.path.exists(returned_plot_path))
    def test_data_with_nan_values(self):
        """Test that the function returns the correct output for a data file with NaN values."""
        plot_path = os.path.join(self.test_dir, "nan_data_plot.png")
        mean, median, returned_plot_path = task_func(self.nan_data_path, plot_path)
        self.assertNotEqual(mean, np.nan)
        self.assertNotEqual(median, np.nan)
        self.assertTrue(os.path.exists(returned_plot_path))
    def test_single_value_data(self):
        """Test that the function returns the correct output for a data file with a single value."""
        plot_path = os.path.join(self.test_dir, "single_value_plot.png")
        mean, median, returned_plot_path = task_func(self.single_value_path, plot_path)
        self.assertEqual(mean, 42)
        self.assertEqual(median, 42)
        self.assertTrue(os.path.exists(returned_plot_path))
    def test_all_nan_data(self):
        """Test that the function returns NaN for mean and median when the file contains all NaN values."""
        plot_path = os.path.join(self.test_dir, "all_nan_plot.png")
        mean, median, returned_plot_path = task_func(self.all_nan_path, plot_path)
        self.assertTrue(np.isnan(mean))
        self.assertTrue(np.isnan(median))
        self.assertTrue(os.path.exists(returned_plot_path))
    def tearDown(self):
        # Remove all created files
        plt.clf()
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
        # Remove the test directory
        dirs_to_remove = ["mnt/data", "mnt"]
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)