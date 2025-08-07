import socket
from ipaddress import IPv4Network
from threading import Thread

def task_func(ip_range, port):
    def check_port(ip, port, results):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Set a timeout for the connection attempt
                result = sock.connect_ex((str(ip), port))
                results[str(ip)] = (result == 0)
        except Exception as e:
            results[str(ip)] = False

    # Create a network object from the IP range
    network = IPv4Network(ip_range)
    results = {}

    # Create a thread for each IP address in the range
    threads = []
    for ip in network:
        thread = Thread(target=check_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return results

# Example usage:
# ip_range = '192.168.1.0/30'
# port = 80
# print(task_func(ip_range, port))