import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Function to scale a group
    def scale_group(group):
        # Scale the 'Age' and 'Income' columns
        group[['Age', 'Income']] = scaler.fit_transform(group[['Age', 'Income']])
        return group
    
    # Apply the scaling function to each group by 'id'
    scaled_df = df.groupby('id').apply(scale_group).reset_index(drop=True)
    
    # Create a histogram of the 'Income' column after scaling
    plt.figure(figsize=(10, 6))
    plt.hist(scaled_df['Income'], bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Histogram of Scaled Income')
    plt.xlabel('Scaled Income')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # Get the histogram data
    histogram_data, bin_edges = np.histogram(scaled_df['Income'], bins=30)
    
    # Return the scaled DataFrame and the histogram data
    return scaled_df, histogram_data

# Example usage:
# df = pd.DataFrame({
#     'id': [1, 1, 2, 2, 3, 3],
#     'Age': [25, 30, 35, 40, 45, 50],
#     'Income': [50000, 60000, 70000, 80000, 90000, 100000]
# })
# scaled_df, histogram_data = task_func(df)
# print(scaled_df)
# print(histogram_data)
import unittest
import pandas as pd
from faker import Faker
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setting up Faker for test data generation
        self.fake = Faker()
    def generate_test_dataframe(self, num_rows):
        # Generating a test DataFrame with 'id', 'age', and 'income' columns
        data = {
            'id': [self.fake.random_int(min=1, max=5) for _ in range(num_rows)],
            'age': [self.fake.random_int(min=18, max=80) for _ in range(num_rows)],
            'income': [self.fake.random_int(min=20000, max=100000) for _ in range(num_rows)]
        }
        return pd.DataFrame(data)
    def test_empty_dataframe(self):
        df = pd.DataFrame()
        with self.assertRaises(Exception):
            scaled_df, income_hist = task_func(df)
    def test_single_group_dataframe(self):
        df = self.generate_test_dataframe(1)
        scaled_df, income_hist = task_func(df)
        self.assertEqual(len(scaled_df), 1)  # Only one row, hence one row in scaled DataFrame
        self.assertEqual(len(income_hist[0]), 10)  # Histogram should have 10 bins by default
    def test_multiple_groups_dataframe(self):
        df = self.generate_test_dataframe(100)
        scaled_df, income_hist = task_func(df)
        self.assertEqual(len(scaled_df), 100)  # Should have the same number of rows as input DataFrame
        self.assertEqual(len(income_hist[0]), 10)  # Checking histogram bin count
    def test_scaled_values_range(self):
        df = self.generate_test_dataframe(50)
        scaled_df, _ = task_func(df)
        self.assertEqual(len(scaled_df[(0.0 > scaled_df['age']) & (scaled_df['age'] > 1.0)]), 0)  # Age should be scaled between 0 and 1
        self.assertEqual(len(scaled_df[(0.0 > scaled_df['income']) & (scaled_df['income'] > 1.0)]), 0)  # Age should be scaled between 0 and 1
        
    def test_histogram_data_integrity(self):
        df = self.generate_test_dataframe(50)
        _, income_hist = task_func(df)
        self.assertTrue(np.all(income_hist[0] >= 0))  # Histogram counts should be non-negative
        self.assertTrue(np.all(np.diff(income_hist[1]) > 0))  # Histogram bins should be in ascending order


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)