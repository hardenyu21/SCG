from datetime import datetime, timedelta
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Parse the input date string to a datetime object
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Generate a list of the next 10 days starting from the input date
    date_list = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a Cartesian product of employees and dates
    employee_date_pairs = list(product(EMPLOYEES, date_list))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(employee_date_pairs, columns=['Employee', 'Date'])
    
    return df

# Example usage
if __name__ == "__main__":
    date_str = "2023-10-01"
    df = task_func(date_str)
    print(df)