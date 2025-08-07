import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(my_list, seed=42):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list.")
    
    # Add item "12" to the list
    my_list.append("12")
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Define the categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    
    # Generate random sales data for each category
    sales_data = np.random.randint(1000, 10000, size=len(categories))
    
    # Create a DataFrame with the sales data
    df_sales = pd.DataFrame({
        'Category': categories,
        'Sales': sales_data
    })
    
    # Plot the sales data
    fig, ax = plt.subplots()
    df_sales.plot(kind='bar', x='Category', y='Sales', ax=ax, legend=False)
    ax.set_ylabel('Sales')
    ax.set_title('Simulated Sales Data')
    
    # Return the DataFrame and the Axes object
    return df_sales, ax

# Example usage:
# my_list = []
# df, ax = task_func(my_list)
# plt.show()
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_reproducibility_with_seed(self):
        seed_value = 42
        data1, _ = task_func([1, 2, 3], seed=seed_value)
        data2, _ = task_func([1, 2, 3], seed=seed_value)
        pd.testing.assert_frame_equal(data1, data2)
    def test_output_types(self):
        my_list = [1, 2, 3]
        data, ax = task_func(my_list, 42)
        df_list = data.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        expect = ['Electronics,1605', 'Fashion,370', 'Home & Kitchen,513', 'Automotive,120', 'Sports,663']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            task_func("not a list")
    def test_plot_title(self):
        my_list = [1, 2, 3]
        _, ax = task_func(my_list)
        self.assertEqual(ax.get_title(), 'Category-wise Sales Data')
    def test_sales_data_length(self):
        my_list = [1, 2, 3]
        data, _ = task_func(my_list)
        self.assertEqual(len(data), 5)  # 5 categories


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)