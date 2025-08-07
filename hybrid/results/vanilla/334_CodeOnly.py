from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def task_func(documents):
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer(tokenizer=word_tokenize, lowercase=True)
    
    # Fit and transform the documents to get the TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Get the feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Create a DataFrame from the TF-IDF matrix
    df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
    
    return df_tfidf

# Example usage:
documents = [
    "The quick brown fox jumps over the lazy dog",
    "Never jump over the lazy dog quickly",
    "A quick brown dog outpaces a quick fox"
]

df = task_func(documents)
print(df)