import unicodedata
import requests

URL = 'https://api.github.com/users/'

def task_func(username):
    try:
        response = requests.get(URL + username)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        user_data = response.json()
        
        # Normalize all string data to ASCII
        normalized_data = {}
        for key, value in user_data.items():
            if isinstance(value, str):
                normalized_data[key] = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
            else:
                normalized_data[key] = value
        
        return normalized_data
    
    except requests.exceptions.HTTPError as http_err:
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"An error occurred: {err}")

# Example usage:
# user_info = task_func('octocat')
# print(user_info)