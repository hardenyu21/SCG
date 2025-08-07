import pandas as pd
from scipy.stats import pearsonr
import numpy as np

def task_func(data):
    # Check if the data frame has less than 2 rows
    if len(data) < 2:
        return np.nan
    
    # Convert scores from string format to floats
    data['scores'] = data['scores'].astype(float)
    
    # Encode categorical grades into numerical values based on their rank order
    grade_mapping = {grade: rank for rank, grade in enumerate(data['grades'].unique())}
    data['encoded_grades'] = data['grades'].map(grade_mapping)
    
    # Compute the Pearson correlation coefficient
    correlation, _ = pearsonr(data['scores'], data['encoded_grades'])
    
    return correlation