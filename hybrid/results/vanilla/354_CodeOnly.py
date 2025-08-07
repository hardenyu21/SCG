import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys=WORDS):
    # Initialize a counter for word occurrences
    word_counter = collections.Counter()

    # Iterate over each sentence in the dictionary
    for sentence in sentences_dict.values():
        # Split the sentence into words and update the counter
        words = sentence.lower().split()
        word_counter.update(words)

    # Filter the counter to only include the specified word keys
    filtered_counts = {word: word_counter[word] for word in word_keys}

    # Create a DataFrame for easier plotting
    df = pd.DataFrame(list(filtered_counts.items()), columns=['Word', 'Count'])

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Word'], df['Count'], color='skyblue')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency in Sentences')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Return the Axes object
    return ax

# Example usage:
# sentences_dict = {
#     'sentence1': "The quick brown fox jumps over the lazy dog.",
#     'sentence2': "I have a dream that one day this nation will rise up.",
#     'sentence3': "To be or not to be, that is the question."
# }
# ax = task_func(sentences_dict)
# plt.show()