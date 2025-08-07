import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os

def task_func(file_path, onpick):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The image file '{file_path}' does not exist.")
    
    # Read the image using OpenCV
    image = cv2.imread(file_path)
    
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Calculate the histogram
    hist = cv2.calcHist([image_rgb], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Create a grid of indices
    x, y, z = np.indices((8, 8, 8))
    
    # Flatten the indices and histogram values
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    values = hist
    
    # Plot the histogram in 3D
    ax.scatter(x, y, z, c=values, cmap='viridis', picker=True)
    
    # Set labels
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    
    # Connect the pick event to the onpick function
    fig.canvas.mpl_connect('pick_event', onpick)
    
    # Show the plot
    plt.show()
    
    return ax

# Example onpick function
def onpick(event):
    ind = event.ind
    print(f"Selected data point index: {ind}")

# Example usage
# task_func('path_to_image.jpg', onpick)