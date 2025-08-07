from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Check if the file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {img_path}")
    
    # Open the image
    original_image = Image.open(img_path)
    
    # Rotate the image
    rotated_image = original_image.rotate(angle, expand=True)
    
    # Convert images to numpy arrays
    original_array = np.array(original_image)
    rotated_array = np.array(rotated_image)
    
    # Display the images side by side
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original_array)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    axes[1].imshow(rotated_array)
    axes[1].set_title('Rotated Image')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Return the numpy arrays
    return original_array, rotated_array