import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    euclidean_dist = distance.euclidean(a, b)
    
    # Create a Pandas DataFrame from the lists with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Plot the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    df.plot(ax=ax, marker='o')
    ax.set_title(f'Euclidean Distance: {euclidean_dist:.2f}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    # Return the computed distance, DataFrame, and Axes object
    return euclidean_dist, df, ax

# Example usage:
# a = [1, 2, 3]
# b = [4, 5, 6]
# dist, df, ax = task_func(a, b)
# plt.show()