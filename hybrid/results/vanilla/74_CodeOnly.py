import socket
import requests

def task_func(host):
    if not host:
        raise ValueError("The 'host' parameter cannot be None or an empty string.")
    
    try:
        # Resolve the IP address of the given host
        ip_address = socket.gethostbyname(host)
    except socket.gaierror as e:
        raise ConnectionError(f"Failed to resolve IP address for host '{host}': {e}")
    
    try:
        # Fetch geolocation information from the ipinfo.io API
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        geolocation_info = response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to fetch geolocation information for IP '{ip_address}': {e}")
    
    # Return a dictionary containing the IP address and geolocation information
    return {
        "ip": ip_address,
        "geolocation": geolocation_info
    }