import requests
from PIL import Image
import io

def task_func(url):
    try:
        # Send a GET request to the URL with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is successful (200-299)
        response.raise_for_status()
        
        # Try to open the image using PIL
        image = Image.open(io.BytesIO(response.content))
        
        # Verify that the image is in a valid format
        image.verify()
        
        # Rewind the image file to the beginning
        image.seek(0)
        
        return image
    
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        raise ValueError(f"Failed to fetch the image from the URL: {e}")
    
    except (IOError, SyntaxError) as e:
        # Handle errors related to image format
        raise ValueError(f"The content fetched from the URL is not a valid image format: {e}")