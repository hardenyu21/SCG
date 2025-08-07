import urllib.request
import os
import zipfile

# Constants
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def task_func(url):
    # Ensure the target directory exists
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    
    # Download the zip file from the specified URL
    urllib.request.urlretrieve(url, TARGET_ZIP_FILE)
    
    # Extract the contents of the zip file
    with zipfile.ZipFile(TARGET_ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall(TARGET_DIR)
    
    # Delete the local zip file after extraction
    os.remove(TARGET_ZIP_FILE)
    
    # Return the path of the directory where the contents are extracted
    return TARGET_DIR