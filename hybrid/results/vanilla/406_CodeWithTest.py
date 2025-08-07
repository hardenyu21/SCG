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
import unittest
from PIL import Image, ImageDraw
import numpy as np
import os
def create_dummy_image(image_path='test_image.png', size=(10, 10)):
    """
    Creates a dummy color image for testing.
    The image size is 10x10 pixels.
    """
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)
    # Draw small shapes
    draw.point((2, 2), fill='red')  # Red point
    draw.point((5, 5), fill='green')  # Green point
    draw.point((8, 8), fill='blue')  # Blue point
    img.save(image_path)
class TestCases(unittest.TestCase):
    def setUp(self):
        create_dummy_image()
    def tearDown(self):
        os.remove('test_image.png')
    def test_normal_functionality(self):
        original_img, rotated_img = task_func('test_image.png', 45)
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(rotated_img, np.ndarray)
    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.png', 45)
    def test_zero_rotation(self):
        original_img, rotated_img = task_func('test_image.png', 0)
        self.assertTrue(np.array_equal(original_img, rotated_img))
    def test_full_rotation(self):
        original_img, rotated_img = task_func('test_image.png', 360)
        self.assertTrue(np.array_equal(original_img, rotated_img))
    def test_negative_angle(self):
        _, rotated_img = task_func('test_image.png', -45)
        self.assertIsInstance(rotated_img, np.ndarray)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)