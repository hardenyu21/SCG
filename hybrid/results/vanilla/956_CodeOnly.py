import re
import string
import random

def task_func(text: str, seed=None) -> str:
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Remove special characters (punctuation)
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    
    # Normalize whitespace
    text = text.replace(' ', '_')
    text = text.replace('\t', '__')
    text = text.replace('\n', '___')
    
    # Randomize character casing
    randomized_text = ''.join(
        char.upper() if random.random() < 0.5 else char.lower() for char in text
    )
    
    return randomized_text