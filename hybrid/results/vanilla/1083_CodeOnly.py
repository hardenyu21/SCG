import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Step 1: Input Validation
    required_keys = {'Salary_String', 'Experience'}
    if not required_keys.issubset(data.keys()):
        raise ValueError("Input data must contain 'Salary_String' and 'Experience' keys.")
    
    # Step 2: DataFrame Conversion
    df = pd.DataFrame(data)
    
    # Step 3: Empty Data Handling
    if df.empty:
        fig, ax = plt.subplots()
        ax.set_xlabel('Experience')
        ax.set_ylabel('Normalized Salary')
        return ax
    
    # Step 4: Salary Conversion
    try:
        df['Salary'] = df['Salary_String'].str.replace(',', '').astype(float)
    except ValueError as e:
        raise ValueError("Failed to convert 'Salary_String' to float.") from e
    
    # Step 5: Salary Normalization
    scaler = MinMaxScaler()
    df['Normalized_Salary'] = scaler.fit_transform(df[['Salary']])
    
    # Step 6: Data Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Normalized_Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    
    return ax