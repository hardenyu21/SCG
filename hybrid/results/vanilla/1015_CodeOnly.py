import requests
from lxml import html
import pandas as pd
import sqlite3

def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    try:
        # Fetch the HTML content from the URL
        response = requests.get(webpage_url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.content

    except requests.RequestException as e:
        raise requests.RequestException(f"Error fetching the webpage: {e}")

    try:
        # Parse the HTML content
        tree = html.fromstring(html_content)
        tables = tree.xpath('//table')

        if not tables:
            return 0  # No tables found

        # Convert the first table to a pandas DataFrame
        table = tables[0]
        df = pd.read_html(html.tostring(table))[0]

        if df.empty:
            return 0  # Table is empty

    except Exception as e:
        raise Exception(f"Error parsing the HTML table: {e}")

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Replace the existing table with the new data
        df.to_sql('my_table', conn, if_exists='replace', index=False)

        # Get the number of rows inserted
        cursor.execute("SELECT COUNT(*) FROM my_table")
        row_count = cursor.fetchone()[0]

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return row_count

    except sqlite3.DatabaseError as e:
        raise sqlite3.DatabaseError(f"Error with the SQLite database: {e}")