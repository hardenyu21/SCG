import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(df, freq='D', decomposition_model='multiplicative'):
    # Validate input DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    if 'value' not in df.columns:
        raise ValueError("DataFrame must contain a 'value' column.")
    
    if not pd.api.types.is_numeric_dtype(df['value']):
        raise ValueError("The 'value' column must contain numeric data.")
    
    # Validate frequency
    if not isinstance(freq, str):
        raise ValueError("Frequency 'freq' must be a string.")
    
    # Validate decomposition model
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("Decomposition model must be 'additive' or 'multiplicative'.")
    
    # Perform decomposition
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, period=pd.Timedelta(freq).days)
    
    # Plot the decomposition
    fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
    decomposition.observed.plot(ax=axes[0], title='Observed')
    decomposition.trend.plot(ax=axes[1], title='Trend')
    decomposition.seasonal.plot(ax=axes[2], title='Seasonality')
    decomposition.resid.plot(ax=axes[3], title='Residuals')
    plt.tight_layout()
    
    return decomposition, axes