import pandas as pd
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from the Excel file
        logging.info(f"Reading data from Excel file: {excel_file_location}")
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        
        # Convert the DataFrame to a CSV file
        logging.info(f"Converting data to CSV file: {csv_file_location}")
        df.to_csv(csv_file_location, index=False)
        
        # Calculate the sum of each column
        logging.info("Calculating the sum of each column")
        column_sums = df.sum().to_dict()
        
        return column_sums
    
    except FileNotFoundError:
        logging.error(f"FileNotFoundError: The Excel file does not exist at the specified path: {excel_file_location}")
        raise
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise

# Example usage:
# result = task_func("Sheet1")
# print(result)
import unittest
import pandas as pd
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a dummy Excel file for testing
        self.test_excel_file = 'dummy_test.xlsx'
        self.test_csv_file = 'dummy_test.csv'
        self.test_sheet_name = 'TestSheet'
        data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
        df = pd.DataFrame(data)
        df.to_excel(self.test_excel_file, sheet_name=self.test_sheet_name, index=False)
    def tearDown(self):
        os.remove(self.test_excel_file)
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)
    def test_normal_functionality(self):
        result = task_func(self.test_sheet_name, self.test_excel_file, self.test_csv_file)
        self.assertEqual(result, {'A': 60, 'B': 150})
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_sheet_name, 'nonexistent.xlsx', self.test_csv_file)
    def test_sheet_not_found(self):
        with self.assertRaises(ValueError):
            task_func('NonexistentSheet', self.test_excel_file, self.test_csv_file)
    def test_empty_excel_file(self):
        empty_excel_file = 'empty_test.xlsx'
        pd.DataFrame().to_excel(empty_excel_file, index=False)
        with self.assertRaises(ValueError):
            task_func(self.test_sheet_name, empty_excel_file, self.test_csv_file)
        os.remove(empty_excel_file)
    def test_overwrite_existing_csv(self):
        with open(self.test_csv_file, 'w') as file:
            file.write('Old Data')
        task_func(self.test_sheet_name, self.test_excel_file, self.test_csv_file)
        with open(self.test_csv_file, 'r') as file:
            self.assertNotIn('Old Data', file.read())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)