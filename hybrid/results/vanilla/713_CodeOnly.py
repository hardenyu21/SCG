import os
import re

def task_func(log_file_path: str, keywords: list):
    formatted_lines = []
    
    # Check if the file exists
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"The file {log_file_path} does not exist.")
    
    # Compile a regex pattern to match any of the keywords
    keyword_pattern = re.compile(r'\b(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b', re.IGNORECASE)
    
    # Read the log file line by line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Search for any of the keywords in the line
            match = keyword_pattern.search(line)
            if match:
                # Extract the keyword, timestamp, and message
                keyword = match.group(0)
                # Assuming the timestamp is the first part of the line before the first space
                timestamp = line.split(' ', 1)[0]
                # The message is the rest of the line after the first space
                message = line.split(' ', 1)[1].strip()
                # Format the line
                formatted_line = f"{keyword:<20}{timestamp:<20}{message}"
                formatted_lines.append(formatted_line)
    
    return formatted_lines