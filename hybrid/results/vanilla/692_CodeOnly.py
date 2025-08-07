import math
import pandas as pd

def task_func(tuples_list):
    # Apply math.sin to each element in each tuple
    sin_tuples = [(math.sin(x) for x in tup) for tup in tuples_list]
    
    # Create a DataFrame from the list of sine values
    df = pd.DataFrame(sin_tuples)
    
    return df