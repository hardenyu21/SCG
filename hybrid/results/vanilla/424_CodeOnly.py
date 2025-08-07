import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    
    # Check if n_clusters is a positive integer
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer.")
    
    # Read the image
    original_image = cv2.imread(image_path)
    
    # Convert the image from BGR to RGB
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    # Reshape the image to a 2D array of pixels
    pixels = original_image_rgb.reshape((-1, 3))
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    kmeans.fit(pixels)
    
    # Get the cluster labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Replace each pixel with its corresponding centroid color
    segmented_image = centroids[labels].reshape(original_image_rgb.shape)
    
    # Convert the segmented image back to uint8
    segmented_image = segmented_image.astype(np.uint8)
    
    # Save each region as a separate image
    for i in range(n_clusters):
        # Create a mask for the current cluster
        mask = (labels == i)
        # Apply the mask to the original image
        region_image = original_image_rgb[mask]
        # Save the region image
        cv2.imwrite(f'region_{i}.jpg', region_image)
    
    # Return the original and segmented images as numpy arrays
    return original_image_rgb, segmented_image