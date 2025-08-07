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