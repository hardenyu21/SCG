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
import unittest
from PIL import Image
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a dummy image for testing
        self.dummy_img_path = "test_image.png"
        Image.fromarray(np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)).save(self.dummy_img_path)
    def tearDown(self):
        # Cleanup the dummy image
        os.remove(self.dummy_img_path)
    def test_scale_factors(self):
        results = task_func(self.dummy_img_path)
        self.assertEqual(len(results), 4)  # Check for 4 scale factors
    def test_return_type(self):
        results = task_func(self.dummy_img_path)
        for ax, img in results:
            self.assertIsInstance(ax, plt.Axes)
            self.assertIsInstance(img, np.ndarray)
    def test_scale_factor_effect(self):
        original_image = Image.open(self.dummy_img_path)
        original_size = original_image.size
        results = task_func(self.dummy_img_path)
        for _, img in results:
            self.assertNotEqual(img.shape[:2], original_size)  # Scaled image should differ in size
    def test_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            task_func("nonexistent.png")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)