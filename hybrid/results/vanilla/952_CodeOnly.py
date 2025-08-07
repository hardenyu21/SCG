import pandas as pd
import random
from datetime import datetime

def task_func(
    task_list,
    n_tasks,
    employees=["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"],
    seed=None,
):
    # Validate the number of tasks
    if n_tasks < 0:
        raise ValueError("n_tasks must be non-negative.")
    
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Sanitize task names by replacing spaces with underscores
    sanitized_task_list = [task.replace(" ", "_") for task in task_list]
    
    # Randomly select the specified number of tasks
    selected_tasks = random.sample(sanitized_task_list, min(n_tasks, len(sanitized_task_list)))
    
    # Randomly assign each selected task to an employee
    assignments = []
    for task in selected_tasks:
        assigned_to = random.choice(employees)
        assignments.append({
            'Task Name': task,
            'Assigned To': assigned_to,
            'Due Date': datetime.now().strftime('%Y-%m-%d')
        })
    
    # Create a DataFrame from the assignments
    df = pd.DataFrame(assignments)
    
    return df