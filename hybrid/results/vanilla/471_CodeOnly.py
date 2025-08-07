from collections import Counter
import pandas as pd

def task_func(myList):
    # Count the frequency of each word in the list
    word_counts = Counter(myList)
    
    # Convert the Counter object to a DataFrame
    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])
    
    return df