from texttable import Texttable
import psutil

def task_func():
    # Create a new Texttable object
    table = Texttable()
    
    # Set the header for the table
    table.set_cols_align(["l", "r"])
    table.set_cols_valign(["m", "m"])
    table.add_rows([["Item", "Value"]])
    
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get memory usage percentage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    
    # Get disk usage percentage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    
    # Add rows to the table with the system information
    table.add_rows([
        ["CPU Usage (%)", f"{cpu_usage}%"],
        ["Memory Usage (%)", f"{memory_usage}%"],
        ["Disk Usage (%)", f"{disk_usage}%"]
    ])
    
    # Return the string representation of the table
    return table.draw()

# Example usage
if __name__ == "__main__":
    print(task_func())