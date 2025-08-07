import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Split the text into sentences using regex to handle periods followed by spaces or newlines
    sentences = re.split(r'\.\s*', text)
    
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the sentences to create the document-term matrix
    dtm = vectorizer.fit_transform(sentences)
    
    # Create a DataFrame from the document-term matrix
    df_dtm = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return df_dtm