import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    try:
        # Fetch the content of the Wikipedia page
        page_content = wikipedia.page(page_title).content
        
        # Generate a word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(page_content)
        
        # Plot the word cloud
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')  # Turn off the axis
        
        # Return the Axes object
        return ax
    except wikipedia.exceptions.PageError:
        # Return None if the page does not exist
        return None