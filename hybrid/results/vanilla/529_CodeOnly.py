from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize a list to store the sums of the dice rolls
    sums = []
    
    # Simulate rolling the dice
    for _ in range(num_rolls):
        # Roll the dice and calculate the sum
        roll_sum = sum(random.randint(1, 6) for _ in range(num_dice))
        sums.append(roll_sum)
    
    # Count the occurrences of each sum
    sum_counter = Counter(sums)
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(sum_counter.keys(), sum_counter.values(), color='blue')
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')
    
    # Save the plot if a path is provided
    if plot_path:
        plt.savefig(plot_path)
    
    # Return the Counter object and the Axes object
    return sum_counter, ax

# Example usage:
# counter, ax = task_func(num_rolls=1000, num_dice=2, plot_path='dice_distribution.png')
# plt.show()