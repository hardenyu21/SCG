from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge datasets on the id column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Extract the feature columns for clustering
    X = merged_df[[column1, column2]].values
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)
    kmeans.fit(X)
    
    # Get the cluster labels
    labels = kmeans.labels_
    
    # Create a scatterplot
    fig, ax = plt.subplots()
    scatter = ax.scatter(merged_df[column1], merged_df[column2], c=labels, cmap='viridis', marker='o')
    
    # Add labels and title
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title('KMeans Clustering')
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    
    # Return the cluster labels and the Axes object
    return labels, ax

# Example usage:
# df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.0, 2.0, 3.0]})
# df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': [4.0, 5.0, 6.0]})
# labels, ax = task_func(df1, df2)
# plt.show()
import unittest
import pandas as pd
import numpy as np
import matplotlib
class TestCases(unittest.TestCase):
    def setUp(self):
        # Sample dataframes for testing
        self.df1_base = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature1": [1.2, 3.4, 5.6, 7.8, 9.0]}
        )
        self.df2_base = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature2": [2.3, 4.5, 6.7, 8.9, 10.1]}
        )
    def tearDown(self):
        plt.close("all")
    def test_case_1(self):
        # Test scatterplot
        _, ax = task_func(self.df1_base, self.df2_base)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)
        self.assertEqual(ax.get_xlabel(), "feature1")
        self.assertEqual(ax.get_ylabel(), "feature2")
    def test_case_2(self):
        # Expect 2 clusters
        labels, _ = task_func(self.df1_base, self.df2_base)
        self.assertEqual(len(labels), 5)
        self.assertEqual(len(np.unique(labels)), 2)
    def test_case_3(self):
        # Mixed valid data types
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1.1, 2.2, 3.3]})
        labels, _ = task_func(df1, df2)
        self.assertEqual(len(labels), 3)
    def test_case_4(self):
        # Partial matches
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1.2, 3.4, 5.6]})
        df2 = pd.DataFrame({"id": [1, 2, 6], "feature2": [1.2, 3.1, 6.7]})
        labels, _ = task_func(df1, df2)
        self.assertEqual(len(labels), 2)
        self.assertEqual(len(np.unique(labels)), 2)
    def test_case_5(self):
        # Should fail when there's no matching id
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1.2, 3.4, 5.6]})
        df2 = pd.DataFrame({"id": [4, 5, 6], "feature2": [2.3, 4.5, 6.7]})
        with self.assertRaises(ValueError):
            task_func(df1, df2)
    def test_case_6(self):
        # Should fail on non-numeric columns
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["a", "b", "c"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1.1, 2.2, 3.3]})
        with self.assertRaises(Exception):
            task_func(df1, df2)
    def test_case_7(self):
        # Should fail on missing value
        df1 = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature1": [1.2, np.nan, 5.6, 7.8, 9.0]}
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature2": [2.3, 4.5, np.nan, 8.9, 10.1]}
        )
        with self.assertRaises(ValueError):
            task_func(df1, df2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)