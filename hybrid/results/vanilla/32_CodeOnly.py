import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first occurrence of the specified HTML tag
        element = soup.find(tag)
        
        # Return the text content of the tag if found, otherwise return None
        return element.get_text(strip=True) if element else None
    
    except requests.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return None