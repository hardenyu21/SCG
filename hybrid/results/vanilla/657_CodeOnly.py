import re
import nltk
from gensim.models import Word2Vec

# Constants
ALPHANUMERIC = re.compile('[\W_]+')

def task_func(texts, stopwords=None):
    # Download stopwords if not provided
    if stopwords is None:
        nltk.download('stopwords')
        stopwords = set(nltk.corpus.stopwords.words('english'))
    
    # Preprocess the texts
    processed_texts = []
    for text in texts:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_text = ALPHANUMERIC.sub(' ', text).lower()
        # Tokenize the text
        tokens = cleaned_text.split()
        # Remove stopwords
        filtered_tokens = [word for word in tokens if word not in stopwords]
        processed_texts.append(filtered_tokens)
    
    # Train the Word2Vec model
    model = Word2Vec(sentences=processed_texts, vector_size=100, window=5, min_count=1, workers=4)
    
    return model

# Example usage
if __name__ == "__main__":
    texts = [
        "This is an example sentence.",
        "Another example, with different words!",
        "Gensim is a powerful library for NLP."
    ]
    model = task_func(texts)
    print(model.wv['example'])