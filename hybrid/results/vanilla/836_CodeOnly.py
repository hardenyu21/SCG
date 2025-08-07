import os
import shutil
import csv

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    
    # Ensure the processed directory exists if not in simulate mode
    if not simulate and not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Iterate over all files in the CSV directory
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_dir, filename)
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for index, row in enumerate(reader):
                    if row and row[0] == target_value:
                        result[filename] = index
                        break
    
    # Move processed files to the processed directory if not in simulate mode
    if not simulate:
        for filename in result:
            src_path = os.path.join(csv_dir, filename)
            dst_path = os.path.join(processed_dir, filename)
            shutil.move(src_path, dst_path)
    
    return result

# Example usage:
# result = task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
# print(result)