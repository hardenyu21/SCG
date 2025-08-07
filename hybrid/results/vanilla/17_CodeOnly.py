import subprocess
import psutil
import time

def task_func(process_name: str) -> str:
    # Check if the process is running
    process_running = False
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == process_name:
                process_running = True
                # Terminate the process
                proc.terminate()
                proc.wait()  # Wait for the process to terminate
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if process_running:
        # Restart the process
        subprocess.Popen(process_name)
        return f"Process found. Restarting {process_name}."
    else:
        # Start the process
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."

# Example usage:
# print(task_func("notepad.exe"))