import matplotlib.pyplot as plt
from itertools import cycle, zip_longest

# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    """
    Plots a list of data series with different colors. Cycles through predefined colors
    if there are more data series than colors. Uses 'black' for series beyond colors + labels.

    Parameters:
    data (list of lists): The data series to plot.
    labels (list of str): The labels for each data series.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Cycle through colors and labels
    color_cycle = cycle(COLORS)
    label_cycle = cycle(labels)

    # Plot each data series
    for series, color, label in zip_longest(data, color_cycle, label_cycle, fillvalue='black'):
        ax.plot(series, label=label, color=color)

    # Add legend
    ax.legend()

    # Show plot
    plt.show()

    return ax

# Example usage:
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# labels = ['Series 1', 'Series 2', 'Series 3']
# task_func(data, labels)