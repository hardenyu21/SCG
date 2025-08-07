import re
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty or lacks the required columns
    if df.empty or not {'Title', 'Views', 'Likes'}.issubset(df.columns):
        fig, ax = plt.subplots()
        return ax

    # Filter videos with titles containing "how" or "what"
    pattern = re.compile(r'\b(how|what)\b', re.IGNORECASE)
    filtered_df = df[df['Title'].apply(lambda title: bool(pattern.search(title)))]

    # Check if there are any entries matching the search criteria
    if filtered_df.empty:
        fig, ax = plt.subplots()
        return ax

    # Calculate the like ratio for each video
    filtered_df['Like Ratio'] = filtered_df['Likes'] / filtered_df['Views']

    # Create a bar plot of the like ratios
    fig, ax = plt.subplots()
    filtered_df.plot(kind='bar', x='Title', y='Like Ratio', ax=ax)
    ax.set_title('Like Ratios for Videos with "How" or "What" in Title')
    ax.set_xlabel('Title')
    ax.set_ylabel('Like Ratio')
    ax.set_xticklabels(filtered_df['Title'], rotation=45, ha='right')

    return ax