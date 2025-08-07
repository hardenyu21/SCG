import matplotlib.pyplot as plt
import random

# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']

def task_func(number_list, bins):
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    
    # Randomly select a color from the predefined set
    color = random.choice(COLORS)
    
    # Plot the histogram
    ax.hist(number_list, bins=bins, color=color, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the axes object
    return ax