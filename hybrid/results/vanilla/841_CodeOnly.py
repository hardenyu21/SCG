import re
import json
from collections import defaultdict
import string

def task_func(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        
        # Check if the "text" field is present
        if "text" not in data:
            return {}
        
        # Extract the text
        text = data["text"]
        
        # Convert text to lowercase
        text = text.lower()
        
        # Remove punctuation using string.punctuation
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        
        # Split the text into words
        words = text.split()
        
        # Count the frequency of each word
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        return dict(word_count)
    
    except (json.JSONDecodeError, TypeError):
        # Return an empty dictionary if JSON is malformed or other errors occur
        return {}