import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, bins=4):
    # Count duplicate values in the 'value' column
    value_counts = df['value'].value_counts()
    duplicates = value_counts[value_counts > 1]
    duplicate_counter = Counter(duplicates)

    # Plot histogram and normal distribution curve
    fig, ax = plt.subplots()
    # Plot histogram
    ax.hist(df['value'], bins=bins, color='green', alpha=0.6, edgecolor='black', label='Histogram')

    # Fit a normal distribution to the data
    mu, std = norm.fit(df['value'])

    # Plot the normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p * len(df) * (xmax - xmin) / bins, 'k', linewidth=2, label='Normal Distribution')

    # Add labels and title
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()

    # Return the counter and the axes object
    return duplicate_counter, ax