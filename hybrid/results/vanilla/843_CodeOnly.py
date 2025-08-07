import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    sentences = []
    for _ in range(n_sentences):
        # Randomly choose a number of words for the sentence (1 to 5)
        num_words = random.randint(1, 5)
        # Randomly select words from the WORD_LIST
        sentence_words = random.sample(WORD_LIST, num_words)
        # Join the words into a sentence
        sentence = ' '.join(sentence_words) + '.'
        # Append the sentence to the list
        sentences.append(sentence)
    
    # Join all sentences into a single string
    result = ' '.join(sentences)
    # Convert to lowercase and remove non-alphanumeric characters except spaces and periods
    result = re.sub(r'[^a-z0-9 .]', '', result.lower())
    
    return result

# Example usage
print(task_func(3))