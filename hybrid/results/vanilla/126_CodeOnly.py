import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
import matplotlib.pyplot as plt

def task_func(animals=None, seed=42):
    if animals is None:
        animals = ['Lion', 'Tiger', 'Bear', 'Giraffe', 'Elephant', 'Zebra', 'Kangaroo', 'Penguin', 'Panda', 'Koala']
    
    random_seed(seed)
    
    data = []
    
    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean_count = statistics.mean(counts)
        median_count = statistics.median(counts)
        std_dev_count = statistics.stdev(counts)
        
        data.append({
            'Animal': animal,
            'Mean': mean_count,
            'Median': median_count,
            'Standard Deviation': std_dev_count
        })
    
    df = pd.DataFrame(data)
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    for i, animal in enumerate(animals):
        plt.bar(animal, df.loc[i, 'Mean'], yerr=df.loc[i, 'Standard Deviation'], capsize=5, label=animal)
    
    plt.xlabel('Animal')
    plt.ylabel('Mean Count ± Standard Deviation')
    plt.title('Animal Counts in the Zoo')
    plt.xticks(rotation=45)
    plt.legend(title='Animals')
    plt.tight_layout()
    plt.show()
    
    return df

# Example usage
df = task_func()
print(df)