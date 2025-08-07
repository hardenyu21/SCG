import subprocess
import random

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'

def task_func():
    # Randomly select a script from the list
    selected_script = random.choice(SCRIPTS)
    
    # Construct the full path of the selected script
    script_path = f"{SCRIPTS_DIR}/{selected_script}"
    
    try:
        # Execute the selected script
        subprocess.run([script_path], check=True)
        print(f"Executed script: {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute script {script_path}: {e}")
    
    # Return the full path of the script that was executed
    return script_path

# Example usage
if __name__ == "__main__":
    executed_script = task_func()
    print(f"Script executed: {executed_script}")