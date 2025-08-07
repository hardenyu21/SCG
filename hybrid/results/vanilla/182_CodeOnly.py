import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

def task_func(df):
    # Filter articles by titles containing "how" or "what" (case-insensitive)
    filtered_df = df[df['title'].str.contains(r'\b(how|what)\b', case=False, regex=True)]
    
    # Extract the content of the filtered articles
    contents = filtered_df['content'].tolist()
    
    # Vectorize the content using CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(contents)
    
    # Determine the number of clusters (for simplicity, let's assume 5 clusters)
    num_clusters = 5
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    # Get the cluster labels for each article
    cluster_labels = kmeans.labels_.tolist()
    
    return cluster_labels