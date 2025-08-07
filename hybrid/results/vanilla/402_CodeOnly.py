import re
import requests
import csv
import os

# Constants
API_URL = 'https://api.example.com/data'

def task_func(pattern):
    # Make a GET request to the API
    response = requests.get(API_URL)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API: {response.status_code}")
    
    # Parse the JSON response
    try:
        data = response.json()
    except json.JSONDecodeError:
        raise Exception("Failed to decode JSON response")
    
    # Extract the data from the JSON response
    if 'data' not in data:
        raise Exception("No 'data' key found in JSON response")
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Find all matches in the data
    matched_data = []
    for item in data['data']:
        if isinstance(item, str) and regex.search(item):
            matched_data.append([item])
    
    # Define the CSV file path
    csv_file_path = os.path.abspath("matched_data.csv")
    
    # Write the matched data to a CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(matched_data)
    
    # Return the absolute path to the CSV file
    return csv_file_path