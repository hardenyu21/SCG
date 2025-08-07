import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    # Check if the file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The specified image file '{image_file}' does not exist.")
    
    # Read the image using OpenCV
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"The file '{image_file}' is not a valid image.")
    
    # Create a histogram with 256 bins for pixel values 0 to 255
    histogram = np.zeros(256, dtype=int)
    
    # Flatten the image array and count the occurrences of each pixel value
    for pixel_value in image.flatten():
        histogram[pixel_value] += 1
    
    return histogram