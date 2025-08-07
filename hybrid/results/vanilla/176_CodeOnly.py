import re
import socket

def task_func(ip_addresses: list) -> dict:
    # Regular expression to validate IPv4 addresses
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    
    def is_valid_ip(ip):
        if ip_pattern.match(ip):
            # Check if each octet is between 0 and 255
            return all(0 <= int(octet) <= 255 for octet in ip.split('.'))
        return False

    ip_to_hostname = {}
    
    for ip in ip_addresses:
        if is_valid_ip(ip):
            try:
                # Get the hostname for the IP address
                hostname = socket.gethostbyaddr(ip)[0]
                ip_to_hostname[ip] = hostname
            except (socket.herror, socket.gaierror):
                # If hostname cannot be determined, set value to None
                ip_to_hostname[ip] = None
        else:
            # If the IP is not valid, set value to None
            ip_to_hostname[ip] = None
    
    return ip_to_hostname