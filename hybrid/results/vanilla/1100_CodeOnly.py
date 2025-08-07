import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Function to remove URLs from text
    def remove_urls(text):
        return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove URLs from each document
    cleaned_texts = [remove_urls(text) for text in texts]

    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the cleaned texts to compute TF-IDF scores
    tfidf_matrix = vectorizer.fit_transform(cleaned_texts)

    # Get the feature names (unique words)
    feature_names = vectorizer.get_feature_names_out()

    # Convert the TF-IDF matrix to a dense format and round the scores to 8 decimal places
    dense_tfidf_matrix = tfidf_matrix.todense().round(8)

    # Create a list of tuples for each document's TF-IDF scores
    tfidf_scores = [tuple(row) for row in dense_tfidf_matrix]

    # Return the result as a tuple of (list of tuples, list of str)
    return (tfidf_scores, feature_names)