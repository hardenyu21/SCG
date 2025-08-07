import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_list):
    # Combine the list of dictionaries into a DataFrame
    df = pd.DataFrame(data_list)
    
    # Transpose the DataFrame to have tests as columns and students as rows
    df_transposed = df.T
    
    # Plotting
    ax = df_transposed.plot(kind='line', marker='o', figsize=(10, 6))
    
    # Set labels and title
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores Over Multiple Tests')
    
    # Show grid
    ax.grid(True)
    
    # Show plot
    plt.legend(title='Students')
    plt.show()
    
    return ax