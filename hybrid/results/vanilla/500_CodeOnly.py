import xlwt
import os

# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    # Create a new workbook and add a worksheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    
    # Write the header row
    for col_index, field in enumerate(FIELDS):
        worksheet.write(0, col_index, field)
    
    # Write the data rows
    for row_index, row_data in enumerate(values, start=1):
        for col_index, field in enumerate(FIELDS):
            worksheet.write(row_index, col_index, row_data.get(field, ''))
    
    # Save the workbook to the specified filename
    workbook.save(filename)
    
    # Return the absolute path of the created file
    return os.path.abspath(filename)

# Example usage
empty_data = []
path = task_func(empty_data, 'empty_data.xls')
print(os.path.exists(path) and 'empty_data.xls' in path)  # Should print True