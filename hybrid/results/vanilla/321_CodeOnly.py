import pandas as pd
import re
from scipy import stats
import matplotlib.pyplot as plt

def task_func(text):
    # Extract names not surrounded by square brackets
    names = re.findall(r'\b(?!\[)[A-Za-z]+\b(?!\])', text)
    
    # Count the frequency of each name
    name_counts = pd.Series(names).value_counts()
    
    # Create a bar chart of the name frequencies
    ax = None
    if not name_counts.empty:
        ax = name_counts.plot(kind='bar', title='Name Frequencies')
        plt.xlabel('Name')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(name_counts) if not name_counts.empty else None
    kurtosis = stats.kurtosis(name_counts) if not name_counts.empty else None
    
    return name_counts, ax, skewness, kurtosis