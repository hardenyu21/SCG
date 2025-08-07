import os
import time
import pandas as pd

OUTPUT_DIR = './output'

def task_func(datasets, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the full path for the output file
    file_path = os.path.join(output_dir, filename)
    
    # Open the file in write mode
    with open(file_path, 'w') as file:
        for i, df in enumerate(datasets):
            # Write the DataFrame to the file
            df.to_csv(file, index=False)
            
            # Add a separator line if it's not the last DataFrame
            if i < len(datasets) - 1:
                file.write('------\n')

# Example usage:
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
# task_func([df1, df2], 'output.csv')
import unittest
import shutil
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        """Ensure the data directory exists before any tests are run."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up by removing the data directory and its contents after all tests."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    def test_single_dataframe(self):
        """Test with a single DataFrame."""
        df = pd.DataFrame({"Column1": [1, 2], "Column2": [3, 4]})
        task_func([df], 'single_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'single_dataframe.csv')))
    def test_multiple_dataframes(self):
        """Test with multiple DataFrames."""
        df1 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
        df2 = pd.DataFrame({"C": [9, 10], "D": [11, 12]})
        task_func([df1, df2], 'multiple_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'multiple_dataframes.csv')))
    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        task_func([df], 'empty_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'empty_dataframe.csv')))
    def test_varying_row_counts(self):
        """Test with DataFrames having varying numbers of rows."""
        df1 = pd.DataFrame({"E": [13], "F": [14]})
        df2 = pd.DataFrame({"G": [15, 16, 17], "H": [18, 19, 20]})
        task_func([df1, df2], 'varying_row_counts.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'varying_row_counts.csv')))
    def test_no_dataframes(self):
        """Test with no DataFrames provided."""
        task_func([], 'no_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'no_dataframes.csv')))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)