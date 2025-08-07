import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def task_func(data, sample_rate=8000):
    # Step 1: Add a new key "a" with the value 1 to the dictionary
    data['a'] = 1
    
    # Step 2: Generate a signal based on the values in "data"
    # Assuming the signal is a simple sum of sine waves with frequencies corresponding to the keys in "data"
    t = np.linspace(0, 1, sample_rate, endpoint=False)  # Time vector
    signal = np.zeros_like(t)
    for key, value in data.items():
        if isinstance(key, (int, float)):  # Only consider numeric keys as frequencies
            signal += np.sin(2 * np.pi * key * t)
    
    # Step 3: Run a Fast Fourier Transform (FFT) on the signal
    fft_result = fftpack.fft(signal)
    freqs = fftpack.fftfreq(len(signal), d=1/sample_rate)
    
    # Step 4: Plot and return the FFT of the signal
    fig, ax = plt.subplots()
    ax.plot(freqs[:len(freqs)//2], np.abs(fft_result[:len(fft_result)//2]))
    ax.set_title('FFT of the signal')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Amplitude')
    plt.show()
    
    return fft_result, ax