import csv
import io

def task_func(filename='sample.csv', from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Read the CSV file with the specified from_encoding
    with open(filename, 'r', encoding=from_encoding, newline='') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data_list = list(reader)
    
    # Convert the list of dictionaries to a CSV string with the specified to_encoding
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data_list[0].keys(), delimiter=delimiter)
    writer.writeheader()
    writer.writerows(data_list)
    
    # Get the CSV data as a string and encode it to the specified to_encoding
    csv_data = output.getvalue()
    csv_data_encoded = csv_data.encode(to_encoding).decode(to_encoding)
    
    return data_list, csv_data_encoded