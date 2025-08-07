import os
from pathlib import Path
import pandas as pd
from docx import Document
import csv

def task_func(source_directory: str, target_directory: str) -> int:
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The source directory '{source_directory}' does not exist.")
    
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)
    
    # Define the supported file extensions
    supported_extensions = {'.txt', '.docx', '.xlsx', '.csv'}
    
    # Initialize a counter for successfully converted files
    converted_count = 0
    
    # Iterate over all files in the source directory
    for file_name in os.listdir(source_directory):
        # Construct the full file path
        file_path = os.path.join(source_directory, file_name)
        
        # Check if it's a file and has a supported extension
        if os.path.isfile(file_path) and Path(file_path).suffix in supported_extensions:
            # Determine the target file path
            target_file_path = os.path.join(target_directory, f"{Path(file_name).stem}.csv")
            
            # Read the content of the file based on its extension
            if Path(file_path).suffix == '.txt':
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            elif Path(file_path).suffix == '.docx':
                doc = Document(file_path)
                content = '\n'.join([para.text for para in doc.paragraphs])
            elif Path(file_path).suffix == '.xlsx':
                df = pd.read_excel(file_path)
                content = df.to_csv(index=False)
            elif Path(file_path).suffix == '.csv':
                df = pd.read_csv(file_path)
                content = df.to_csv(index=False)
            
            # Write the content to a CSV file
            with open(target_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Text'])
                csv_writer.writerow([content])
            
            # Increment the counter
            converted_count += 1
    
    return converted_count