import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    try:
        # Read the CSV file
        try:
            df = pd.read_csv(file_path)
        except pd.errors.EmptyDataError:
            raise Exception("The file is empty.")
        
        # Check if the DataFrame has a header
        if 'Text' in df.columns:
            text_data = df['Text']
        else:
            text_data = df.iloc[:, 0]
        
        # Initialize CountVectorizer with the predefined stopwords
        vectorizer = CountVectorizer(stop_words=STOP_WORDS)
        
        # Fit and transform the text data
        word_counts = vectorizer.fit_transform(text_data)
        
        # Sum up the counts of each word
        sum_words = word_counts.sum(axis=0)
        
        # Get the words and their frequencies
        words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
        
        # Sort words by frequency in descending order
        words_freq.sort(key=lambda x: x[1], reverse=True)
        
        # Get the top 10 most common words
        top_words = words_freq[:10]
        
        # Separate words and their frequencies
        words, frequencies = zip(*top_words)
        
        # Plot the histogram
        fig, ax = plt.subplots()
        ax.bar(words, frequencies)
        ax.set_xlabel('Words')
        ax.set_ylabel('Frequency')
        ax.set_title('Top 10 Most Common Words')
        plt.xticks(rotation=45)
        
        # Save or display the plot
        if save_path:
            plt.savefig(save_path)
            plt.close(fig)
            return None
        else:
            plt.show()
            return ax
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None