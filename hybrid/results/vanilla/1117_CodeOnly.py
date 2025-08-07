import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Initialize a dictionary to hold the department data
    department_levels = collections.defaultdict(list)
    
    # Iterate over each department code and its corresponding employee count
    for department_code, employee_count in department_data.items():
        # Ensure the department code is valid
        if department_code not in PREFICES:
            raise ValueError(f"Invalid department code: {department_code}")
        
        # Randomly assign employee levels based on the employee count
        for _ in range(employee_count):
            # Randomly choose a level for each employee
            level = random.choice(LEVELS)
            department_levels[department_code].append(level)
    
    # Convert the dictionary to a JSON object
    json_object = json.dumps(department_levels, indent=4)
    
    return json_object

# Example usage
department_data = {
    'EMP$$': 5,
    'MAN$$': 3,
    'DEV$$': 7,
    'HR$$': 2
}

print(task_func(department_data))