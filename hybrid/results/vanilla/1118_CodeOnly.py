import json
import csv
import requests
from io import StringIO

# Constants
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'

def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file from the specified URL
    response = requests.get(csv_url)
    response.raise_for_status()  # Raise an error for bad responses

    # Read the CSV data from the response
    csv_data = StringIO(response.text)
    csv_reader = csv.DictReader(csv_data)

    # Convert the CSV data to a list of dictionaries
    data_list = [row for row in csv_reader]

    # Convert the list of dictionaries to JSON format
    json_data = json.dumps(data_list, indent=4)

    # Save the JSON data to the specified file path
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

    # Return the path to the saved JSON file
    return json_file_path