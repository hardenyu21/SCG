import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    
    # Check if the threshold is a valid integer within the range 0-255
    if not isinstance(threshold, int) or not (0 <= threshold <= 255):
        raise ValueError("Threshold must be an integer in the range 0-255.")
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binarize the image using the given threshold
    _, binary_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)
    
    # Save the binarized image
    cv2.imwrite('binary_image.jpg', binary_image)
    
    # Return the original grayscale and binarized images as numpy arrays
    return grayscale_image, binary_image