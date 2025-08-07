import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df1, df2):
    # Ensure the dataframes are combined and the target is separated
    combined_df = pd.concat([df1, df2], axis=1)
    X = combined_df.drop(columns='target')  # Assuming 'target' is the column name for the target variable
    y = combined_df['target']
    
    # Perform feature selection using SelectKBest
    selector = SelectKBest(score_func=f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    
    # Get the mask of selected features
    mask = selector.get_support()
    
    # Get the list of selected feature names
    selected_features = X.columns[mask].tolist()
    
    # Create a correlation matrix for the selected features
    selected_df = X[selected_features]
    corr_matrix = selected_df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of Selected Features')
    plt.show()
    
    return selected_features, ax

# Example usage:
# df1 = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'feature3': [7, 8, 9]})
# df2 = pd.DataFrame({'target': [0, 1, 0]})
# selected_features, ax = task_func(df1, df2)
import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def tearDown(self):
        plt.close("all")
    def test_case_1(self):
        # Dataset with clear distinction between features
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3, 4, 5],
                "feature1": [5.5, 6.7, 7.8, 8.9, 9.0],
                "feature2": [1.1, 2.2, 3.3, 4.4, 5.5],
                "feature3": [0.5, 1.5, 2.5, 3.5, 4.5],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "target": [1, 0, 1, 0, 1]})
        # Calling the function and asserting results
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ["feature1", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_2(self):
        # Dataset with features having moderate correlation
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1.2, 3.4, 5.6],
                "feature2": [2.3, 4.5, 6.7],
                "feature3": [3.4, 5.6, 7.8],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [4.5, 6.7, 8.9]})
        # Calling the function and asserting results
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_3(self):
        # Dataset with balanced target values
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3, 4],
                "feature1": [2.5, 3.5, 4.5, 5.5],
                "feature2": [6.6, 7.7, 8.8, 9.9],
                "feature3": [10.1, 11.1, 12.1, 13.1],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3, 4], "target": [0, 1, 0, 1]})
        # Calling the function and asserting results
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_4(self):
        # Smaller dataset
        df1 = pd.DataFrame(
            {
                "id": [1, 2],
                "feature1": [3.3, 4.4],
                "feature2": [5.5, 6.6],
                "feature3": [7.7, 8.8],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2], "target": [1, 0]})
        # Calling the function and asserting results
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_5(self):
        # Dataset with different feature correlations
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [10, 20, 30],
                "feature2": [40, 50, 60],
                "feature3": [70, 80, 90],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})
        # Calling the function and asserting results
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_6(self):
        # Test handling errors - no "id"
        df1 = pd.DataFrame(
            {
                "feature1": [10, 20, 30],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})
        with self.assertRaises(KeyError):
            task_func(df1, df2)
    def test_case_7(self):
        # Test handling errors - wrong types
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": ["a", "b", 3],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})
        with self.assertRaises(ValueError):
            task_func(df1, df2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)