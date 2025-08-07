import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    # Default dataset if no data is provided
    if data is None:
        data = {
            'Weight_String': ['70.5', '65.2', '80.0', '55.3', '72.1'],
            'Height': [170, 165, 180, 160, 175]
        }
    
    # Validate that all weights are strings
    if not all(isinstance(weight, str) for weight in data['Weight_String']):
        raise ValueError("All values in 'Weight_String' must be formatted as strings.")
    
    # Convert string-formatted weights to floats
    data['Weight'] = [float(weight) for weight in data['Weight_String']]
    
    # Create a DataFrame for easier plotting
    df = pd.DataFrame(data)
    
    # Plotting
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Weight', y='Height', data=df)
    ax.set_title("Weight vs Height")
    ax.set_xlabel("Weight (kg)")
    ax.set_ylabel("Height (cm)")
    
    # Show the plot
    plt.show()
    
    return ax