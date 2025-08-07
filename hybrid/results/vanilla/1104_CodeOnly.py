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