import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Ensure the input series are pandas Series with the correct index
    s1 = s1.reindex(CATEGORIES).fillna(0)
    s2 = s2.reindex(CATEGORIES).fillna(0)
    
    # Filter categories where both stores have sales exceeding the threshold
    threshold = 200
    valid_categories = (s1 > threshold) & (s2 > threshold)
    
    if not valid_categories.any():
        return None, 0.0
    
    # Select the valid categories
    s1_filtered = s1[valid_categories]
    s2_filtered = s2[valid_categories]
    
    # Compute the Euclidean distance between the two series
    euclidean_distance = np.linalg.norm(s1_filtered - s2_filtered)
    
    # Plot the bar plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(s1_filtered))
    
    ax.bar(index, s1_filtered, bar_width, label='Store 1')
    ax.bar(index + bar_width, s2_filtered, bar_width, label='Store 2')
    
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Comparison for Categories Exceeding $200')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(s1_filtered.index)
    ax.legend()
    
    plt.tight_layout()
    plt.show()
    
    return ax, euclidean_distance

# Example usage:
# s1 = pd.Series([250, 150, 300, 100, 220], index=CATEGORIES)
# s2 = pd.Series([210, 180, 350, 90, 240], index=CATEGORIES)
# ax, distance = task_func(s1, s2)
# print("Euclidean Distance:", distance)