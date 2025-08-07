import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Generate random ratings for each product based on the provided weights
    assigned_ratings = choices(ratings, weights=weights, k=len(products))
    
    # Create a DataFrame with the products and their assigned ratings
    df = pd.DataFrame({'Product': products, 'Rating': assigned_ratings})
    
    # Sort the DataFrame by 'Rating' in descending order
    df_sorted = df.sort_values(by='Rating', ascending=False)
    
    return df_sorted

# Example usage:
products = ['Product A', 'Product B', 'Product C', 'Product D']
ratings = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]

df = task_func(products, ratings, weights)
print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.products = ["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"]
        self.ratings = [1, 2, 3, 4, 5]
        self.weights = [0.05, 0.1, 0.2, 0.3, 0.35]
    def test_random_reproducibility(self):
        df1 = task_func(self.products, self.ratings, self.weights, 42)
        df2 = task_func(self.products, self.ratings, self.weights, 42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_dataframe_structure(self):
        df = task_func(self.products, self.ratings, self.weights)
        self.assertEqual(list(df.columns), ['Product', 'Rating'])
        self.assertEqual(len(df), len(self.products))
    def test_rating_range(self):
        df = task_func(self.products, self.ratings, self.weights)
        self.assertTrue(df['Rating'].isin(self.ratings).all())
    def test_sort_order(self):
        df = task_func(self.products, self.ratings, self.weights)
        sorted_df = df.sort_values('Rating', ascending=False)
        pd.testing.assert_frame_equal(df, sorted_df)
    def test_different_seeds(self):
        df1 = task_func(self.products, self.ratings, self.weights, 42)
        df2 = task_func(self.products, self.ratings, self.weights, 24)
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(df1, df2)
    
    def test_values(self):
        df1 = task_func(self.products, self.ratings, self.weights, 42)
        df_list = df1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        expect = ['Apple Watch,5', 'iPhone,4', 'Macbook,3', 'Airpods,3', 'iPad,1']
   
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)