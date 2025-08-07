import re
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

def task_func(text):
    # Extract words from the text
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a subplot
    fig, ax = plt.subplots()
    
    # Plot the histogram of word lengths
    ax.hist(word_lengths, bins=range(1, max(word_lengths) + 2), alpha=0.6, color='g', edgecolor='black', density=True)
    
    # If there are more than one unique word lengths, plot the KDE
    if len(set(word_lengths)) > 1:
        kde = gaussian_kde(word_lengths)
        x = range(1, max(word_lengths) + 1)
        ax.plot(x, kde(x), color='r', label='KDE')
        ax.legend()
    
    # Set labels and title
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Density')
    ax.set_title('Distribution of Word Lengths')
    
    # Show the plot
    plt.show()
    
    return ax