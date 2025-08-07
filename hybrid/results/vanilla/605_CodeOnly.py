import pandas as pd
import matplotlib.pyplot as plt

def task_func(matrix):
    """
    Visualizes a 2D numeric array (matrix) as a heatmap using matplotlib.

    Parameters:
    matrix (list of lists or 2D numpy array): The numeric data to visualize.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object with the heatmap.
    """
    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Plot the heatmap with the 'hot' colormap and 'nearest' interpolation
    cax = ax.matshow(matrix, cmap='hot', interpolation='nearest')

    # Add a colorbar to the heatmap
    fig.colorbar(cax)

    # Display the plot
    plt.show()

    # Return the Axes object
    return ax