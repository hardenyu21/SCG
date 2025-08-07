import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded JSON string
    decoded_bytes = base64.b64decode(raw_string)
    decoded_string = decoded_bytes.decode('utf-8')
    
    # Parse the JSON string into a Python dictionary
    data = json.loads(decoded_string)
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full file path
    file_path = os.path.join(output_dir, filename)
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as csvfile:
        if data:
            # Use the keys of the first dictionary as the header
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            writer.writeheader()
            
            # Write the data rows
            for row in data:
                writer.writerow(row)
    
    # Return the path of the file
    return file_path