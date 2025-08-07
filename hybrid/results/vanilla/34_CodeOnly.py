import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(text):
    # Remove URLs from the text
    text_without_urls = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove any extra whitespace
    text_without_urls = text_without_urls.strip()
    
    # Check if there are any words left after removing URLs
    if not text_without_urls:
        raise ValueError("No words available to generate a word cloud after removing URLs.")
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_without_urls)
    
    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
    # Return the WordCloud object
    return wordcloud