import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    # Initialize lists to store product data
    products = []
    quantities = []
    prices = []
    profits = []

    # Iterate over the specified product keys
    for key in product_keys:
        if key in product_dict:
            product = product_dict[key]
            products.append(key)
            quantities.append(product.get('quantity', 0))
            prices.append(product.get('price', 0))
            profits.append(product.get('profit', 0))

    # Create a DataFrame from the collected data
    df = pd.DataFrame({
        'Product': products,
        'Quantity': quantities,
        'Price': prices,
        'Profit': profits
    })

    # Calculate average price and profit
    if not df.empty:
        average_price = df['Price'].mean()
        average_profit = df['Profit'].mean()
        df['Average Price'] = average_price
        df['Average Profit'] = average_profit
    else:
        df['Average Price'] = np.nan
        df['Average Profit'] = np.nan

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    if not df.empty:
        df.plot(kind='bar', x='Product', y='Profit', ax=ax, legend=False)
        ax.set_ylabel('Profit')
        ax.set_title('Profit for Each Product')
    else:
        ax = None

    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
product_dict = {
    'ProductA': {'quantity': 10, 'price': 20, 'profit': 5},
    'ProductB': {'quantity': 15, 'price': 25, 'profit': 7},
    'ProductC': {'quantity': 20, 'price': 30, 'profit': 10}
}

product_keys = ['ProductA', 'ProductB', 'ProductC']
df, ax = task_func(product_dict, product_keys)
print(df)
plt.show()
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup common to all tests: A product dictionary
        self.product_dict = {
            'Apple': [100, 2.5],
            'Orange': [80, 3.5],
            'Banana': [120, 1.5]
        }
    def test_case_1(self):
        # Test with a single product
        product_keys = ['Apple']
        report, ax = task_func(self.product_dict, product_keys)
        self.assertEqual(len(report), 1)  # Should return 1 row
        self.assertIn('Apple', report['Product'].values)
        self.assertAlmostEqual(report['Average Price'].iloc[0], 2.5)
        self.assertAlmostEqual(report['Average Profit'].iloc[0], 250.0)
    def test_case_2(self):
        # Test with multiple products
        product_keys = ['Apple', 'Orange']
        report, ax = task_func(self.product_dict, product_keys)
        self.assertEqual(len(report), 2)  # Should return 2 rows
        self.assertTrue(all(item in ['Apple', 'Orange'] for item in report['Product'].values))
        expected_avg_price = (2.5 + 3.5) / 2
        expected_avg_profit = (250.0 + 280.0) / 2
        self.assertTrue(all(report['Average Price'] == expected_avg_price))
        self.assertTrue(all(report['Average Profit'] == expected_avg_profit))
    def test_case_3(self):
        # Test with no products
        product_keys = []
        report, ax = task_func(self.product_dict, product_keys)
        self.assertTrue(report.empty)  # Should return an empty DataFrame
    def test_case_4(self):
        # Test with a product that doesn't exist in the dictionary
        product_keys = ['Mango']  # Mango is not in product_dict
        with self.assertRaises(KeyError):
            task_func(self.product_dict, product_keys)
    def test_case_5(self):
        # Test the DataFrame structure
        product_keys = ['Apple', 'Banana']
        report, ax = task_func(self.product_dict, product_keys)
        expected_columns = ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
        self.assertEqual(list(report.columns), expected_columns)
        for col in ['Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']:
            self.assertTrue(pd.api.types.is_numeric_dtype(report[col]), f"{col} should be numeric type")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)