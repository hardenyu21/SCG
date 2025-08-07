import codecs
import os
import zipfile

def task_func(directory_name="latin_files",
              content='Sopetón',
              file_names=['file1.txt', 'file2.txt', 'file3.txt'],
              encoding="latin-1"):
    # Create the directory
    os.makedirs(directory_name, exist_ok=True)
    
    # Write content to each file with the specified encoding
    for file_name in file_names:
        file_path = os.path.join(directory_name, file_name)
        with codecs.open(file_path, 'w', encoding) as file:
            file.write(content)
    
    # Create a zip file of the directory
    zip_file_name = f"{directory_name}.zip"
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_name in file_names:
            file_path = os.path.join(directory_name, file_name)
            zipf.write(file_path, os.path.relpath(file_path, directory_name))
    
    # Clean up the directory
    for file_name in file_names:
        file_path = os.path.join(directory_name, file_name)
        os.remove(file_path)
    os.rmdir(directory_name)
    
    return zip_file_name

# Example usage
zipped_file = task_func(directory_name="directorio", content='hi', file_names=["custom1.txt", "custom2.txt"], encoding='utf-8')
print(zipped_file)  # Output: directorio.zip