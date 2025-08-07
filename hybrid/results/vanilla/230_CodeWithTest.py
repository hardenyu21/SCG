import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def task_func(df):
    # Check if the input is a valid DataFrame and contains the required columns
    if not isinstance(df, pd.DataFrame) or not all(column in df.columns for column in COLUMNS):
        return "Invalid input"
    
    # Consider only unique names
    unique_df = df.drop_duplicates(subset='Name')
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Histogram of scores
    sns.histplot(unique_df['Score'], bins=10, kde=True, ax=axes[0])
    axes[0].set_title("Histogram of Scores")
    axes[0].set_xlabel("Score")
    axes[0].set_ylabel("Frequency")
    
    # Boxplot of scores by country
    sns.boxplot(x='Country', y='Score', data=unique_df, ax=axes[1])
    axes[1].set_title("Boxplot of Scores by Country")
    axes[1].set_xlabel("Country")
    axes[1].set_ylabel("Score")
    
    # Adjust layout
    plt.tight_layout()
    
    return fig
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_valid_dataframe(self):
        # Test with a valid DataFrame with unique and duplicate 'Name' entries
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85},
            {'Name': 'James', 'Age': 35, 'Country': 'USA', 'Score': 90},
            {'Name': 'Lily', 'Age': 28, 'Country': 'Canada', 'Score': 92},
            {'Name': 'Sam', 'Age': 40, 'Country': 'UK', 'Score': 88},
            {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}
        ])
        fig = task_func(data)
        # Retrieve axes from the figure
        axes = fig.get_axes()
        # Assert titles
        self.assertEqual(axes[0].get_title(), 'Histogram of Scores')
        self.assertEqual(axes[1].get_title(), 'Boxplot of Scores by Country')
        
        # Assert data points in the boxplot
        for idx, country in enumerate(data['Country']):
            # Filter collection corresponding to the country
            for collection in axes[1].collections:
                if collection.get_label() == country:
                    self.assertIn(data['Score'][idx], collection.get_offsets()[:, 1])
                    break  # Exit inner loop once found
    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        data = pd.DataFrame([])
        result = task_func(data)
        self.assertEqual(result, "Invalid input")
    def test_missing_columns(self):
        # Test with a DataFrame missing required columns
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Score': 85},
            {'Name': 'Lily', 'Age': 28, 'Score': 92}
        ])
        result = task_func(data)
        self.assertEqual(result, "Invalid input")
    def test_non_dataframe_input(self):
        # Test with a non-DataFrame input
        data = "not a dataframe"
        result = task_func(data)
        self.assertEqual(result, "Invalid input")
    def test_plot_attributes(self):
        # Test if the plot contains the correct title, x-axis, y-axis, and data points
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85},
            {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}
        ])
        fig = task_func(data)
        # Retrieve axes from the figure
        axes = fig.get_axes()
        # Assert titles
        self.assertEqual(axes[0].get_title(), 'Histogram of Scores')
        self.assertEqual(axes[1].get_title(), 'Boxplot of Scores by Country')
        
        # Assert data points in the boxplot
        for idx, country in enumerate(data['Country']):
            # Filter collection corresponding to the country
            for collection in axes[1].collections:
                if collection.get_label() == country:
                    self.assertIn(data['Score'][idx], collection.get_offsets()[:, 1])
                    break  # Exit inner loop once found


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)