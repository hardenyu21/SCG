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
import unittest
import os
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup code to create a test log file
        self.test_file_path = "test_log_file.log"
        with open(self.test_file_path, 'w') as f:
            f.write("ERROR 11:30:10 This is an error message\n")
            f.write("WARNING 11:35:10 This is a warning message\n")
    def tearDown(self):
        # Cleanup the test log file
        os.remove(self.test_file_path)
    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func("/path/to/nonexistent/file.log", ['ERROR', 'WARNING'])
    def test_empty_keywords(self):
        self.assertEqual(task_func(self.test_file_path, []), [])
    def test_single_keyword(self):
        result = task_func(self.test_file_path, ['ERROR'])
        self.assertTrue(all('ERROR' in line for line in result))
    def test_multiple_keywords(self):
        result = task_func(self.test_file_path, ['ERROR', 'WARNING'])
        self.assertTrue(all(any(kw in line for kw in ['ERROR', 'WARNING']) for line in result))
    def test_all_keywords(self):
        result = task_func(self.test_file_path, ['ERROR', 'WARNING', 'INFO'])
        self.assertTrue(len(result) >= 2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)