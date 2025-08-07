import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

def task_func(L, M, N, audio_file):
    # Check if the audio file exists
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"The specified audio file '{audio_file}' does not exist.")
    
    # Read the audio file
    data, sample_rate = sf.read(audio_file)
    
    # Calculate the sound pressure level (SPL)
    spl = 20 * np.log10(np.sqrt(np.mean(data**2)))
    
    # Create an MxN matrix from the list L
    matrix = np.array(L).reshape(M, N)
    
    # Normalize the matrix based on the SPL
    normalized_matrix = matrix / spl
    
    # Generate a spectrogram from the normalized matrix
    fig, ax = plt.subplots()
    spec = ax.specgram(normalized_matrix, Fs=sample_rate, scale_by_freq=True, mode='magnitude')
    
    # Set the scale for frequency and time
    ax.set_yscale('log')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Frequency [Hz]')
    
    # Display the spectrogram
    plt.colorbar(spec[3], ax=ax, label='Intensity [dB]')
    plt.title('Spectrogram of Normalized Matrix')
    
    # Return the normalized matrix and the figure object
    return normalized_matrix, fig