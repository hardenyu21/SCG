import re
from collections import Counter
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Download stopwords if not already downloaded
    try:
        stopwords.words('english')
    except LookupError:
        import nltk
        nltk.download('stopwords')
    
    # Get the set of English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Use regex to find words in the text
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out stopwords
    non_stop_words = [word for word in words if word not in stop_words]
    
    # Count the occurrences of each non-stop word
    word_counts = Counter(non_stop_words)
    
    return dict(word_counts)

# Example usage:
# text = "This is a sample text with some sample words."
# print(task_func(text))