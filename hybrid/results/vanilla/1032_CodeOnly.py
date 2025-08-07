import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

# Constants
LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):
    if rows == 0:
        print("No data to generate heatmap.")
        return None

    # Generate random strings
    random_strings = [''.join(random.choices(string.ascii_lowercase, k=string_length)) for _ in range(rows)]
    
    # Create a DataFrame from the list of strings
    df = pd.DataFrame(random_strings, columns=['random_string'])
    
    # Convert each string into a one-hot encoded format
    one_hot_encoded = df['random_string'].apply(lambda s: pd.Series({letter: (s.count(letter) > 0) for letter in LETTERS}))
    
    # Sum the one-hot encoded DataFrame to get the frequency of each letter
    letter_frequency = one_hot_encoded.sum()
    
    # Create a correlation matrix of the letter frequencies
    correlation_matrix = letter_frequency.corr().fillna(0)
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True, square=True)
    plt.title('Correlation Heatmap of Letter Frequencies')
    plt.show()
    
    return ax

# Example usage
task_func(rows=1000, string_length=3)