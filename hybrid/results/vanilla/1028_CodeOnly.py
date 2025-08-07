import subprocess
import time
import json
import platform

LOGFILE_PATH = "logfile.log"

def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Both 'interval' and 'duration' must be greater than zero.")
    
    start_time = time.time()
    end_time = start_time + duration
    cpu_usage_data = []

    while time.time() < end_time:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cpu_usage = get_cpu_usage()
        cpu_usage_data.append({"timestamp": timestamp, "cpu_usage": cpu_usage})
        time.sleep(interval)

    try:
        with open(LOGFILE_PATH, 'w') as logfile:
            json.dump(cpu_usage_data, logfile, indent=4)
        return LOGFILE_PATH
    except IOError:
        return None

def get_cpu_usage():
    if platform.system() == "Windows":
        # Use 'wmic' command to get CPU usage on Windows
        result = subprocess.run(['wmic', 'cpu', 'get', 'loadpercentage'], capture_output=True, text=True)
        if result.returncode == 0:
            # Extract the percentage value from the output
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                return int(lines[1].strip())
    elif platform.system() == "Linux":
        # Use 'top' command to get CPU usage on Linux
        result = subprocess.run(['top', '-bn1', '-H'], capture_output=True, text=True)
        if result.returncode == 0:
            # Extract the percentage value from the output
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                cpu_usage_line = lines[1].split()
                return int(cpu_usage_line[8].strip('%'))
    
    return 0  # Default to 0% if unable to retrieve CPU usage