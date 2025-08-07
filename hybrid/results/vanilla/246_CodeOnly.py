import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2 * np.pi, 0.01)

def task_func(n_waves, seed=0):
    if n_waves < 1:
        return [], np.array([]), None

    np.random.seed(seed)
    sine_waves = []
    frequencies = np.linspace(1, n_waves, n_waves)

    for freq in frequencies:
        sine_wave = np.sin(freq * ANGLES)
        sine_waves.append(sine_wave)

    # Mix all sine waves into a single signal
    mixed_signal = np.sum(sine_waves, axis=0)

    # Calculate the Fast Fourier Transform (FFT) of the mixed signal
    fft_data = fft(mixed_signal)

    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data), bins=50, color='blue', alpha=0.7)
    ax.set_title('Histogram of FFT Magnitude')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')

    return sine_waves, fft_data, ax

# Example usage:
# sine_waves, fft_data, ax = task_func(5)
# plt.show()