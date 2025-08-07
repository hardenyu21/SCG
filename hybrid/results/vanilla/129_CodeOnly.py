import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Raise an HTTPError for bad responses
        response.raise_for_status()
    except requests.ConnectionError:
        raise ConnectionError("Failed to connect to the URL.")
    except requests.HTTPError as e:
        raise requests.HTTPError(f"HTTP request failed with status code {e.response.status_code}.")

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first table in the page
    table = soup.find('table')
    if not table:
        raise ValueError("No table found on the page.")

    # Extract table headers
    headers = []
    header_row = table.find('tr')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all('th')]

    # Extract table rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row if present
        cols = row.find_all('td')
        if cols:
            rows.append([col.get_text(strip=True) for col in cols])

    if not rows:
        raise ValueError("No table data found on the page.")

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(rows, columns=headers if headers else None)

    return df