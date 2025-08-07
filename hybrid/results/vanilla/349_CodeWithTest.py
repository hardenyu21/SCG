import pandas as pd
import random

def task_func(product_list, categories):
    # Ensure the number of products matches the number of categories
    if len(product_list) != len(categories):
        raise ValueError("The number of products must match the number of categories.")
    
    # Initialize lists to store sales data
    quantity_sold = []
    revenue = []
    
    # Generate random sales data for each product
    for _ in product_list:
        q_sold = random.randint(1, 100)
        price_per_unit = random.randint(10, 100)
        r_generated = q_sold * price_per_unit
        
        quantity_sold.append(q_sold)
        revenue.append(r_generated)
    
    # Create a DataFrame with the sales data
    sales_data = {
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': quantity_sold,
        'Revenue': revenue
    }
    
    df = pd.DataFrame(sales_data)
    
    return df

# Example usage:
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']
sales_report = task_func(product_list, categories)
print(sales_report)
import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    
    categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
    products = ['Product ' + str(i) for i in range(1, 101)]
    
    def test_case_1(self):
        random.seed(0)
        report = task_func(self.products[:5], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 5)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_2(self):
        random.seed(0)
        report = task_func(self.products[5:10], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 5)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_3(self):
        random.seed(0)
        report = task_func([self.products[10]], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 1)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_4(self):
        random.seed(0)
        report = task_func(self.products[10:20], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 10)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_5(self):
        random.seed(0)
        report = task_func(self.products[20:40], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 20)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)