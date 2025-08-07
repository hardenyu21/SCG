import random
from collections import Counter

def task_func(values, weights, n_samples):
    # Ensure the weights sum to 1
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]
    
    # Sample random numbers based on the weighted distribution
    samples = random.choices(values, weights=normalized_weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = Counter(samples)
    
    return dict(histogram)

# Example usage:
values = ['a', 'b', 'c']
weights = [0.1, 0.3, 0.6]
n_samples = 1000
histogram = task_func(values, weights, n_samples)
print(histogram)