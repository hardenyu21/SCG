import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

def task_func():
    # Generate a DataFrame with random sales figures
    np.random.seed(0)  # For reproducibility
    sales_data = np.random.randint(100, 1000, size=(12, 5))
    df = pd.DataFrame(sales_data, index=MONTHS, columns=PRODUCTS)
    
    # Calculate total sales per product
    total_sales = df.sum(axis=0)
    
    # Plot total sales per product using a line plot
    plt.figure(figsize=(10, 5))
    total_sales.plot(kind='line', marker='o', color='b')
    plt.title('Total Sales per Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    
    # Plot sales figures across products and months using a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Sales'})
    plt.title('Sales Heatmap')
    plt.xlabel('Product')
    plt.ylabel('Month')
    plt.xticks(rotation=45)
    plt.show()
    
    return df

# Call the function to generate the DataFrame and visualize the data
df = task_func()
print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test if the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (12, 5))  # 12 months and 5 products
    def test_dataframe_columns(self):
        """Test if the DataFrame has the correct column names."""
        df = task_func()
        expected_columns = PRODUCTS
        self.assertListEqual(list(df.columns), expected_columns)
    def test_dataframe_index(self):
        """Test if the DataFrame has the correct index."""
        df = task_func()
        expected_index = MONTHS
        self.assertListEqual(list(df.index), expected_index)
    def test_sales_range(self):
        """Test if sales figures are within the expected range."""
        df = task_func()
        self.assertTrue((df >= 100).all().all() and (df <= 1000).all().all())
    def test_returns_dataframe(self):
        """Test if the function returns a pandas DataFrame."""
        df = task_func()
        self.assertIsInstance(df, pd.DataFrame)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)