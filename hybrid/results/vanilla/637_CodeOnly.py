from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students: int) -> Tuple[pd.DataFrame, plt.Axes]:
    # Define course names and student names
    courses = ['Math', 'Science', 'History', 'English', 'Art']
    students = [f'Student_{i+1}' for i in range(num_students)]
    
    # Randomly select a subset of students
    selected_students = sample(students, num_students)
    
    # Generate random grades for each student in each course
    data = {
        student: [np.random.randint(50, 101) for _ in courses] for student in selected_students
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data, index=courses).T
    
    # Calculate average grade in each course
    average_grades = df.mean()
    
    # Calculate the number of students with a passing grade (>= 60) in each course
    passing_counts = (df >= 60).sum()
    
    # Create a new DataFrame to hold the results
    result_df = pd.DataFrame({
        'Average Grade': average_grades,
        'Passing Students': passing_counts
    })
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    result_df.plot(kind='bar', ax=ax)
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.set_xlabel('Courses')
    ax.set_ylabel('Count')
    ax.set_ylim(0, max(result_df.max()) + 5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return result_df, ax

# Example usage:
# df, ax = task_func(10)
# plt.show()