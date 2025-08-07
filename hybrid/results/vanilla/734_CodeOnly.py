import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter

def task_func(content):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(content)
    
    # Remove the last word
    words = words[:-1]
    
    # Get the POS tags for the words
    pos_tags = nltk.pos_tag(words)
    
    # Extract only the POS tags from the list of tuples
    pos_tags_list = [tag for word, tag in pos_tags]
    
    # Count the occurrences of each POS tag
    pos_count = Counter(pos_tags_list)
    
    return dict(pos_count)

# Example usage:
# sentence = "The quick brown fox jumps over the lazy dog."
# print(task_func(sentence))