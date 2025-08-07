import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    try:
        # Read the contents of the first file
        with open(file_path1, mode='r', newline='', encoding='utf-8') as file1:
            reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
            lines1 = list(reader1)
        
        # Read the contents of the second file
        with open(file_path2, mode='r', newline='', encoding='utf-8') as file2:
            reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)
            lines2 = list(reader2)
        
        # Check if either file is empty
        if not lines1:
            raise ValueError(f"The file {file_path1} is empty.")
        if not lines2:
            raise ValueError(f"The file {file_path2} is empty.")
        
        # Compare the lines using ndiff
        diff = ndiff(lines1, lines2)
        
        # Prepare the difference report
        differences = []
        line_number = 0
        
        for line in diff:
            if line.startswith('- '):
                differences.append({'Line Number': line_number, 'Status': '-', 'Content': line[2:]})
            elif line.startswith('+ '):
                differences.append({'Line Number': line_number, 'Status': '+', 'Content': line[2:]})
            elif line.startswith('  '):
                differences.append({'Line Number': line_number, 'Status': ' ', 'Content': line[2:]})
            line_number += 1
        
        # Create a DataFrame from the differences
        df = pd.DataFrame(differences)
        
        return df
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"One of the files was not found: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while processing the files: {e}")

# Example usage:
# df = task_func('file1.csv', 'file2.csv')
# print(df)