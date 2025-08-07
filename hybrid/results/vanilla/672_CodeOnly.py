import csv
import sys

def task_func(filename):
    # Read the CSV file and store the lines
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        lines = list(reader)
    
    # Reverse the order of the lines
    lines.reverse()
    
    # Write the reversed lines back to the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    
    # Reset the cursor to the beginning of the file
    with open(filename, mode='r+', newline='') as file:
        file.seek(0)

# Example usage:
# task_func('example.csv')