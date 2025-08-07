import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Display the original image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    # Create a histogram of the image pixel intensities
    plt.subplot(1, 2, 2)
    ax = plt.gca()
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='gray', alpha=0.75)
    plt.title('Histogram of Pixel Intensities')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    
    # Save the histogram as a PNG file
    plt.savefig(histogram_path)
    
    # Show the plot
    plt.show()
    
    # Return the Axes object of the histogram plot
    return ax