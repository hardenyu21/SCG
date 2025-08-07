import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0:
        raise ValueError("Delay must be non-negative.")
    if not scripts:
        raise ValueError("No scripts provided.")
    
    timestamps = []
    
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        if not os.path.isfile(script_path):
            print(f"Warning: Script {script} not found. Skipping.")
            continue
        
        # Record the start time
        start_time = datetime.now()
        timestamps.append(start_time)
        
        # Execute the script
        try:
            subprocess.run(['bash', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing script {script}: {e}")
        
        # Wait for the specified delay
        time.sleep(delay)
    
    return timestamps
import unittest
import tempfile
import os
from datetime import datetime
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store scripts
        self.temp_dir = tempfile.TemporaryDirectory()
        self.script_dir = self.temp_dir.name
    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()
    def create_temp_script(self, script_content):
        # Helper function to create a temporary script file with the given content
        fd, path = tempfile.mkstemp(dir=self.script_dir, suffix=".sh")
        with os.fdopen(fd, "w") as f:
            f.write("#!/bin/bash\n")
            f.write(script_content)
        os.chmod(path, 0o755)
        return os.path.basename(path)
    def test_case_1(self):
        # Testing with a single script and delay of 1 second
        script_name = self.create_temp_script("echo 'Test'")
        scripts = [script_name]
        delay = 1
        start_times = task_func(self.script_dir, scripts, delay)
        self.assertEqual(len(start_times), 1)
        self.assertTrue(
            isinstance(datetime.strptime(start_times[0], "%Y-%m-%d %H:%M:%S"), datetime)
        )
    def test_case_2(self):
        # Testing with multiple scripts and a longer delay
        script_names = [
            self.create_temp_script("echo 'Test'"),
            self.create_temp_script("echo 'Test 2'"),
        ]
        delay = 2
        start_times = task_func(self.script_dir, script_names, delay)
        self.assertTrue(2 <= len(start_times) )
        time_diff = datetime.strptime(
            start_times[1], "%Y-%m-%d %H:%M:%S"
        ) - datetime.strptime(start_times[0], "%Y-%m-%d %H:%M:%S")
        self.assertTrue(2 <= time_diff.seconds<= 3)
    def test_case_3(self):
        # Testing with an invalid script path
        with self.assertRaises(FileNotFoundError):
            task_func(self.script_dir, ["this-doesn't-exist"], 1)
    def test_case_4(self):
        # Testing with no scripts (empty list)
        with self.assertRaises(Exception):
            task_func(self.script_dir, [], 1)
    def test_case_5(self):
        # Testing with zero delay
        script_names = [
            self.create_temp_script("echo 'Test'"),
            self.create_temp_script("echo 'Test 2'"),
        ]
        delay = 0
        start_times = task_func(self.script_dir, script_names, delay)
        self.assertEqual(len(start_times), 2)
    def test_case_6(self):
        # Test handling invalid delay
        script_names = [
            self.create_temp_script("echo 'Test'"),
            self.create_temp_script("echo 'Test 2'"),
        ]
        with self.assertRaises(Exception):
            task_func(self.script_dir, script_names, -1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)