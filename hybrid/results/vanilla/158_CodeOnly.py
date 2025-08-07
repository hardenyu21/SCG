import json
import urllib.request
import gzip

def task_func(url_str, file_path):
    # Fetch JSON data from the given URL
    with urllib.request.urlopen(url_str) as response:
        json_data = response.read().decode('utf-8')
    
    # Decode the JSON data
    data = json.loads(json_data)
    
    # Compress the JSON data into a gzip file
    with gzip.open(file_path, 'wt', encoding='utf-8') as gzip_file:
        json.dump(data, gzip_file)
    
    # Return the path to the compressed gzip file
    return file_path