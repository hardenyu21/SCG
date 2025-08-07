import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Extract the 'from_user' values from the result
    from_user_values = [entry['from_user'] for entry in result]
    
    # Select a random color from the provided colors list
    random_color = random.choice(colors)
    
    # Set the style of seaborn
    sns.set(style="whitegrid")
    
    # Create the histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(from_user_values, color=random_color, kde=False)
    
    # Add labels and title
    plt.xlabel('From User')
    plt.ylabel('Frequency')
    plt.title('Histogram of From User Values')
    
    # Display the histogram
    plt.show()