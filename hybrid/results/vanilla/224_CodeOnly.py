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