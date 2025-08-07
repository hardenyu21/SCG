import pandas as pd
from itertools import cycle
from random import randint, seed

def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):
    # Check if the list of students is empty
    if not students:
        raise ValueError("The list of students is empty.")
    
    # Set the random seed for reproducibility if provided
    if rng_seed is not None:
        seed(rng_seed)
    
    # Cycle through the list of students
    student_cycle = cycle(students)
    
    # Generate grades and compile them into a list of dictionaries
    grades_data = []
    for _ in range(n_grades):
        student = next(student_cycle)
        grade = randint(min(grade_range), max(grade_range))
        grades_data.append({'Student': student, 'Grade': grade})
    
    # Create a pandas DataFrame from the list of dictionaries
    grade_report = pd.DataFrame(grades_data)
    
    return grade_report

# Example usage
grade_report = task_func(5, rng_seed=12)
print(grade_report)