import pandas as pd
import numpy as np
import random
from random import randint, seed

# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Generate product names with spaces replaced by underscores
    product_names = [name.replace(' ', '_') for name in mystrings]
    
    # Ensure we have enough product names or truncate if necessary
    if len(product_names) > n_products:
        product_names = product_names[:n_products]
    else:
        # If not enough product names, repeat them
        product_names = (product_names * (n_products // len(product_names) + 1))[:n_products]
    
    # Randomly assign categories to each product
    categories = [random.choice(CATEGORIES) for _ in range(n_products)]
    
    # Generate prices based on a normal distribution
    prices = np.random.normal(loc=50, scale=10, size=n_products).round(2)
    
    # Create a DataFrame
    product_catalog = pd.DataFrame({
        'Product Name': product_names,
        'Category': categories,
        'Price': prices
    })
    
    return product_catalog

# Example usage:
# mystrings = ['Laptop', 'T-shirt', 'Blender', 'Novel', 'Toy Car']
# n_products = 10
# print(task_func(mystrings, n_products))
import unittest
from pandas.testing import assert_frame_equal
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        
        result = task_func(['Mobile Phone', 'T Shirt', 'Coffee Maker', 'Python Book', 'Toy Car'], 2, 42)
        # assert the value of the DataFrame
        self.assertEqual(result['Product Name'].tolist(), ['Mobile_Phone', 'Coffee_Maker'])
        self.assertEqual(result['Category'].tolist(), ['Electronics', 'Clothing'])
        self.assertEqual(result['Price'].tolist(), [54.97, 48.62])
        
    def test_case_2(self):
        result = task_func(['Laptop', 'Sweater'], 1)
        self.assertEqual(result['Product Name'].tolist(), ['Sweater'])
        self.assertEqual(result['Category'].tolist(), ['Books'])
        self.assertEqual(result['Price'].tolist(), [67.64])
        
    def test_case_3(self):
        result = task_func(['Book', 'Pen', 'Bag'], 3)
        self.assertEqual(result['Product Name'].tolist(), ['Pen', 'Book', 'Bag'])
        self.assertEqual(result['Category'].tolist(), ['Books', 'Home & Kitchen', 'Books'])
        self.assertEqual(result['Price'].tolist(), [67.64, 54.00, 59.79])
        
    def test_case_4(self):
        result = task_func(['Watch'], 2)
        self.assertEqual(result['Product Name'].tolist(), ['Watch', 'Watch'])
        self.assertEqual(result['Category'].tolist(), ['Books', 'Home & Kitchen'])
        self.assertEqual(result['Price'].tolist(), [67.64, 54.00])
    def test_case_5(self):
        result = task_func(['TV', 'Fridge', 'Sofa', 'Table'], 0)
        self.assertEqual(result.empty, True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)