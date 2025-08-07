import re
import json
import requests

def task_func(myString, token):
    # Regular expression to find URLs in the string
    url_pattern = re.compile(r'https?://[^\s]+')
    
    # Find all URLs in the string
    urls = url_pattern.findall(myString)
    
    # If no URL is found, return an empty dictionary
    if not urls:
        return {}
    
    # Use the first URL found
    first_url = urls[0]
    
    # Prepare the JSON payload
    payload = {
        'url': first_url
    }
    
    # Prepare the headers with the authorization token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    # Define the API endpoint (replace with the actual endpoint)
    api_endpoint = 'https://example.com/api/endpoint'
    
    # Send the POST request to the API
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(payload))
    
    # Return the response from the API
    return response.json()