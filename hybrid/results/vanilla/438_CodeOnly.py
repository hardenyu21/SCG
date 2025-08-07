import pickle
import os
import matplotlib.pyplot as plt

def task_func(numbers, file_path="save.pkl"):
    # Check if the input is a list of numbers
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Input must be a list of numbers.")
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(numbers)
    ax.set_title("Plot of Numbers")
    
    # Save the figure to a pickle file
    with open(file_path, 'wb') as file:
        pickle.dump(fig, file)
    
    # Close the figure to free up memory
    plt.close(fig)
    
    # Load the figure back from the pickle file
    with open(file_path, 'rb') as file:
        loaded_fig = pickle.load(file)
    
    # Delete the pickle file
    os.remove(file_path)
    
    return loaded_fig