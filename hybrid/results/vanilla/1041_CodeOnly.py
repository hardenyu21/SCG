import re
import os

def task_func(request):
    # Define the base directory where static files are stored
    BASE_DIR = 'static_files'
    
    # Regular expression to extract the filename from the GET request
    GET_REQUEST_REGEX = r'^GET\s+/(.+?)\s+HTTP/1\.1$'
    
    # Match the request against the regex
    match = re.match(GET_REQUEST_REGEX, request)
    
    if not match:
        return "HTTP/1.1 400 Bad Request\r\n\r\nInvalid request format"
    
    # Extract the filename from the request
    filename = match.group(1)
    
    # Construct the full file path
    file_path = os.path.join(BASE_DIR, filename)
    
    # Check if the file exists and is a file
    if not os.path.isfile(file_path):
        return "HTTP/1.1 404 Not Found\r\n\r\nFile not found"
    
    # Read the file content
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
    except Exception as e:
        return f"HTTP/1.1 500 Internal Server Error\r\n\r\nError reading file: {str(e)}"
    
    # Prepare the HTTP response
    response = (
        f"HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(file_content)}\r\n"
        f"Content-Type: application/octet-stream\r\n"
        "\r\n"
    ).encode('utf-8') + file_content
    
    return response.decode('utf-8')