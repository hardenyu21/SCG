import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def task_func(dict1):
    # Extract employee names from the department "EMP$$"
    employees = [name for name, dept in dict1.items() if dept == "EMP$$"]
    
    # Generate random ages for each employee within the specified range
    ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for _ in employees]
    
    # Calculate mean
    mean_age = statistics.mean(ages)
    
    # Calculate median
    median_age = statistics.median(ages)
    
    # Calculate mode(s)
    try:
        mode_ages = statistics.mode(ages)
        mode_ages = [mode_ages]  # Convert to list for consistency
    except statistics.StatisticsError:
        # If there is no unique mode, calculate all modes
        mode_ages = statistics.multimode(ages)
    
    # Return the results as a tuple
    return (mean_age, median_age, mode_ages)

# Example usage:
# employee_dict = {
#     "Alice": "EMP$$",
#     "Bob": "HR",
#     "Charlie": "EMP$$",
#     "David": "EMP$$",
#     "Eve": "Marketing"
# }
# print(task_func(employee_dict))