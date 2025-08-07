import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Ensure the number of products matches the number of categories
    if len(product_list) != len(categories):
        raise ValueError("The number of products must match the number of categories.")
    
    # Generate random data for quantity sold and revenue
    data = {
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': [random.randint(min_value, max_value) for _ in product_list],
        'Revenue': [random.uniform(10.0, 100.0) for _ in product_list]
    }
    
    # Calculate total revenue for each product
    data['Total Revenue'] = [q * r for q, r in zip(data['Quantity Sold'], data['Revenue'])]
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
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
    
    def test_case_6(self):
        random.seed(0)
        report = task_func([self.products[0]], self.categories, 10, 10)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 1)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        self.assertEqual(report.iloc[0]['Quantity Sold'], 10)
        self.assertEqual(report.iloc[0]['Total Revenue'], 100)
    
    def test_case_7(self):
        random.seed(0)
        report = task_func([self.products[0]], self.categories, 10, 100)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 1)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        self.assertEqual(report.iloc[0]['Total Revenue'], report.iloc[0]['Quantity Sold']*report.iloc[0]['Revenue'])
    def test_case_8(self):
        random.seed(0)
        report = task_func(self.products[40:60], self.categories, 100, 200)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 20)
        for index, row in report.iterrows():
            self.assertEqual(row['Total Revenue'], row['Quantity Sold']*row['Revenue'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)