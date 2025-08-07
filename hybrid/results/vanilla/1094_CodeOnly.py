from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    # Tokenizer to extract words starting with $ and ignore those with only $
    tokenizer = RegexpTokenizer(r'\$\w+')
    tokens = tokenizer.tokenize(text)
    
    # Remove the $ symbol from each token
    dollar_words = [token[1:] for token in tokens if len(token) > 1]
    
    # Count the frequency of each dollar-prefixed word
    word_counts = Counter(dollar_words)
    
    # Get the five most common words
    most_common_words = word_counts.most_common(5)
    
    return most_common_words

# Example usage:
text = "The $price of the $product is $100. The $product is on $sale. $discount available. $$ is not a word."
print(task_func(text))