import pandas as pd
import numpy as np
from random import randint

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    # Initialize a dictionary to store student data
    student_data = {student: [] for student in STUDENTS}
    
    # Generate random grades for each student in each course
    for student in STUDENTS:
        for course in COURSES:
            grade = randint(0, 100)  # Random grade between 0 and 100
            student_data[student].append(grade)
    
    # Calculate average grade for each student
    for student in STUDENTS:
        average_grade = np.mean(student_data[student])
        student_data[student].append(average_grade)
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(student_data, index=COURSES + ['Average'])
    
    # Transpose the DataFrame to have students as rows
    df = df.T
    
    # Rename the last column to 'Average'
    df.columns = COURSES + ['Average']
    
    return df

# Example usage
df = task_func()
print(df)