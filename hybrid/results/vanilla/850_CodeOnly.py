import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize a list to store each student's grades and average
    data = []
    
    # Iterate over each student
    for student in students:
        # Generate random grades for each subject
        grades = [random.randint(0, 100) for _ in subjects]
        
        # Calculate the average grade
        average_grade = statistics.mean(grades)
        
        # Append the student's data to the list
        data.append([student] + grades + [average_grade])
    
    # Create a DataFrame with the appropriate columns
    columns = ['Student'] + subjects + ['Average Grade']
    df = pd.DataFrame(data, columns=columns)
    
    return df

# Example usage:
students = ['Alice', 'Bob', 'Charlie']
subjects = ['Math', 'Science', 'History']
seed = 42
grade_report = task_func(students, subjects, seed)
print(grade_report)