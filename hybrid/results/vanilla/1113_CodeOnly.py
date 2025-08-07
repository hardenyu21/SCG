import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    # Initialize a defaultdict to store the count of records for each employee
    employee_record_count = collections.defaultdict(int)
    
    # Open the CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the row has at least one element
            if row:
                # Check if the first element of the row starts with the employee prefix
                if row[0].startswith(emp_prefix):
                    # Increment the count for this employee
                    employee_record_count[row[0]] += 1
    
    # Convert the defaultdict to a regular dictionary before returning
    return dict(employee_record_count)