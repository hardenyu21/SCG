import json
import csv

def task_func(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Check if the data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON data must be a list of dictionaries.")
    
    # Write the data to a CSV file
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
        
        # Write the header
        csv_writer.writeheader()
        
        # Write the data rows
        for item in data:
            csv_writer.writerow(item)
    
    # Return the path to the CSV file
    return csv_file