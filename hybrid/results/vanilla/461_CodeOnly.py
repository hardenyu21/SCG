import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    # Check if the script path exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script path {script_path} does not exist.")
    
    # Start the subprocess
    try:
        process = subprocess.Popen(['bash', script_path])
    except Exception as e:
        raise RuntimeError(f"Failed to start the script: {e}")
    
    start_time = time.time()
    cpu_usage = 0.0
    memory_usage = 0
    
    while True:
        # Check if the process is still running
        if process.poll() is not None:
            break
        
        # Check if the process has become a zombie
        try:
            proc = psutil.Process(process.pid)
        except psutil.NoSuchProcess:
            break
        
        # Accumulate CPU and memory usage
        cpu_usage += proc.cpu_percent(interval=1)
        memory_usage += proc.memory_info().rss
        
        # Check for timeout
        if time.time() - start_time > timeout:
            process.terminate()
            break
    
    # Wait for the process to terminate
    process.wait()
    
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }