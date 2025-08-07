import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    
    Args:
    ip_range (str): The IP address range in CIDR notation (e.g., '192.168.1.0/24').
    
    Returns:
    dict: A dictionary mapping IP addresses to their active status (True if active, False otherwise).
    
    Raises:
    subprocess.CalledProcessError: If a ping command fails due to a subprocess error.
    """
    ip_network = IPv4Network(ip_range)
    active_ips = {}

    for ip in ip_network:
        try:
            # Ping the IP address
            response = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Check if the ping was successful
            if response.returncode == 0:
                active_ips[str(ip)] = True
            else:
                active_ips[str(ip)] = False
        except subprocess.CalledProcessError as e:
            raise subprocess.CalledProcessError(response.returncode, response.args, response.stdout, response.stderr) from e

    return active_ips