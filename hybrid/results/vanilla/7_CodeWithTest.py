import csv
import collections

def task_func(csv_file_path):
    # Initialize a dictionary to keep track of total sales per product
    sales_data = collections.defaultdict(int)
    
    # Open the CSV file and read the data
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV file
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            
            # Update the total sales for the product
            sales_data[product] += quantity
    
    # Find the product with the highest total sales
    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]
    
    return top_selling_product
import os
import unittest
import csv
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a directory for test files if it does not exist
        self.test_dir = os.path.join(os.getcwd(), 'test_data')
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self):
        # Remove all files created in the test directory
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    def test_case_1(self):
        # Correct data, expected top-seller is determined correctly
        self.create_csv('sales1.csv', [['product', 'quantity'], ['Product B', '200'], ['Product A', '100']])
        result = task_func(os.path.join(self.test_dir, "sales1.csv"))
        self.assertEqual(result, "Product B")
    def test_case_2(self):
        # Correct data, expected top-seller is determined correctly
        self.create_csv('sales2.csv', [['product', 'quantity'], ['Product Z', '120'], ['Product Y', '80']])
        result = task_func(os.path.join(self.test_dir, "sales2.csv"))
        self.assertEqual(result, "Product Z")
    def test_case_3(self):
        # Correct data, expected top-seller is determined correctly
        self.create_csv('sales3.csv', [['product', 'quantity'], ['Product M', '500'], ['Product N', '400']])
        result = task_func(os.path.join(self.test_dir, "sales3.csv"))
        self.assertEqual(result, "Product M")
    def test_case_4(self):
        # Empty file with header, expect a ValueError or a graceful handle
        self.create_csv('sales4.csv', [['product', 'quantity']])
        with self.assertRaises(ValueError):
            task_func(os.path.join(self.test_dir, "sales4.csv"))
    def test_case_5(self):
        # Single product data, correct determination
        self.create_csv('sales5.csv', [['product', 'quantity'], ['Single Product', '999']])
        result = task_func(os.path.join(self.test_dir, "sales5.csv"))
        self.assertEqual(result, "Single Product")
    def test_case_6(self):
        # File does not exist, expect FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func(os.path.join(self.test_dir, "nonexistent.csv"))
    def test_case_7(self):
        # Incorrect data types, expect ValueError or graceful handling of conversion failure
        self.create_csv('sales6.csv', [['product', 'quantity'], ['Product A', 'one hundred']])
        with self.assertRaises(ValueError):
            task_func(os.path.join(self.test_dir, "sales6.csv"))
    def create_csv(self, filename, rows):
        # Helper function to create CSV files with given rows
        path = os.path.join(self.test_dir, filename)
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)