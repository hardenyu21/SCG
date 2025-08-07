import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the page
        title = soup.title.string if soup.title else None

        # Prepare the data to be saved in JSON format
        data = {"title": title}

        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Write the JSON data to the file, with each title on a new line
            json.dump(data, file)
            file.write('\n')

        return file_name

    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None