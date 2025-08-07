import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

def task_func(df):
    # Remove duplicate entries based on 'Name'
    df = df.drop_duplicates(subset='Name')
    
    # Standardize 'Age' and 'Score' columns
    scaler = StandardScaler()
    df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])
    
    # Plot a scatter plot of the standardized values
    fig, ax = plt.subplots()
    ax.scatter(df['Age'], df['Score'])
    ax.set_title("Scatter Plot of Standardized Age and Score")
    ax.set_xlabel("Age (standardized)")
    ax.set_ylabel("Score (standardized)")
    
    # Return the DataFrame and the Axes object
    return df, ax