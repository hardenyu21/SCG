import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    
    # Validate the threshold value
    if not isinstance(threshold, int) or not (0 <= threshold <= 255):
        raise ValueError("Threshold must be an integer in the range 0-255.")
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binarize the image using the given threshold
    _, binarized_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)
    
    # Return the original grayscale and binarized images as numpy arrays
    return grayscale_image, binarized_image
import unittest
import os
from PIL import Image, ImageDraw
def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([5, 5, 15, 15], fill='black')
    img.save(image_path)
class TestCases(unittest.TestCase):
    def setUp(self):
        create_dummy_image()
    def tearDown(self):
        os.remove('test_image.jpg')
    def test_normal_functionality(self):
        original_img, binary_img = task_func('test_image.jpg', 10)
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(binary_img, np.ndarray)
        self.assertEqual(binary_img.max(), 255)
        self.assertEqual(binary_img.min(), 0)
    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.jpg')
    def test_invalid_threshold_non_integer(self):
        with self.assertRaises(ValueError):
            task_func('test_image.jpg', 'invalid')
    def test_invalid_threshold_out_of_range(self):
        with self.assertRaises(ValueError):
            task_func('test_image.jpg', -10)
    def test_threshold_effect(self):
        _, binary_img_high_threshold = task_func('test_image.jpg', 200)
        self.assertEqual(np.sum(binary_img_high_threshold), 71145)
    def test_binary_output_values(self):
        _, binary_img = task_func('test_image.jpg', 128)
        unique_values = np.unique(binary_img)
        self.assertTrue(np.array_equal(unique_values, [0, 255]))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)