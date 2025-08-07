import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Make sure to download NLTK stopwords
nltk.download('stopwords')

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')

# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts):
    # Preprocess the text documents
    def preprocess(text):
        # Remove non-alphanumeric characters
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        return text

    # Preprocess all documents
    preprocessed_texts = [preprocess(text) for text in texts]

    # Initialize CountVectorizer with stop words
    vectorizer = CountVectorizer(stop_words=STOPWORDS)

    # Fit and transform the preprocessed texts to create the DTM
    dtm = vectorizer.fit_transform(preprocessed_texts)

    # Create a DataFrame from the DTM
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())

    return dtm_df

# Example usage:
# texts = ["This is a sample document.", "Another example document is here.", "And another one."]
# dtm_df = task_func(texts)
# print(dtm_df)