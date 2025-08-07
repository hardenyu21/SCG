import psutil
import platform

def task_func():
    # Get the operating system name
    os_name = platform.system()
    
    # Get the system architecture
    architecture = platform.architecture()[0]
    
    # Get memory details
    memory_info = psutil.virtual_memory()
    used_memory_percentage = (memory_info.used / memory_info.total) * 100
    
    # Format the memory usage percentage
    memory_usage = f"{used_memory_percentage:.2f}%"
    
    # Return the gathered details in a dictionary
    return {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': memory_usage
    }

# Example usage
if __name__ == "__main__":
    system_details = task_func()
    print(system_details)