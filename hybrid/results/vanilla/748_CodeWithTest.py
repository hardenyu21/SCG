import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Check if the required columns are present in the DataFrame
    if 'Age' not in df.columns or 'Weight' not in df.columns:
        raise KeyError("The input DataFrame must contain the columns 'Age' and 'Weight'.")
    
    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # If the filtered DataFrame is empty, return it as is
    if filtered_df.empty:
        return filtered_df
    
    # Select only the numerical columns for standardization
    numerical_cols = filtered_df.select_dtypes(include=['number']).columns
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the numerical columns
    filtered_df[numerical_cols] = scaler.fit_transform(filtered_df[numerical_cols])
    
    return filtered_df
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # This method will run before each test
        self.data = {
            "Age": [25, 35, 45, 20, 55, 30],
            "Weight": [60, 80, 75, 85, 65, 90],
            "Other_Column": [1, 2, 3, 4, 5, 6]  # Some additional data
        }
        self.df = pd.DataFrame(self.data)
    def test_standard_usage(self):
        result_df = task_func(self.df, 70, 1)
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape[1], self.df.shape[1])
        self.assertTrue((result_df.columns == self.df.columns).all())
        expected = pd.DataFrame(
            {'Age': {0: -0.8401680504168059, 1: 0.0, 2: 0.8401680504168059, 3: -1.260252075625209, 4: 1.6803361008336117, 5: -0.42008402520840293}, 'Weight': {0: -1.497409771854291, 1: 0.3940552031195508, 2: -0.07881104062390962, 3: 0.8669214468630112, 4: -1.0245435281108304, 5: 1.3397876906064716}, 'Other_Column': {0: -1.4638501094227998, 1: -0.8783100656536799, 2: -0.29277002188455997, 3: 0.29277002188455997, 4: 0.8783100656536799, 5: 1.4638501094227998}}
        )
        pd.testing.assert_frame_equal(result_df, expected, atol=1e-2)
    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        self.assertRaises(Exception, task_func, empty_df, 30, 70)
    def test_no_rows_meet_criteria(self):
        result_df = task_func(self.df, 15, 95)
        self.assertTrue(result_df.empty)
    def test_missing_columns(self):
        with self.assertRaises(KeyError):
            incomplete_df = self.df.drop(columns=["Age"])
            task_func(incomplete_df, 30, 70)
    def test_non_numeric_values(self):
        self.df['Age'] = self.df['Age'].astype(str)  # Converting Age to string
        with self.assertRaises(Exception):  # Assuming ValueError is raised for non-numeric inputs
            task_func(self.df, 30, 70)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)