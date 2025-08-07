from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100, noise_level=0.2):
    # Generate a clean sine wave
    x = np.linspace(0, 2 * np.pi, array_length)
    y_clean = np.sin(x)
    
    # Add noise to the sine wave
    noise = noise_level * np.random.normal(size=array_length)
    y_noisy = y_clean + noise
    
    # Define the model function to fit
    def sine_model(x, amplitude, frequency, phase, offset):
        return amplitude * np.sin(frequency * x + phase) + offset
    
    # Initial guess for the parameters
    initial_guess = [1, 1, 0, 0]
    
    # Fit the model to the noisy data
    params, covariance = curve_fit(sine_model, x, y_noisy, p0=initial_guess)
    
    # Extract the fitted parameters
    amplitude_fit, frequency_fit, phase_fit, offset_fit = params
    
    # Generate the fitted curve
    y_fit = sine_model(x, amplitude_fit, frequency_fit, phase_fit, offset_fit)
    
    # Plot the noisy data and the fitted curve
    fig, ax = plt.subplots()
    ax.plot(x, y_noisy, 'b.', label='Noisy Data')
    ax.plot(x, y_fit, 'r-', label='Fitted Curve')
    ax.set_title('Noisy Sine Wave and Fitted Curve')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage
task_func(array_length=100, noise_level=0.2)