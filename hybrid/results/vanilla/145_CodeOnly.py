import csv
from ipaddress import IPv4Network

def task_func(ip_range, csv_path):
    # Create an IPv4 network object from the given IP range
    network = IPv4Network(ip_range)
    
    # Open the CSV file for writing
    with open(csv_path, mode='w', newline='') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)
        
        # Iterate over each IP address in the network
        for ip in network:
            # Write the IP address as a row in the CSV file
            csvwriter.writerow([str(ip)])
    
    # Return the path to the generated CSV file
    return csv_path