import re
import json
import requests

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        response.raise_for_status()  # Ensure we handle HTTP errors
        data = response.text

        # Use regular expression to find names not enclosed in square brackets
        # This regex assumes names are alphanumeric and may include spaces
        names = re.findall(r'(?<!\[)"([A-Za-z\s]+)"(?!\])', data)

        return names

    except Exception:
        return "Invalid url input"