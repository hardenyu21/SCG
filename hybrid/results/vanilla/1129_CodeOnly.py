import json
import requests
import os
from datetime import datetime

def task_func(json_data, unknown_key, save_dir=None):
    # Parse the JSON string to find the URL associated with the specified key
    try:
        data = json.loads(json_data)
        url = data.get(unknown_key)
        if not url:
            raise ValueError(f"No URL found for key: {unknown_key}")
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON data") from e

    # Download the file from the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to download file from {url}") from e

    # Generate a timestamped filename
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = f"{unknown_key}_{timestamp}.txt"

    # Determine the save directory
    if save_dir:
        save_path = os.path.join(save_dir, filename)
    else:
        save_path = filename

    # Save the file
    try:
        with open(save_path, 'wb') as file:
            file.write(response.content)
    except IOError as e:
        raise RuntimeError(f"Failed to save file to {save_path}") from e

    # Return the absolute path of the downloaded file
    return os.path.abspath(save_path)