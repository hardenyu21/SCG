import csv
import json
import os

def task_func(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    # Define the output JSON file name
    json_file_name = os.path.splitext(file_name)[0] + '.json'
    
    # Read the CSV file and convert it to JSON
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    
    # Write the JSON data to a file
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Return the name of the created JSON file
    return json_file_name