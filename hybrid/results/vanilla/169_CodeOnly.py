import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def task_func(image, sigma=2):
    # Check if the input is a numpy array
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array.")
    
    # Check if sigma is positive
    if sigma <= 0:
        raise ValueError("Sigma must be a positive number.")
    
    # Apply Gaussian filter
    filtered_image = gaussian_filter(image, sigma=sigma)
    
    # Create a plot with two subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    # Display the original image
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original')
    ax[0].axis('off')
    
    # Display the filtered image
    ax[1].imshow(filtered_image, cmap='gray')
    ax[1].set_title('Filtered')
    ax[1].axis('off')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax, filtered_image