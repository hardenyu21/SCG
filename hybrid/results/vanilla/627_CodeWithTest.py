from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    # Initialize a list to store the sales data for each product
    sales_data = []

    # Iterate over each product in the list
    for product in products_list:
        # Generate random sales data for 12 months
        monthly_sales = [randint(100, 1000) for _ in range(12)]
        
        # Calculate the average sales for the product
        average_sales = mean(monthly_sales)
        
        # Append the product name, monthly sales, and average sales to the sales_data list
        sales_data.append([product] + monthly_sales + [average_sales])

    # Define the column names for the DataFrame
    columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    
    # Create a pandas DataFrame from the sales data
    df = pd.DataFrame(sales_data, columns=columns)
    
    return df

# Example usage:
# products = ['Product A', 'Product B', 'Product C']
# df = task_func(products)
# print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a single product
        products = ["Apples"]
        sales_data = task_func(products)
        
        # Checking if returned DataFrame has the correct structure
        expected_columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
        self.assertEqual(list(sales_data.columns), expected_columns)
        
        # Checking the correctness of average sales
        avg_sales = sales_data['Average Sales'].iloc[0]
        self.assertAlmostEqual(avg_sales, sales_data.iloc[0, 1:13].mean(), places=2)
        
        # Checking if sales values are within the expected range
        self.assertTrue((sales_data.iloc[0, 1:13] >= 100).all() and (sales_data.iloc[0, 1:13] <= 500).all())
    def test_case_2(self):
        # Test with multiple products
        products = ["Apples", "Bananas", "Grapes"]
        sales_data = task_func(products)
        self.assertEqual(len(sales_data), 3)
    def test_case_3(self):
        # Test with no products
        products = []
        sales_data = task_func(products)
        self.assertEqual(len(sales_data), 0)
    def test_case_4(self):
        # Test with a long product name
        products = ["A" * 100]
        sales_data = task_func(products)
        self.assertEqual(sales_data['Product'].iloc[0], "A" * 100)
    def test_case_5(self):
        # Test with products having special characters
        products = ["@pples", "!Bananas", "#Grapes"]
        sales_data = task_func(products)
        self.assertTrue(all(item in sales_data['Product'].tolist() for item in products))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)