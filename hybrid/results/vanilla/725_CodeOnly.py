import codecs
import os
import glob

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    # Ensure the directory path ends with a slash
    if not directory.endswith('/'):
        directory += '/'

    # Find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))

    for file_path in text_files:
        # Read the content of the file with the specified source encoding
        with codecs.open(file_path, 'r', from_encoding) as file:
            content = file.read()

        # Write the content back to the file with the specified target encoding
        with codecs.open(file_path, 'w', to_encoding) as file:
            file.write(content)

    # Output None as specified
    return None