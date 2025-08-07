import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    try:
        # Fetch the content of the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        webpage_content = response.text

        # Parse the webpage content
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Find all <script> tags
        script_tags = soup.find_all('script')

        # List to store successfully evaluated dictionaries
        evaluated_dicts = []

        # Iterate over each script tag
        for script in script_tags:
            script_content = script.string
            if script_content:
                # Attempt to evaluate the script content as a Python dictionary
                try:
                    # Use ast.literal_eval to safely evaluate the string
                    evaluated_content = ast.literal_eval(script_content)
                    # Check if the evaluated content is a dictionary
                    if isinstance(evaluated_content, dict):
                        evaluated_dicts.append(evaluated_content)
                except (ValueError, SyntaxError):
                    # If evaluation fails, continue to the next script tag
                    continue

        return evaluated_dicts

    except requests.RequestException:
        # Return an empty list if any error occurs during the request
        return []

# Example usage:
# result = task_func('https://example.com')
# print(result)