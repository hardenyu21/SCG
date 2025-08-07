from bs4 import BeautifulSoup
import requests

# Constants
URL = "http://example.com"

def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    # Check if the URL is empty or None
    if not url:
        return None
    
    try:
        # Fetch the web page
        response = requests.get(url)
        
        # Check if the response status code is 200 (OK)
        if response.status_code != 200:
            return None
        
        # Decode the content using the specified encoding
        content = response.content.decode(from_encoding)
        
        # Parse the HTML content using BeautifulSoup
        if use_lxml:
            soup = BeautifulSoup(content, 'lxml')
        else:
            soup = BeautifulSoup(content, 'html.parser')
        
        return soup
    
    except (requests.RequestException, UnicodeDecodeError):
        # Catch network errors, HTTP errors, and decoding issues
        return None