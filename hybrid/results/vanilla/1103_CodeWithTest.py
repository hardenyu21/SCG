import subprocess
import shutil
import os

def task_func(script_path: str, temp_dir: str) -> str:
    try:
        # Ensure the temporary directory exists
        os.makedirs(temp_dir, exist_ok=True)
        
        # Copy the script to the temporary directory
        script_name = os.path.basename(script_path)
        temp_script_path = os.path.join(temp_dir, script_name)
        shutil.copy(script_path, temp_script_path)
        
        # Change the current working directory to the temporary directory
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        # Execute the script
        result = subprocess.run(['python', script_name], check=True, capture_output=True, text=True)
        
        # Restore the original working directory
        os.chdir(original_cwd)
        
        # If the script executed successfully, return the success message
        return "Script executed successfully!"
    
    except subprocess.CalledProcessError as e:
        # If the script execution failed, return the failure message
        return f"Script execution failed! Error: {e.stderr}"
    
    except Exception as e:
        # Handle any other exceptions that may occur
        return f"Script execution failed! Error: {str(e)}"
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        f = open(self.test_dir+"/script4.py","w")
        f.write("print('Hello from script4')")
        f.close()
        f = open(self.test_dir+"/script1.py","w")
        f.write("import time\ntime.sleep(20)\nprint('waiting')")
        f.close()
        f = open(self.test_dir+"/script2.py","w")
        f.close()
        f = open(self.test_dir+"/script3.py","w")
        f.write("invalid python code")
        f.close()
        
        self.temp_dir = 'testdir_task_func/temp_dir'
        os.makedirs(self.temp_dir, exist_ok=True)
        
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    
    def test_case_1(self):
        # Testing with a non-existent script path
        result = task_func('/path/to/non_existent_script.py', self.temp_dir)
        self.assertEqual(result, "Script execution failed!")
        self.assertEqual(os.path.exists(self.temp_dir+"/non_existent_script.py"), False)
    
    def test_case_2(self):
        # Testing with a valid script path but the script contains errors
        # Assuming we have a script named "error_script.r" which contains intentional errors
        result = task_func(self.test_dir+"/script3.py", self.temp_dir)
        self.assertEqual(result, "Script execution failed!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script3.py"), True)
        
    def test_case_3(self):
        # Testing with a valid script path and the script executes successfully
        # Assuming we have a script named "sscript4.r" which runs without errors
        result = task_func(self.test_dir+"/script4.py", self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script4.py"), True)
    
    def test_case_4(self):
        # Testing with a script that takes a long time to execute
        # Assuming we have a script named "script1.r" that intentionally runs for a long time
        result = task_func(self.test_dir+"/script1.py", self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script1.py"), True)
    
    def test_case_5(self):
         # Testing with a script that empty
        result = task_func(self.test_dir+"/script2.py", self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script2.py"), True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)