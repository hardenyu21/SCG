import re
import nltk
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure nltk's stopwords are downloaded
nltk.download('stopwords')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts, num_topics):
    # Preprocess the texts
    def preprocess(text):
        # Remove non-alphanumeric characters
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        # Remove stopwords
        text = ' '.join(word for word in text.split() if word not in STOPWORDS)
        return text

    # Preprocess all texts
    processed_texts = [preprocess(text) for text in texts]

    # Vectorize the processed texts using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_texts)

    # Apply NMF to extract topics
    nmf = NMF(n_components=num_topics, random_state=42)
    nmf.fit(tfidf_matrix)

    # Get the feature names (words)
    feature_names = vectorizer.get_feature_names_out()

    # Extract the topics
    topics = []
    for topic_idx, topic in enumerate(nmf.components_):
        # Get the indices of the top words for the current topic
        top_word_indices = topic.argsort()[:-11:-1]
        # Get the words corresponding to these indices
        top_words = [feature_names[i] for i in top_word_indices]
        topics.append(top_words)

    return topics