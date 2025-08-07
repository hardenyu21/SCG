from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points
    duplicates = df.duplicated(keep=False)
    duplicate_counts = Counter(df[duplicates].values.tolist())
    
    # Remove duplicates to get unique points
    unique_df = df.drop_duplicates()
    
    # Perform KMeans clustering on unique points
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_df['cluster'] = kmeans.fit_predict(unique_df)
    
    # Plot the clustered data
    fig, ax = plt.subplots()
    scatter = ax.scatter(unique_df.iloc[:, 0], unique_df.iloc[:, 1], c=unique_df['cluster'], cmap='viridis')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    ax.set_title('KMeans Clustering of Unique Points')
    
    return duplicate_counts, unique_df, ax

# Example usage:
# df = pd.DataFrame([[1, 2], [1, 2], [3, 4], [5, 6], [3, 4], [7, 8]], columns=['x', 'y'])
# duplicate_counts, clustered_df, ax = task_func(df)
# plt.show()
import unittest
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality with duplicates
        df = pd.DataFrame({"x": [1, 2, 2, 2, 3, 4], "y": [1, 1, 1, 1, 3, 3]})
        duplicates, df_clustered, ax = task_func(df, random_state=42)
        self.assertEqual(duplicates, Counter({(2, 1): 3}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
        self.assertFalse(df_clustered["cluster"].isna().any())
    def test_case_2(self):
        # Test functionality without duplicates
        df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [1, 2, 3, 4, 5, 6]})
        duplicates, df_clustered, ax = task_func(df, random_state=42)
        self.assertEqual(duplicates, Counter())
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
    def test_case_3(self):
        # Test functionality with all points being duplicates
        df = pd.DataFrame({"x": [1, 1, 1, 1, 1, 1], "y": [1, 1, 1, 1, 1, 1]})
        duplicates, df_clustered, ax = task_func(df, random_state=42)
        self.assertEqual(duplicates, Counter({(1, 1): 6}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
    def test_case_4(self):
        # Test with specified number of clusters
        df = pd.DataFrame({"x": [1, 2, 3, 40, 50, 60], "y": [1, 2, 3, 40, 50, 60]})
        duplicates, df_clustered, ax = task_func(df, n_clusters=2, random_state=42)
        self.assertEqual(duplicates, Counter())
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
    def test_case_5(self):
        # Test functionality with multiple duplicates
        df = pd.DataFrame(
            {"x": [1, 2, 3, 4, 5, 5, 5, 5], "y": [1, 2, 3, 4, 5, 5, 5, 5]}
        )
        duplicates, df_clustered, ax = task_func(df, random_state=42)
        self.assertEqual(duplicates, Counter({(5, 5): 4}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
        self.assertFalse(df_clustered["cluster"].isna().any())
    def test_case_6(self):
        # Test with a mix of unique points and duplicates
        df = pd.DataFrame(
            {"x": [1, 2, 3, 3, 3, 4, 5, 6], "y": [1, 2, 3, 3, 3, 4, 5, 6]}
        )
        duplicates, df_clustered, ax = task_func(df, random_state=42)
        self.assertEqual(duplicates, Counter({(3, 3): 3}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
        self.assertFalse(df_clustered["cluster"].isna().any())
    def test_case_7(self):
        # Easily separable data
        df = pd.DataFrame(
            {
                "x": [1, 2, 3, 10, 11, 12, 20, 21, 22],
                "y": [1, 2, 3, 10, 11, 12, 20, 21, 22],
            }
        )
        # We expect 3 clusters because of the natural separation in data
        duplicates, df_clustered, _ = task_func(df, n_clusters=3, random_state=42)
        self.assertEqual(duplicates, Counter())
        # Check that all points in a specific region belong to the same cluster
        cluster_1 = df_clustered[df_clustered["x"] <= 3]["cluster"].nunique()
        cluster_2 = df_clustered[(df_clustered["x"] > 3) & (df_clustered["x"] <= 12)][
            "cluster"
        ].nunique()
        cluster_3 = df_clustered[df_clustered["x"] > 12]["cluster"].nunique()
        self.assertEqual(
            cluster_1, 1
        )  # All points in this region should belong to the same cluster
        self.assertEqual(
            cluster_2, 1
        )  # All points in this region should belong to the same cluster
        self.assertEqual(
            cluster_3, 1
        )  # All points in this region should belong to the same cluster
    def test_case_8(self):
        # Test effects of random state on clustering outcome
        df = pd.DataFrame(
            {"x": [10, 20, 20, 40, 50, 60], "y": [10, 20, 20, 40, 50, 60]}
        )
        _, df_clustered_1, _ = task_func(df, n_clusters=2, random_state=42)
        _, df_clustered_2, _ = task_func(df, n_clusters=2, random_state=42)
        # Clusters should be the same for the same random state
        self.assertTrue((df_clustered_1["cluster"] == df_clustered_2["cluster"]).all())
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)