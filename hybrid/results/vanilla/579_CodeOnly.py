import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def task_func(csv_file):
    try:
        # Read the CSV file
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            text_data = []
            for row in reader:
                for cell in row:
                    text_data.append(cell)
        
        # Normalize text to ASCII
        normalized_text = [unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii') for text in text_data]
        
        # Join all text into a single string and split into words
        all_text = ' '.join(normalized_text)
        words = all_text.split()
        
        # Count the words
        word_counts = Counter(words)
        
        # Get the 10 most common words
        most_common_words = word_counts.most_common(10)
        
        # Plot the 10 most common words
        words, frequencies = zip(*most_common_words)
        fig, ax = plt.subplots()
        ax.bar(words, frequencies)
        ax.set_xlabel('Words')
        ax.set_ylabel('Frequencies')
        ax.set_title('Top 10 Most Common Words')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Return the plot and the list of tuples
        return ax, most_common_words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {csv_file} was not found.")
    except IOError:
        raise IOError(f"An error occurred while reading the file {csv_file}.")