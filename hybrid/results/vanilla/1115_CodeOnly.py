import random
from string import ascii_uppercase

def task_func(dict1):
    def generate_random_string(length=5):
        return ''.join(random.choices(ascii_uppercase, k=length))
    
    unique_ids = []
    for department_code, employee_count in dict1.items():
        for _ in range(employee_count):
            unique_id = f"{department_code}{generate_random_string()}"
            unique_ids.append(unique_id)
    
    return unique_ids

# Example usage:
# departments = {'HR': 3, 'ENG': 2, 'MKT': 4}
# print(task_func(departments))