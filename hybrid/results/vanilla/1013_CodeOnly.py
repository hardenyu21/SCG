import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

def task_func(
    url: str,
    base_url: str = "https://www.example.com",
    csv_file: str = "scraped_data.csv",
) -> int:
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return 0

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags
    links = soup.find_all('a', href=True)

    # Set to store unique absolute URLs
    unique_links = set()

    # Convert relative URLs to absolute URLs
    for link in links:
        href = link['href']
        absolute_url = urljoin(base_url, href)
        unique_links.add(absolute_url)

    # Write the unique links to a CSV file
    try:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['URL'])  # Write header
            for link in unique_links:
                writer.writerow([link])
    except IOError as e:
        print(f"Error writing to CSV file: {e}")
        return 0

    # Return the number of unique links
    return len(unique_links)