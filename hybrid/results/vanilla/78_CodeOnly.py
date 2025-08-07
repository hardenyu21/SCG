import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request: HttpRequest, header: list, csv_data: list) -> FileResponse:
    # Create an in-memory text stream
    output = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.writer(output)
    
    # Write the header to the CSV
    writer.writerow(header)
    
    # Write the CSV data
    for row in csv_data:
        writer.writerow(row)
    
    # Seek to the beginning of the stream
    output.seek(0)
    
    # Create a FileResponse object with the CSV data
    response = FileResponse(output, as_attachment=True, filename='data.csv')
    
    return response