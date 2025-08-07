import requests
import os
import zipfile

def task_func(url, destination_directory, headers=None):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Download the zip file
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to download file from {url}. Status code: {response.status_code}")
    
    # Define the path for the downloaded zip file
    zip_file_path = os.path.join(destination_directory, 'downloaded_file.zip')
    
    # Save the zip file
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)
    
    # Extract the contents of the zip file
    extracted_files = []
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)
        extracted_files = zip_ref.namelist()
    
    # Remove the zip file after extraction
    os.remove(zip_file_path)
    
    return extracted_files