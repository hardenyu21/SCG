import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Create a generator object
    def data_generator():
        x = range_start
        while x <= range_end:
            sin_x = np.sin(x)
            cos_x = np.cos(x)
            abs_diff = abs(sin_x - cos_x)
            yield (x, sin_x, cos_x, abs_diff)
            x += step

    # Generate data for plotting
    data = list(data_generator())
    x_values, sin_values, cos_values, abs_diff_values = zip(*data)

    # Plot the sine, cosine, and absolute difference
    fig, ax = plt.subplots()
    ax.plot(x_values, sin_values, label='sin(x)')
    ax.plot(x_values, cos_values, label='cos(x)')
    ax.plot(x_values, abs_diff_values, label='|sin(x) - cos(x)|')
    ax.set_title('Sine, Cosine, and Absolute Difference')
    ax.set_xlabel('x')
    ax.set_ylabel('Value')
    ax.legend()

    # Compute the 1D FFT of the absolute difference
    fft_abs_diff = fft(abs_diff_values)
    fft_abs_diff_mean = np.mean(np.abs(fft_abs_diff))
    fft_abs_diff_median = np.median(np.abs(fft_abs_diff))

    # Return the generator, plot, and FFT statistics
    return data_generator(), ax, fft_abs_diff_mean, fft_abs_diff_median

# Example usage
gen, ax, mean_fft, median_fft = task_func()
plt.show()
print(f"Mean of FFT: {mean_fft}")
print(f"Median of FFT: {median_fft}")
import unittest
import types
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data, ax, _, _ = task_func()
        self.assertIsInstance(data, types.GeneratorType, "Returned data is not a generator")
        x, sin_x, cos_x, _ = next(data)
        self.assertAlmostEqual(x, -10.0, delta=0.01, msg="Unexpected x value in the first tuple")
        self.assertAlmostEqual(sin_x, np.sin(-10.0), delta=0.01, msg="Unexpected sin(x) value in the first tuple")
        self.assertAlmostEqual(cos_x, np.cos(-10.0), delta=0.01, msg="Unexpected cos(x) value in the first tuple")
    def test_case_2(self):
        data, ax, mean_fft, median_fft = task_func(23, 43, 0.4)
        points = list(data)
        self.assertEqual(len(points), 50, "Unexpected number of points generated")
        self.assertAlmostEqual(points[-1][0], 42.6, delta=0.01, msg="Unexpected last x value")
        self.assertAlmostEqual(round(mean_fft, 2), 0.31, delta=0.01, msg="Unexpected mean of the 1D fft")
        self.assertAlmostEqual(round(median_fft, 2), 0.57, delta=0.01, msg="Unexpected median of the 1D fft")
    def test_case_3(self):
        data, ax, _, _ = task_func()
        points = list(data)
        x_values = [point[0] for point in points]
        abs_diff_values = [point[3] for point in points]
        self.assertTrue(all(-10.0 <= x <= 10.0 for x in x_values), "x values are out of the expected range")
        self.assertTrue(all(0.0 <= x <= 1.42 for x in abs_diff_values), "abs(sin(x) - cos(x)) values are out of the expected range")
        # Check the plot data
        lines = ax.get_children()
        self.assertEqual(len(lines), 610, "Unexpected number of lines in the plot")
    def test_case_4(self):
        with self.assertRaises(ValueError):
            task_func(33, -11, 2)
    def test_case_5(self):
        data, _, mean_fft, median_fft = task_func()
        points = list(data)
        for x, sin_x, cos_x, _ in points:
            self.assertAlmostEqual(sin_x, np.sin(x), delta=0.01, msg=f"sin({x}) value is incorrect")
            self.assertAlmostEqual(cos_x, np.cos(x), delta=0.01, msg=f"cos({x}) value is incorrect")
        self.assertAlmostEqual(round(mean_fft, 2), 1.38, delta=0.01, msg="Unexpected mean of the 1D fft")
        self.assertAlmostEqual(round(median_fft, 2), 0.54, delta=0.01, msg="Unexpected median of the 1D fft")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)