import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url, table_id):
    try:
        # Send an HTTP request to the specified URL
        response = requests.get(url)
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise requests.exceptions.HTTPError(f"HTTP request failed: {e}")

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the specified ID
    table = soup.find('table', id=table_id)

    # Raise a ValueError if the table is not found
    if table is None:
        raise ValueError("Table with the specified ID not found.")

    # Extract the table headers
    headers = []
    header_row = table.find('tr')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all('th')]

    # Extract the table rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row if present
        cols = row.find_all(['td', 'th'])
        cols = [col.get_text(strip=True) for col in cols]
        rows.append(cols)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(rows, columns=headers)

    return df