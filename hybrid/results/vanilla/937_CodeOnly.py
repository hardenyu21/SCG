import re
from collections import Counter

def task_func(input_str):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str).lower()
    
    # Count the frequency of each character
    frequency = Counter(cleaned_str)
    
    return dict(frequency)

# Example usage:
# result = task_func("Hello, World! 123")
# print(result)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '1': 1, '2': 1, '3': 1}