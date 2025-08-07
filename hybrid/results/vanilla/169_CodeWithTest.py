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
import unittest
from skimage import data
import numpy as np
class TestCases(unittest.TestCase):
    def test_return_types(self):
        image = data.coins()
        ax, filtered_image = task_func(image)
        self.assertIsInstance(ax, np.ndarray, "ax is not a numpy array")
        self.assertIsInstance(filtered_image, np.ndarray, "filtered_image is not a numpy array")
    def test_error_on_non_positive_sigma(self):
        image = data.coins()
        with self.assertRaises(ValueError):
            task_func(image, sigma=0)
    def test_error_on_invalid_image_type(self):
        invalid_image = "not an image"
        with self.assertRaises(TypeError):
            task_func(invalid_image)
    def test_subplot_titles(self):
        image = data.coins()
        ax, _ = task_func(image)
        self.assertEqual(ax[0].get_title(), 'Original', "Title of the first subplot is incorrect")
        self.assertEqual(ax[1].get_title(), 'Filtered', "Title of the second subplot is incorrect")
    def test_filtered_image_difference(self):
        image = data.coins()
        _, filtered_image = task_func(image)
        expect = gaussian_filter(image, sigma=2)
        self.assertFalse(np.array_equal(image, filtered_image), "Filtered image is not different from the original")
        self.assertEqual(expect.tolist(), filtered_image.tolist(), "Filtered image is not different from the original")
    def test_sigma_blurring_effect(self):
        image = data.coins()
        _, filtered_image = task_func(image, sigma=2)
        _, filtered_image_high_sigma = task_func(image, sigma=5)
        diff_original = np.sum(np.abs(image - filtered_image))
        diff_high_sigma = np.sum(np.abs(image - filtered_image_high_sigma))
        self.assertGreater(diff_high_sigma, diff_original, "Higher sigma does not increase blurring")
    def test_different_images(self):
        images = [data.coins(), data.camera(), data.astronaut()]
        for img in images:
            _, filtered_image = task_func(img)
            self.assertEqual(filtered_image.shape, img.shape, "Filtered image shape does not match original image shape")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)