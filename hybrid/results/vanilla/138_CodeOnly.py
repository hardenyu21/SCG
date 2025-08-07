import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    # Check if the input is a DataFrame and contains the 'Letters' column
    if not isinstance(df, pd.DataFrame) or 'Letters' not in df.columns:
        raise ValueError("Input must be a DataFrame with a 'Letters' column.")
    
    # Filter the DataFrame to include only the specified letters
    df_filtered = df[df['Letters'].isin(letters)]
    
    # Count the frequency of each letter
    letter_counts = df_filtered['Letters'].value_counts().reindex(letters, fill_value=0)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    letter_counts.plot(kind='bar', ax=ax)
    
    # Set labels and title
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequency')
    
    # Return the Axes object
    return ax