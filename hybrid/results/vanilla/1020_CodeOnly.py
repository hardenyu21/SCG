import json
import requests
import chardet

# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    try:
        # Make an HTTP GET request with a 5-second timeout
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses

        # Get the raw bytes content
        raw_content = response.content

        # Handle empty content
        if not raw_content:
            return {}

        # Detect encoding if not provided
        if from_encoding is None:
            detection = chardet.detect(raw_content)
            from_encoding = detection.get('encoding')
            if from_encoding is None:
                raise ValueError("Unable to detect encoding for non-empty content")

        # Decode the content using the detected or provided encoding
        decoded_content = raw_content.decode(from_encoding)

        # Re-encode the content to the target encoding
        re_encoded_content = decoded_content.encode(to_encoding)

        # Parse the JSON content
        json_data = json.loads(re_encoded_content.decode(to_encoding))

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return {}
    except ValueError as e:
        print(f"Value error: {e}")
        raise