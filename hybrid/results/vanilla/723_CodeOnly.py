import urllib.request
from bs4 import BeautifulSoup
import csv
import os

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def task_func(url):
    # Fetch the content from the URL
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data (example: extracting all paragraph texts)
    data = []
    for paragraph in soup.find_all('p'):
        data.append(paragraph.get_text())

    # Save the data to a CSV file
    try:
        with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Paragraph Text'])  # Write header
            for item in data:
                writer.writerow([item])
    except Exception as e:
        print(f"Error writing to CSV file: {e}")
        return None

    return CSV_FILE_PATH

# Example usage
# url = 'http://example.com'
# csv_path = task_func(url)
# print(f"Data saved to {csv_path}")