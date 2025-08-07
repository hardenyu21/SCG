import pandas as pd
import collections

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame.")
    
    # Remove duplicate customer names
    df_unique_customers = df.drop_duplicates(subset='Customer Name')
    
    # Calculate total sales
    total_sales = df_unique_customers['Sales'].sum()
    
    # Find the most popular sales category
    category_counts = collections.Counter(df_unique_customers['Category'])
    most_common_categories = category_counts.most_common()
    
    # In case of a tie, select the first category in alphabetical order
    max_count = most_common_categories[0][1]
    most_popular_categories = [category for category, count in most_common_categories if count == max_count]
    most_popular_category = sorted(most_popular_categories)[0]
    
    # Create the report dictionary
    report = {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }
    
    return report
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_regular(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Peter', 'Category': 'Beauty', 'Sales': 400},
            {'Customer': 'Nick', 'Category': 'Sports', 'Sales': 600}
        ])
        expected_output = {'Total Sales': 1800, 'Most Popular Category': 'Electronics'}
        self.assertEqual(task_func(data), expected_output)
    def test_case_with_duplicates(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'John', 'Category': 'Fashion', 'Sales': 200},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Peter', 'Category': 'Beauty', 'Sales': 400}
        ])
        expected_output = {'Total Sales': 1200, 'Most Popular Category': 'Electronics'}
        self.assertEqual(task_func(data), expected_output)
    def test_case_empty(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}
        ])
        expected_output = {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
        self.assertEqual(task_func(data), expected_output)
    def test_case_unique_customers(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}
        ])
        expected_output = {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
        self.assertEqual(task_func(data), expected_output)
    def test_case_tie_categories(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Nick', 'Category': 'Home', 'Sales': 200},
            {'Customer': 'Alice', 'Category': 'Electronics', 'Sales': 300}
        ])
        # In case of a tie, the first category in alphabetical order will be chosen
        expected_output = {'Total Sales': 1300, 'Most Popular Category': 'Electronics'}
        self.assertEqual(task_func(data), expected_output)
    def test_case_6(self):
        with self.assertRaises(ValueError):
            task_func("non_df")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)