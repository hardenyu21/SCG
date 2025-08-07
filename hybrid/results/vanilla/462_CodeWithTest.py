import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    # Validate the number of rows
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1.")
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Generate random data
    data = {
        'Category': [random.choice(categories) for _ in range(num_rows)],
        'Value': [random.randint(1, 100) for _ in range(num_rows)]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Plot the bar chart
    category_counts = df['Category'].value_counts()
    ax = category_counts.plot(kind='bar', title='Category Counts')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    
    # Show the plot
    plt.show()
    
    return df, ax

# Example usage:
# df, ax = task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42)
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with default parameters
        df, ax = task_func()
        self.assertEqual(len(df), 100)
        self.assertTrue(
            set(df["Category"].unique()).issubset(set(["a", "b", "c", "d", "e"]))
        )
        self.assertTrue(df["Value"].min() >= 1)
        self.assertTrue(df["Value"].max() <= 100)
        self.assertEqual(ax.get_title(), "Category Counts")
    def test_case_2(self):
        # Test num_rows
        for num_rows in [10, 50, 100]:
            df, _ = task_func(num_rows=num_rows)
            self.assertEqual(len(df), num_rows)
    def test_case_3(self):
        # Test edge case - 0 rows
        with self.assertRaises(Exception):
            task_func(num_rows=0)
    def test_case_4(self):
        # Test edge case - invalid num_rows
        with self.assertRaises(Exception):
            task_func(num_rows=-1)
    def test_case_5(self):
        # Test categories
        df, _ = task_func(categories=["x", "y", "z"])
        self.assertTrue(set(df["Category"].unique()).issubset(set(["x", "y", "z"])))
    def test_case_6(self):
        # Test edge case - single category
        df, _ = task_func(categories=["unique"])
        self.assertTrue(
            set(["unique"]).issubset(df["Category"].unique()),
            "Should work with a single category",
        )
    def test_case_7(self):
        # Test edge case - empty categories
        with self.assertRaises(Exception):
            task_func(categories=[])
    def test_case_8(self):
        # Test random seed
        df1, _ = task_func(random_seed=123)
        df2, _ = task_func(random_seed=123)
        df3, _ = task_func(random_seed=124)
        self.assertTrue(
            df1.equals(df2), "DataFrames should be identical with the same seed"
        )
        self.assertFalse(
            df1.equals(df3), "DataFrames should differ with different seeds"
        )
    def test_case_9(self):
        # Test visualization
        categories = ["x", "y", "z"]
        _, ax = task_func(num_rows=100, categories=categories, random_seed=42)
        ax_categories = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertListEqual(
            sorted(categories),
            sorted(ax_categories),
            "X-axis categories should match input categories",
        )
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)