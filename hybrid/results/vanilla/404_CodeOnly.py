import cv2
import numpy as np
import os

def task_func(img_path):
    # Check if the file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {img_path}")
    
    # Read the original image
    original_image = cv2.imread(img_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Find contours in the grayscale image
    contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Return the original image and the contours
    return original_image, contours