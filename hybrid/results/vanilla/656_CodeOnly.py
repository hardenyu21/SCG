import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation

def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    # Clean the text
    # Remove all non-alphanumeric characters except spaces
    text = ALPHANUMERIC.sub(' ', text)
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    
    # Analyze sentiment
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores

# Example usage
if __name__ == "__main__":
    sia = SentimentIntensityAnalyzer()
    text = "I love this product! It's amazing and works great."
    sentiment = task_func(text, sia)
    print(sentiment)