import pandas as pd
import numpy as np
from random import choice, seed as set_seed

def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    # Validate the number of students
    if num_of_students <= 0:
        raise ValueError("num_of_students must be a positive integer.")
    
    # Set the random seed for reproducibility
    set_seed(seed)
    np.random.seed(seed)
    
    # Default lists if none are provided
    if name_list is None:
        name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    if gender_list is None:
        gender_list = ["Male", "Female", "Other"]
    
    # Generate random data
    names = [choice(name_list) for _ in range(num_of_students)]
    ages = np.random.randint(age_range[0], age_range[1] + 1, size=num_of_students)
    genders = [choice(gender_list) for _ in range(num_of_students)]
    scores = np.random.randint(score_range[0], score_range[1] + 1, size=num_of_students)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Name': names,
        'Age': ages,
        'Gender': genders,
        'Score': scores
    })
    
    return df