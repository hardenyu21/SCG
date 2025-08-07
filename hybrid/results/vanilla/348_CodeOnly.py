import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Get a list of all running processes
    processes = subprocess.Popen(['pgrep', process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = processes.communicate()

    if error:
        print(f"Error finding processes: {error.decode()}")
        return 0

    # Decode the output and split into individual process IDs
    process_ids = output.decode().strip().split('\n')
    
    if not process_ids:
        return 0

    # Convert process IDs to integers
    process_ids = [int(pid) for pid in process_ids if pid.isdigit()]

    # Send a termination signal to each process
    for pid in process_ids:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            print(f"Process with PID {pid} not found.")
        except PermissionError:
            print(f"Permission denied to terminate process with PID {pid}.")

    # Wait for 1 second
    time.sleep(1)

    # Return the number of processes stopped
    return len(process_ids)