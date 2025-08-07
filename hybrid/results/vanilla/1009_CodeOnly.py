import xml.etree.ElementTree as ET
import csv

def task_func(xml_content, output_csv_path):
    try:
        # Parse the XML content
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        raise ET.ParseError(f"Error parsing XML content: {e}")

    # Extract data from XML
    data = []
    headers = []

    # Assuming the XML structure is a list of items with the same tags
    if len(root) > 0:
        headers = list(root[0].keys())
        for item in root:
            row = [item.get(header) for header in headers]
            data.append(row)

    # Write data to CSV
    try:
        with open(output_csv_path, mode='w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            if headers:
                csvwriter.writerow(headers)
            csvwriter.writerows(data)
    except IOError as e:
        raise IOError(f"Error writing to CSV file: {e}")

# Example usage:
# xml_content = '<root><item name="Item1" value="Value1"/><item name="Item2" value="Value2"/></root>'
# output_csv_path = 'output.csv'
# task_func(xml_content, output_csv_path)