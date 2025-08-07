from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    # Check if the file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {img_path}")
    
    # Open the image using PIL
    original_image = Image.open(img_path)
    
    # Convert the image to a numpy array
    original_array = np.array(original_image)
    
    # Apply a blur filter
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Convert the blurred image to grayscale
    grayscale_image = blurred_image.convert('L')
    
    # Convert the grayscale image to a numpy array
    processed_array = np.array(grayscale_image)
    
    # Display both images side by side using OpenCV
    combined_image = np.hstack((original_array, cv2.cvtColor(processed_array, cv2.COLOR_GRAY2BGR)))
    cv2.imshow('Original and Processed Image', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Return the numpy arrays of the original and processed images
    return original_array, processed_array