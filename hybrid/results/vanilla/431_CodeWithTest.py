import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    # Check if the file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The specified image file '{image_file}' does not exist.")
    
    # Read the image using OpenCV
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"The file '{image_file}' is not a valid image.")
    
    # Create a histogram with 256 bins for pixel values 0 to 255
    histogram = np.zeros(256, dtype=int)
    
    # Flatten the image array and count the occurrences of each pixel value
    for pixel_value in image.flatten():
        histogram[pixel_value] += 1
    
    return histogram
import unittest
import numpy as np
import cv2
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a dummy grayscale image for testing
        self.dummy_image_path = 'dummy_image.png'
        np.random.seed(48)
        dummy_image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path, dummy_image)
        
        self.dummy_image_path_zero = 'dummy_image_zero.png'
        self.dummy_image_path_max = 'dummy_image_max.png'
        # Create an all-zero grayscale image
        zero_image = np.zeros((10, 10), dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path_zero, zero_image)
        # Create an all-max-value grayscale image
        max_image = np.full((10, 10), 255, dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path_max, max_image)
    def tearDown(self):
        # Cleanup the dummy image
        os.remove(self.dummy_image_path)
        os.remove(self.dummy_image_path_zero)
        os.remove(self.dummy_image_path_max)
    def test_histogram_output(self):
        histogram = task_func(self.dummy_image_path)
        with open('df_contents.txt', 'w') as file:
            file.write(str(histogram.tolist()))
        self.assertEqual(histogram.shape, (256,))
        self.assertTrue(np.all(histogram >= 0))
        
        expect = [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 3, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 3, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 2, 1, 1, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        self.assertEqual(histogram.tolist(), expect, "DataFrame contents should match the expected output")
    def test_nonexistent_image_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent_image.png')
    def test_invalid_image_file(self):
        with open('invalid_image.txt', 'w') as file:
            file.write("This is not an image file.")
        with self.assertRaises(ValueError):
            task_func('invalid_image.txt')
        os.remove('invalid_image.txt')
    def test_histogram_values(self):
        histogram = task_func(self.dummy_image_path)
        self.assertTrue(np.sum(histogram) == 100)  # 10x10 pixels
    
    def test_all_zero_image_histogram(self):
        histogram = task_func(self.dummy_image_path_zero)
        self.assertEqual(histogram[0], 100, "All pixels should be at value 0")
        self.assertTrue(np.all(histogram[1:] == 0), "No pixels should be present at other values")
    def test_all_max_value_image_histogram(self):
        histogram = task_func(self.dummy_image_path_max)
        self.assertEqual(histogram[-1], 100, "All pixels should be at maximum value 255")
        self.assertTrue(np.all(histogram[:-1] == 0), "No pixels should be present at other values")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)