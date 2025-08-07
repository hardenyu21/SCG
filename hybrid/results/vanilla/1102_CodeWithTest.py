import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    # Record the start time
    start_time = datetime.now()
    
    # Prepare the command to run the R script
    command = f"Rscript {shlex.quote(script_path)}"
    
    # Run the command using subprocess
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Capture the stdout and stderr
    stdout, stderr = process.communicate()
    
    # Record the end time
    end_time = datetime.now()
    
    # Prepare the result dictionary
    result = {
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "stdout": stdout,
        "stderr": stderr
    }
    
    return result
import unittest
from unittest.mock import patch, Mock
class TestCases(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_case_1(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Script output here...", b"Any errors here...")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/script.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "Script output here...")
        self.assertEqual(result['Stderr'], "Any errors here...")
    
    @patch('subprocess.Popen')
    def test_case_2(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Another output...", b"")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/different_script.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "Another output...")
        self.assertEqual(result['Stderr'], "")
    
    @patch('subprocess.Popen')
    def test_case_3(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"", b"An error occurred...")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/erroneous_script.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "")
        self.assertEqual(result['Stderr'], "An error occurred...")
    @patch('subprocess.Popen')
    def test_case_4(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Script output for case 4...", b"")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/script_4.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "Script output for case 4...")
        self.assertEqual(result['Stderr'], "")
    
    @patch('subprocess.Popen')
    def test_case_5(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"", b"Error for case 5...")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/erroneous_script_5.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "")
        self.assertEqual(result['Stderr'], "Error for case 5...")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)