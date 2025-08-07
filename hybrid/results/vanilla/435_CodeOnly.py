import pandas as pd
from random import choice

def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    # Predefined job titles
    job_titles = ['Engineer', 'Manager', 'Analyst', 'Developer', 'Tester']
    
    # Randomly select a job title
    job_title = choice(job_titles)
    
    # Create a dictionary with the employee details
    employee_data = {
        'Name': [name],
        'Age': [age],
        'Code': [code],
        'Salary': [salary],
        'Bio': [bio],
        'Job Title': [job_title]
    }
    
    # Create a DataFrame from the dictionary
    data_df = pd.DataFrame(employee_data)
    
    return data_df

# Example usage:
# df = task_func('John Doe', 30, 'E123', 75000.0, 'Experienced software developer')
# print(df)