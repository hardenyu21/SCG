import re
import os
from collections import Counter

def task_func(folder_path: str) -> dict:
    # Regular expression pattern to match IP addresses
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    
    # Dictionary to store IP addresses and their counts
    ip_counts = Counter()
    
    # Iterate over all files in the specified directory
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Open and read the file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Find all IP addresses in the file content
                    ips = ip_pattern.findall(content)
                    
                    # Update the counter with the found IP addresses
                    ip_counts.update(ips)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    
    # Convert Counter to a regular dictionary and return
    return dict(ip_counts)