import mechanize
from bs4 import BeautifulSoup

def task_func(url, form_id, data):
    # Create a new browser instance
    br = mechanize.Browser()
    
    # Open the URL
    br.open(url)
    
    # Select the form by its ID
    br.select_form(nr=0)  # Assuming the form is the first one, adjust if needed
    
    # Fill in the form fields with the provided data
    for key, value in data.items():
        br[key] = value
    
    # Submit the form
    response = br.submit()
    
    # Read the response content
    response_content = response.read()
    
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response_content, 'html.parser')
    
    # Extract the title of the page
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        return title_tag.string.strip()
    else:
        return 'No Title'

# Example usage:
# url = 'http://example.com'
# form_id = 'exampleForm'
# data = {'field1': 'value1', 'field2': 'value2'}
# print(task_func(url, form_id, data))