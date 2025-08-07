from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file {img_path} cannot be found.")
    
    # Open the image file
    image = Image.open(img_path)
    image_array = np.array(image)
    
    # Create a figure to display the images
    fig, axes = plt.subplots(1, len(scale_factors), figsize=(15, 5))
    
    # List to store the Axes and scaled images
    scaled_images = []
    
    # Scale the image by each factor and display it
    for i, factor in enumerate(scale_factors):
        # Calculate new dimensions
        new_height = int(image_array.shape[0] * factor)
        new_width = int(image_array.shape[1] * factor)
        
        # Resize the image
        scaled_image = resize(image_array, (new_height, new_width), anti_aliasing=True)
        
        # Display the scaled image
        ax = axes[i]
        ax.imshow(scaled_image)
        ax.set_title(f'Scale {factor}')
        ax.axis('off')
        
        # Store the Axes and the scaled image
        scaled_images.append((ax, scaled_image))
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return scaled_images