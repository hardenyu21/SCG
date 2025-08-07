import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Use regex to find all words in the text
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the length of each word
    word_lengths = [len(word) for word in words]
    
    # Create a figure and a subplot
    fig, ax = plt.subplots()
    
    # Check if there are any word lengths to plot
    if word_lengths:
        # Plot the histogram of word lengths
        ax.hist(word_lengths, bins=range(1, max(word_lengths) + 2), rwidth=rwidth, edgecolor='black')
        ax.set_title('Distribution of Word Lengths')
        ax.set_xlabel('Word Length')
        ax.set_ylabel('Frequency')
    else:
        # If no words, set a title indicating the absence of data
        ax.set_title('No Words to Analyze')
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func("This is a simple example to demonstrate the function.")
# plt.show()