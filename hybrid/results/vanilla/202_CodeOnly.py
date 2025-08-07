import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Define a URL pattern
    url_pattern = r'https?://[^\s"]+'
    
    # Load the JSON string into a Python dictionary
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return {}
    
    # Convert the dictionary to a string to search for URLs
    data_str = json.dumps(data)
    
    # Find all URLs in the string using the regex pattern
    urls = re.findall(url_pattern, data_str)
    
    # Count the occurrences of each URL
    url_counts = Counter(urls)
    
    # Return the top_n URLs with their counts
    return dict(url_counts.most_common(top_n))

# Example usage:
# json_str = '{"links": ["http://example.com", "https://example.com", "http://example.com/page", "https://example.com"]}'
# print(task_func(json_str))