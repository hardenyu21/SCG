import numpy as np
import matplotlib.pyplot as plt
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def task_func(word):
    # Convert the word to lowercase to ensure case insensitivity
    word = word.lower()
    
    # Get the positions of each letter in the word
    positions = [ALPHABET.index(letter) + 1 for letter in word if letter in ALPHABET]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(word)), positions, tick_label=list(word))
    
    # Set labels and title
    ax.set_xlabel('Letters in the word')
    ax.set_ylabel('Position in the alphabet')
    ax.set_title('Alphabet Positions of Letters in the Word')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func("example")