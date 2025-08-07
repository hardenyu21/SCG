import collections
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Count the frequency of each letter in the dataset
    letter_counts = collections.Counter(data)
    
    # Find the letter with the maximum integer value
    max_value_letter = max(letter_counts.items(), key=itemgetter(1))[0]
    
    # Prepare data for plotting
    letters = list(letter_counts.keys())
    counts = list(letter_counts.values())
    
    # Create the bar plot
    fig, ax = plt.subplots()
    bars = ax.bar(letters, counts, label='Letter Counts')
    
    # Highlight the letter with the maximum value
    for bar, letter in zip(bars, letters):
        if letter == max_value_letter:
            bar.set_color('red')
    
    # Set labels and title
    ax.set_xlabel('Letter')
    ax.set_ylabel('Count')
    ax.set_title('Letter Counts with Max Value Letter Highlighted')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax