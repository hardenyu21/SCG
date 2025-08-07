import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(loc=mean, scale=std_dev, size=1000)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    
    # Create a histogram
    plt.figure(figsize=(10, 5))
    plt.hist(sample, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Histogram of the Sample')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    histogram_path = 'histogram.png'
    if save_plots:
        plt.savefig(histogram_path)
    plt.show()
    
    # Create a QQ plot
    plt.figure(figsize=(10, 5))
    stats.probplot(sample, dist="norm", plot=plt)
    plt.title('QQ Plot of the Sample')
    qqplot_path = 'qqplot.png'
    if save_plots:
        plt.savefig(qqplot_path)
    plt.show()
    
    # Return the results
    plot_paths = [histogram_path, qqplot_path] if save_plots else []
    return skewness, kurtosis, plot_paths

# Example usage:
# skew, kurt, plot_files = task_func(save_plots=True)
# print(f"Skewness: {skew}, Kurtosis: {kurt}, Plot Files: {plot_files}")