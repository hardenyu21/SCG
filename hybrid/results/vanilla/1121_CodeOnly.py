import re
import urllib.parse
import requests

def task_func(myString, API_KEY):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain to geolocation data mapping
    domain_geolocation = {}
    
    for url in urls:
        # Parse the URL to extract the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Skip if domain is empty
        if not domain:
            continue
        
        # Construct the API request URL
        api_url = f"http://ip-api.com/json/{domain}?key={API_KEY}"
        
        try:
            # Make the API request
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse the JSON response
            geolocation_data = response.json()
            
            # Store the geolocation data in the dictionary
            domain_geolocation[domain] = geolocation_data
        
        except requests.RequestException as e:
            # If the request fails, store None for this domain
            domain_geolocation[domain] = None
    
    return domain_geolocation