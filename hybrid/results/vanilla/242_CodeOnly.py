import cv2
import matplotlib.pyplot as plt
import numpy as np

def task_func(image_path, kernel_size):
    # Check if the kernel size is a positive integer
    if not isinstance(kernel_size, int) or kernel_size <= 0:
        raise ValueError("kernel_size must be a positive integer.")
    
    # Check if the image file exists
    if not cv2.haveImageReader(image_path):
        raise FileNotFoundError(f"The specified image file '{image_path}' does not exist.")
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The specified image file '{image_path}' could not be read.")
    
    # Convert the image from BGR to RGB for matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Apply the blur effect
    blurred_image = cv2.blur(image_rgb, (kernel_size, kernel_size))
    
    # Create a figure and axes for plotting
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot the original image
    axes[0].imshow(image_rgb)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Plot the blurred image
    axes[1].imshow(blurred_image)
    axes[1].set_title('Blurred Image')
    axes[1].axis('off')
    
    # Show the plots
    plt.tight_layout()
    plt.show()
    
    # Return the blurred image and the axes objects
    return blurred_image, axes[0], axes[1]