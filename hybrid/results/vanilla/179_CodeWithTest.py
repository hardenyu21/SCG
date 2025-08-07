import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

def task_func(df):
    # Check if the DataFrame contains 'Title' and 'Content' columns
    if 'Title' not in df.columns or 'Content' not in df.columns:
        fig, ax = plt.subplots()
        return ax

    # Filter articles with titles containing "how" or "what"
    filtered_df = df[df['Title'].str.contains(r'\b(how|what)\b', case=False, na=False)]

    # If no articles match the criteria, return an empty plot
    if filtered_df.empty:
        fig, ax = plt.subplots()
        return ax

    # Extract content from the filtered articles
    contents = filtered_df['Content'].tolist()

    # Calculate TF-IDF scores
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(contents)
    feature_names = vectorizer.get_feature_names_out()

    # Calculate the average TF-IDF score for each feature
    avg_tfidf_scores = np.mean(tfidf_matrix.toarray(), axis=0)

    # Sort features by their average TF-IDF scores in descending order
    sorted_indices = np.argsort(avg_tfidf_scores)[::-1]
    sorted_feature_names = feature_names[sorted_indices]
    sorted_tfidf_scores = avg_tfidf_scores[sorted_indices]

    # Plot the TF-IDF scores
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.bar(sorted_feature_names, sorted_tfidf_scores)
    ax.set_ylabel('TF-IDF Score')
    ax.set_title('Average TF-IDF Scores for Articles with "How" or "What" in Title')
    plt.xticks(rotation=90)
    plt.tight_layout()

    return ax
import unittest
import pandas as pd
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.DATA = {
            'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
            'Content': ['This is a tutorial about coding...', 'Python is a programming language...',
                        'Programming is an art...', 'This is a cooking tutorial...', 'Life is complicated...']
        }
        self.df_sample = pd.DataFrame(self.DATA)
    def test_case_1(self):
        # Test with original data
        ax = task_func(self.df_sample)
        self.assertEqual(len(ax.patches), 11)  # Adjusting based on actual data
        self.assertEqual(ax.get_ylabel(), "TF-IDF Score")
    def test_case_2(self):
        # Test with no interesting articles
        df_no_interesting = self.df_sample.copy()
        df_no_interesting['Title'] = ['Coding 101', 'Python tutorial', 'Programming basics', 'Cooking basics',
                                      'Life basics']
        ax = task_func(df_no_interesting)
        self.assertEqual(len(ax.patches), 0)  # No bars in the plot as no interesting articles
    def test_case_3(self):
        # Test with only one interesting article
        df_one_interesting = self.df_sample.copy()
        df_one_interesting['Title'] = ['How to play guitar?', 'Python tutorial', 'Programming basics', 'Cooking basics',
                                       'Life basics']
        ax = task_func(df_one_interesting)
        self.assertEqual(len(ax.patches), 5)  # 5 unique words in the interesting article
    def test_case_4(self):
        # Test with data not containing columns 'Title' and 'Content'
        df_empty = pd.DataFrame(columns=['Title', 'Description'])
        ax = task_func(df_empty)
        self.assertEqual(len(ax.patches), 0)  # No bars in the plot as dataframe is empty
    def test_case_5(self):
        # Test with empty dataframe
        df_empty = pd.DataFrame(columns=['Title', 'Content'])
        ax = task_func(df_empty)
        self.assertEqual(len(ax.patches), 0)  # No bars in the plot as dataframe is empty


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)