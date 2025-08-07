import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split the text into words
    words = text.split()
    
    # Remove stopwords and duplicates
    unique_words = []
    seen = set()
    for word in words:
        if word not in STOPWORDS and word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Join the unique words back into a string
    cleaned_text = ' '.join(unique_words)
    
    # Analyze the sentiment of the cleaned text
    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment
    
    # Output the sentiment
    return f"Sentiment: {sentiment}"

# Example usage
text = "This is a sample text with some sample words and some stopwords."
print(task_func(text))