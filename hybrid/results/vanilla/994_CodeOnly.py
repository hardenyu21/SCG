import requests
import pandas as pd
from bs4 import BeautifulSoup

def task_func(url: str, csv_file_path: str) -> list:
    try:
        # Make an HTTP request to the specified URL with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching URL: {e}")

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the extracted data
    data = []

    # Iterate through each 'div' element with a class 'container'
    for container in soup.find_all('div', class_='container'):
        # Extract the text of 'h1' element, default to 'No Title' if not found
        title = container.find('h1').get_text(strip=True) if container.find('h1') else 'No Title'
        
        # Extract the text of 'span' element with class 'date', default to 'No Date' if not found
        date = container.find('span', class_='date').get_text(strip=True) if container.find('span', class_='date') else 'No Date'
        
        # Extract the text of 'span' element with class 'author', default to 'No Author' if not found
        author = container.find('span', class_='author').get_text(strip=True) if container.find('span', class_='author') else 'No Author'
        
        # Append the extracted data as a tuple to the list
        data.append((title, date, author))

    # Convert the list of tuples into a Pandas DataFrame
    df = pd.DataFrame(data, columns=['Title', 'Date', 'Author'])

    # Save the DataFrame to a CSV file at the specified file path
    df.to_csv(csv_file_path, index=False)

    # Return the list of tuples
    return data