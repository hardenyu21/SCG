import ipaddress
import requests

def task_func(ip_range, timeout):
    try:
        # Validate and create a list of IP addresses from the CIDR range
        network = ipaddress.ip_network(ip_range, strict=False)
    except ValueError as e:
        raise ValueError("Invalid IP range provided.") from e

    active_ips = []

    for ip in network:
        try:
            # Send an HTTP GET request to the IP address
            response = requests.get(f"http://{ip}", timeout=timeout)
            # Check if the response status code is 200
            if response.status_code == 200:
                active_ips.append(str(ip))
        except requests.RequestException:
            # Ignore any request exceptions and continue to the next IP
            continue

    return active_ips