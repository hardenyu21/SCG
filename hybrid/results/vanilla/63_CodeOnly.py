import pandas as pd
import matplotlib.pyplot as plt

def task_func(car_dict):
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(list(car_dict.items()), columns=['Car', 'Color'])
    
    # Count the occurrences of each color
    color_counts = df['Color'].value_counts()
    
    # Plot the distribution of vehicle colors
    ax = color_counts.plot(kind='bar', color='skyblue')
    ax.set_title('Distribution of Vehicle Colors')
    ax.set_xlabel('Color')
    ax.set_ylabel('Number of Cars')
    
    # Show the plot
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# car_dict = {'Toyota': 'Red', 'Honda': 'Blue', 'Ford': 'Red', 'Chevrolet': 'Blue', 'BMW': 'Black'}
# df, ax = task_func(car_dict)