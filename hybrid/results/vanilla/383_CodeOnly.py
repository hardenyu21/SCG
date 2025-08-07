import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    # Tokenize the text into n-grams
    blob = TextBlob(text)
    ngrams = blob.ngrams(n=n)
    
    # Count the frequency of each n-gram
    ngram_counts = Counter(ngrams)
    
    # Get the top K n-grams
    top_ngrams = ngram_counts.most_common(top_k)
    
    # Convert the top n-grams to a DataFrame for visualization
    df = pd.DataFrame(top_ngrams, columns=['N-gram', 'Frequency'])
    
    # Plot the top K n-grams
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Frequency', y='N-gram', data=df, palette='viridis')
    plt.title(f'Top {top_k} {n}-grams')
    plt.xlabel('Frequency')
    plt.ylabel('N-gram')
    plt.show()

# Example usage:
# task_func("This is a test. This test is only a test.", 2, 3)