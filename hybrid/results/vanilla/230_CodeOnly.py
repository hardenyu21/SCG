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