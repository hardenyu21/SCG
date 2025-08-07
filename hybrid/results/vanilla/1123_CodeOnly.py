import re
import urllib.parse
import ssl
import socket
from datetime import datetime

def task_func(myString):
    # Regular expression to find all URLs in the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain and SSL certificate expiry date
    ssl_info = {}
    
    for url in urls:
        try:
            # Parse the URL to extract the domain
            parsed_url = urllib.parse.urlparse(url)
            domain = parsed_url.netloc
            
            # Create a default SSL context
            context = ssl.create_default_context()
            
            # Get the SSL certificate
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    # Extract the expiration date from the certificate
                    expiry_date = cert['notAfter']
                    expiry_datetime = datetime.strptime(expiry_date, '%b %d %H:%M:%S %Y %Z')
                    
                    # Store the domain and expiry date in the dictionary
                    ssl_info[domain] = expiry_datetime
        except (ssl.SSLError, socket.error, ValueError):
            # Ignore any SSL errors or socket errors
            continue
    
    return ssl_info