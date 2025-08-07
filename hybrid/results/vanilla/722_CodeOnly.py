import urllib.request
import os
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    try:
        # Download the file from the specified URL
        urllib.request.urlretrieve(url, TARGET_FILE)
        
        # Read the content of the downloaded file
        with open(TARGET_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Search for occurrences of the word 'ERROR'
        occurrences = len(re.findall(SEARCH_PATTERN, content, re.IGNORECASE))
        
        # Return the number of occurrences
        return occurrences
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

    finally:
        # Clean up the downloaded file
        if os.path.exists(TARGET_FILE):
            os.remove(TARGET_FILE)

# Example usage:
# occurrences = task_func('http://example.com/path/to/file.txt')
# print(f"Number of 'ERROR' occurrences: {occurrences}")