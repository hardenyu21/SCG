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