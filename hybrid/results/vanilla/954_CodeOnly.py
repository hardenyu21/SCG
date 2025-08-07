import random
import re

def task_func(target_words, n_sentences, vocabulary):
    # Validate inputs
    if n_sentences < 0:
        raise ValueError("n_sentences must be non-negative.")
    if not vocabulary:
        raise ValueError("The vocabulary must not be empty.")
    
    # Convert target words to lowercase for case-insensitive comparison
    target_words = [word.lower() for word in target_words]
    
    # Compile a regex pattern to match any of the target words
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in target_words) + r')\b')
    
    # Generate sentences
    sentences = []
    for _ in range(n_sentences):
        # Randomly sample 10 words with replacement from the vocabulary
        sentence = ' '.join(random.choices(vocabulary, k=10))
        
        # Replace spaces in target words with underscores
        sentence = pattern.sub(lambda match: match.group(0).replace(' ', '_'), sentence)
        
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        
        # Add the processed sentence to the list
        sentences.append(sentence)
    
    return sentences