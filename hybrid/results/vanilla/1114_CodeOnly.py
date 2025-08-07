from collections import defaultdict
from random import randint

def task_func(dict1):
    # Initialize a defaultdict to store department codes and their corresponding salaries
    emp_salaries = defaultdict(list)
    
    # Iterate over the input dictionary
    for dept_code, salaries in dict1.items():
        # Check if the department code starts with 'EMP$$'
        if dept_code.startswith('EMP$$'):
            # Add the salaries to the corresponding department code in the defaultdict
            emp_salaries[dept_code].extend(salaries)
    
    # Convert defaultdict to a regular dictionary before returning
    return dict(emp_salaries)

# Example usage:
# Sample input dictionary with department codes and lists of salaries
sample_dict = {
    'EMP$$001': [50000, 60000, 55000],
    'EMP$$002': [70000, 75000],
    'HR001': [45000, 47000],
    'EMP$$003': [80000, 85000, 90000],
    'FIN001': [65000, 70000]
}

# Call the function with the sample dictionary
result = task_func(sample_dict)
print(result)