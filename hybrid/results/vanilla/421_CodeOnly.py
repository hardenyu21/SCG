import requests
import os
import json
import time

# Redefining the function in the current context
HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}

def task_func(url, directory, metadata):
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    # Check if the URL is valid
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise TypeError("The URL is invalid.")
    
    status_codes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Prepare the data to be sent
            files = {'file': open(file_path, 'rb')}
            data = {'metadata': json.dumps(metadata)}
            
            try:
                # Send the POST request
                response = requests.post(url, headers=HEADERS, files=files, data=data)
                
                # Append the status code to the list
                status_codes.append(response.status_code)
                
                # Pause for one second
                time.sleep(1)
            finally:
                # Ensure the file is closed
                files['file'].close()
    
    return status_codes