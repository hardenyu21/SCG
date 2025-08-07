import requests
from pathlib import Path
import zipfile

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def task_func(url, filename):
    try:
        # Ensure the download directory exists
        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
        
        # Download the file
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Save the file to the download directory
        file_path = DOWNLOAD_DIR / filename
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        # Ensure the unzip directory exists
        ZIP_DIR.mkdir(parents=True, exist_ok=True)
        
        # Extract the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(ZIP_DIR)
        
        # List the files in the unzipped directory
        unzipped_files = [f.name for f in ZIP_DIR.iterdir() if f.is_file()]
        
        return ("Success", unzipped_files)
    
    except requests.RequestException as e:
        return (f"Error: Network-related exception occurred - {str(e)}", [])
    except (zipfile.BadZipFile, FileNotFoundError, PermissionError) as e:
        return (f"Error: File-related exception occurred - {str(e)}", [])
    except Exception as e:
        return (f"Error: An unexpected error occurred - {str(e)}", [])

# Example usage:
# status, files = task_func("http://example.com/file.zip", "file.zip")
# print(status)
# print(files)