import re
import socket
import urllib.parse

def task_func(myString):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domains and their IP addresses
    domain_ip_dict = {}
    
    for url in urls:
        # Parse the URL to extract the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Resolve the domain to an IP address
        try:
            ip_address = socket.gethostbyname(domain)
        except socket.gaierror:
            ip_address = None
        
        # Store the domain and IP address in the dictionary
        domain_ip_dict[domain] = ip_address
    
    return domain_ip_dict