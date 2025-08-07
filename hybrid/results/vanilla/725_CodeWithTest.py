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
import unittest
from unittest.mock import patch
import os
import glob
import codecs
# Helper function to create a text file with specific encoding
def create_text_file(filename, content, encoding):
    with codecs.open(filename, 'w', encoding) as file:
        file.write(content)
import codecs
import os
import glob
# Constants
DIRECTORY_PATH = './files/'
class TestCases(unittest.TestCase):
    def setUp(self):
        os.makedirs('./test_files/', exist_ok=True)
        os.makedirs('./empty/', exist_ok=True)
        
    def tearDown(self):
        for filename in glob.glob('./test_files/*.txt'):
            os.remove(filename)
        os.rmdir('./test_files/')
        os.rmdir('./empty/')
    @patch('glob.glob')
    def test_encoding_conversion(self, mock_glob):
        mock_glob.return_value = ['./test_files/file1.txt', './test_files/file2.txt']
        create_text_file('./test_files/file1.txt', 'Hello', 'utf8')
        create_text_file('./test_files/file2.txt', 'World', 'utf8')
        task_func(directory='./test_files/', from_encoding='utf8', to_encoding='ascii')
        with codecs.open('./test_files/file1.txt', 'r', 'ascii') as file:
            self.assertEqual(file.read(), 'Hello')
        with codecs.open('./test_files/file2.txt', 'r', 'ascii') as file:
            self.assertEqual(file.read(), 'World')
            
    @patch('glob.glob')
    def test_empty_directory(self, mock_glob):
        mock_glob.return_value = []
        task_func(directory='./empty/', from_encoding='utf8', to_encoding='ascii')
        
    @patch('glob.glob')
    def test_same_encoding(self, mock_glob):
        mock_glob.return_value = ['./test_files/file3.txt']
        create_text_file('./test_files/file3.txt', 'Same Encoding', 'utf8')
        task_func(directory='./test_files/', from_encoding='utf8', to_encoding='utf8')
        with codecs.open('./test_files/file3.txt', 'r', 'utf8') as file:
            self.assertEqual(file.read(), 'Same Encoding')
            
    @patch('glob.glob')
    def test_invalid_encoding(self, mock_glob):
        mock_glob.return_value = ['./test_files/file4.txt']
        create_text_file('./test_files/file4.txt', 'Invalid', 'utf8')
        with self.assertRaises(LookupError):
            task_func(directory='./test_files/', from_encoding='utf8', to_encoding='invalid_encoding')
            
    @patch('glob.glob')
    def test_nonexistent_directory(self, mock_glob):
        mock_glob.return_value = []
        task_func(directory='./nonexistent/', from_encoding='utf8', to_encoding='ascii')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)