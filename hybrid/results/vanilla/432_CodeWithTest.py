import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import pandas as pd

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Create a contingency table from the specified columns
    contingency_table = pd.crosstab(merged_df[column1], merged_df[column2])
    
    # Perform the Chi-Squared test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Plot the heatmap of the contingency table
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(contingency_table, annot=True, fmt="d", cmap="YlGnBu")
    plt.title(f'Heatmap of {column1} vs {column2}')
    plt.xlabel(column2)
    plt.ylabel(column1)
    
    # Return the p-value and the heatmap
    return p, heatmap

# Example usage:
# df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature1': ['A', 'B', 'A', 'B']})
# df2 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature2': ['X', 'Y', 'X', 'Y']})
# p_value, heatmap = task_func(df1, df2)
# plt.show()
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing basic functionality with simple data
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["A", "B", "A"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": ["X", "Y", "X"]})
        p_value, heatmap = task_func(df1, df2)
        # P-value should be between 0 and 1 inclusive
        self.assertTrue(0.0 <= p_value <= 1.0)
        self.assertEqual(len(heatmap.get_yticklabels()), 2)  # A and B
        self.assertEqual(len(heatmap.get_xticklabels()), 2)  # X and Y
    def test_case_2(self):
        # Testing with distinct feature values across both dataframes
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["C", "D", "C"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": ["W", "W", "Z"]})
        p_value, heatmap = task_func(df1, df2)
        self.assertTrue(0.0 <= p_value <= 1.0)
        self.assertEqual(len(heatmap.get_yticklabels()), 2)  # C and D
        self.assertEqual(len(heatmap.get_xticklabels()), 2)  # W and Z
    def test_case_3(self):
        # Test custom feature column names
        df1 = pd.DataFrame({"id": [1, 2, 3], "foo": ["A", "B", "A"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "bar": ["X", "Y", "X"]})
        p_value, heatmap = task_func(df1, df2, column1="foo", column2="bar")
        self.assertTrue(0.0 <= p_value <= 1.0)
        self.assertEqual(len(heatmap.get_yticklabels()), 2)
        self.assertEqual(len(heatmap.get_xticklabels()), 2)
    def test_case_4(self):
        # Testing a scenario where the p-value is expected to be close to 0
        # This is because there's a strong association between feature1 and feature2
        df1 = pd.DataFrame(
            {"id": list(range(1, 21)), "feature1": ["A"] * 10 + ["B"] * 10}
        )
        df2 = pd.DataFrame(
            {"id": list(range(1, 21)), "feature2": ["X"] * 10 + ["Y"] * 10}
        )
        p_value, _ = task_func(df1, df2)
        self.assertTrue(0.0 <= p_value < 0.01)  # Expected p-value to be close to 0
    def test_case_5(self):
        # Test error handling - should fail when there is no 'id' column
        df1 = pd.DataFrame({"foo": [1, 2], "bar": [3, 4]})
        df2 = pd.DataFrame({"foo": [1, 2], "bar": [3, 4]})
        with self.assertRaises(KeyError):
            task_func(df1, df2)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)