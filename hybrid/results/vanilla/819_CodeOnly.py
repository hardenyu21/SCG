import time
import random

def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    # Validate input parameters
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("iterations must be a positive integer.")
    if not isinstance(min_delay, float) or min_delay <= 0:
        raise ValueError("min_delay must be a positive floating point value.")
    if not isinstance(max_delay, float) or max_delay <= 0:
        raise ValueError("max_delay must be a positive floating point value.")
    if min_delay > max_delay:
        raise ValueError("min_delay must be less than or equal to max_delay.")
    
    # Set the random seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    messages = []
    total_delay = 0.0
    
    for _ in range(iterations):
        # Sample a random delay from the uniform distribution
        delay = random.uniform(min_delay, max_delay)
        
        # Simulate the delay
        time.sleep(delay)
        
        # Record the message
        message = f"{delay:.2f} seconds have passed"
        messages.append(message)
        
        # Accumulate the total delay
        total_delay += delay
    
    return messages, total_delay