import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

def task_func(seed=42, image_size=(100, 100, 3), range_low=0, range_high=255):
    # Check if range_low is less than range_high
    if range_low >= range_high:
        raise ValueError("range_low must be less than range_high.")
    
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Generate a random RGB image
    image = np.random.randint(range_low, range_high, size=image_size, dtype=np.uint8)
    
    # Plot the image
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')  # Turn off axis numbers and ticks
    plt.show()
    
    return ax, image

# Example usage
ax, image = task_func()