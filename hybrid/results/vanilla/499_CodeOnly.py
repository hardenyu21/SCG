import xlwt
import os
import io
import csv

def task_func(csv_content, filename):
    # Create a workbook and add a worksheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    
    # Use StringIO to simulate a file object from the CSV content
    csv_file = io.StringIO(csv_content)
    csv_reader = csv.reader(csv_file)
    
    # Write the CSV content to the Excel file
    for row_idx, row in enumerate(csv_reader):
        for col_idx, cell in enumerate(row):
            worksheet.write(row_idx, col_idx, cell)
    
    # Save the workbook to the specified filename
    workbook.save(filename)
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)

# Example usage
csv_content = 'Hello'
print(os.path.isfile(task_func(csv_content, 'single_cell.xls')))  # Should print True