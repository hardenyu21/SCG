import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    # Define the regular expression pattern
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Create a DataFrame from the matches
    df = pd.DataFrame(matches, columns=COLUMN_NAMES)
    
    # Convert the 'Age' column to integer
    df['Age'] = df['Age'].astype(int)
    
    # Plot the age distribution using seaborn
    sns.histplot(df['Age'], bins=10, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the DataFrame
    return df