import random
import matplotlib.pyplot as plt

# Constants
SALARY_RANGE = (20000, 100000)

def task_func(dict1):
    # Extract the number of employees in the department with code 'EMPXX'
    num_employees = dict1.get('EMPXX', 0)
    
    # Generate random salaries for each employee
    salaries = [random.uniform(*SALARY_RANGE) for _ in range(num_employees)]
    
    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(salaries, bins=10, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Salary Distribution in EMPXX Department')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Number of Employees')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax