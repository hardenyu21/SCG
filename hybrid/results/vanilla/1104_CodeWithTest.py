import subprocess
import os
import threading

def task_func(script_path: str, timeout: int = 60) -> str:
    # Check if the file exists
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"The file {script_path} does not exist.")
    
    # Function to run the script
    def run_script():
        try:
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError:
            pass

    # Create a thread to run the script
    script_thread = threading.Thread(target=run_script)
    script_thread.start()

    # Wait for the thread to complete or timeout
    script_thread.join(timeout)

    # Check if the thread is still alive, indicating a timeout
    if script_thread.is_alive():
        # Terminate the process
        script_thread.join()  # Ensure the thread is cleaned up
        return "Terminating process due to timeout."
    else:
        return "Script executed successfully."
import unittest
from unittest.mock import patch
import time
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        f = open(self.test_dir+"/script4.py","w")
        f.write("print('Hello from script4')")
        f.close()
        f = open(self.test_dir+"/script1.py","w")
        f.write("import time\ntime.sleep(10)\nprint('waiting')")
        f.close()
        f = open(self.test_dir+"/script2.py","w")
        f.close()
        f = open(self.test_dir+"/script3.py","w")
        f.write("import time\ntime.sleep(62)\nprint('waiting')")
        f.close()
        
        self.temp_dir = 'testdir_f_947/temp_dir'
        os.makedirs(self.temp_dir, exist_ok=True)
        
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    
    @patch('subprocess.call', return_value=None)
    def test_case_1(self, mock_subprocess):
        # Test with a short-running script
        result = task_func('/path/to/short_script.py', 10)
        self.assertEqual(result, 'Script executed successfully.')
    
    def test_case_2(self):
        # Test with a long-running script and short timeout
        result = task_func(self.test_dir+"/script1.py", 3)
        self.assertEqual(result, 'Terminating process due to timeout.')
    @patch('subprocess.call', return_value=None)
    def test_case_3(self, mock_subprocess):
        # Test default timeout behavior
        result = task_func('/path/to/short_script.py')
        self.assertEqual(result, 'Script executed successfully.')
    def test_case_4(self):
        # Test with a long-running script and long timeout
        result = task_func(self.test_dir+"/script1.py", 20)
        self.assertEqual(result, 'Script executed successfully.')
    def test_case_5(self):
        # Test with a long-running script and default timeout
        result = task_func(self.test_dir+"/script3.py")
        self.assertEqual(result, 'Terminating process due to timeout.')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)