import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # Compile the regular expression pattern for matching
    regex = re.compile(pattern)
    
    # List to store the Axes objects
    axes_list = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename matches the given pattern
        if regex.match(filename):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Ensure the DataFrame has the required columns
            if 'Month' in df.columns and 'Sales' in df.columns:
                # Create a new figure and axis for the plot
                fig, ax = plt.subplots()
                
                # Plot the sales data
                ax.plot(df['Month'], df['Sales'], marker='o')
                
                # Set the title and labels
                ax.set_title(f'Sales Data from {filename}')
                ax.set_xlabel('Month')
                ax.set_ylabel('Sales')
                
                # Rotate x-axis labels for better readability
                plt.xticks(rotation=45)
                
                # Add the axis to the list
                axes_list.append(ax)
    
    # Return the list of Axes objects
    return axes_list
import unittest
import shutil
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        # Prepare test data
        self.directory = "task_func_data/"
        self.pattern = r"^sales_data_\d{4}.csv"
        os.makedirs(self.directory, exist_ok=True)
        data_2021 = pd.DataFrame({
            'Month': ['January', 'February', 'March'],
            'Sales': [100, 150, 200]
        })
        data_2022 = pd.DataFrame({
            'Month': ['January', 'February', 'March'],
            'Sales': [120, 130, 210]
        })
        data_2021.to_csv(self.directory + "sales_data_2021.csv", index=False)
        data_2022.to_csv(self.directory + "sales_data_2022.csv", index=False)
    def tearDown(self):
        # Clean up test data
        shutil.rmtree(self.directory)
    def test_plots_generated(self):
        plots = task_func(self.directory, self.pattern)
        self.assertEqual(len(plots), 2, "Should generate two plots for two CSV files")
    def test_plot_titles(self):
        plots = task_func(self.directory, self.pattern)
        expected_titles = ['sales_data_2022.csv', 'sales_data_2021.csv']
        plot_titles = [plot.get_title() for plot in plots]
        self.assertEqual(set(plot_titles), set(expected_titles), "Plot titles should match the CSV filenames")
    def test_no_files_matched(self):
        plots = task_func(self.directory, r"^no_match_\d{4}.csv")
        self.assertEqual(len(plots), 0, "Should return an empty list if no files match the pattern")
    def test_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            task_func("/invalid/directory/", self.pattern)
    def test_plot_data_integrity(self):
        plots = task_func(self.directory, self.pattern)
        # Read the CSV files again to get expected data
        expected_data = []
        for file in os.listdir(self.directory):
            if re.match(self.pattern, file):
                df = pd.read_csv(os.path.join(self.directory, file))
                expected_data.append(df['Sales'].to_list())
        for plot, expected_sales in zip(plots, expected_data):
            lines = plot.get_lines()
            for line in lines:
                y_data = line.get_ydata()
                # Use np.isclose for floating point comparison, if necessary
                self.assertTrue(any(np.array_equal(y_data, expected) for expected in expected_data), "Plotted data should match the CSV file content")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)