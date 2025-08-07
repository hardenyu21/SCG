import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=0):
    # Check if the DataFrame is empty or lacks required columns
    if df.empty or not {'date', 'value'}.issubset(df.columns):
        raise ValueError("The DataFrame is empty or lacks required columns.")
    
    # Convert the 'date' column to ordinal
    df['date_ordinal'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    
    # Perform KMeans clustering on 'date_ordinal' and 'value' columns
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    df['cluster'] = kmeans.fit_predict(df[['date_ordinal', 'value']])
    
    # Plot the clusters
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['date_ordinal'], df['value'], c=df['cluster'], cmap='viridis')
    
    # Add labels and title
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "group": ["A", "A", "A", "B", "B"],
            "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
            "value": [10, 20, 16, 31, 56],
        })
    def test_basic_functionality(self):
        ax = task_func(self.df)
        self.assertEqual(len(ax.collections), 1)  # Check if scatter plot is created
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())
    def test_missing_columns(self):
        incomplete_df = self.df.drop(columns=['date'])
        with self.assertRaises(ValueError):
            task_func(incomplete_df)
    def test_invalid_date_column(self):
        invalid_df = self.df.copy()
        invalid_df['date'] = "not a date"
        with self.assertRaises(ValueError):
            task_func(invalid_df)
    def test_plot_labels_and_title(self):
        ax = task_func(self.df)
        self.assertEqual(ax.get_xlabel(), 'Date (ordinal)')
        self.assertEqual(ax.get_ylabel(), 'Value')
        self.assertEqual(ax.get_title(), 'KMeans Clustering of Value vs Date')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)