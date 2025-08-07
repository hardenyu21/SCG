import numpy as np
from scipy import stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    try:
        # Check if all required features are in the DataFrame
        if not all(feature in df.columns for feature in FEATURES):
            return "Invalid input"

        # Replace values in the DataFrame based on the provided dictionary
        df_replaced = df.replace(dct)

        # Initialize a dictionary to store the results
        results = {}

        # Calculate statistics for each feature
        for feature in FEATURES:
            if feature in df_replaced.columns:
                data = df_replaced[feature].dropna()  # Drop NaN values for calculations

                # Calculate mean
                mean = np.mean(data)

                # Calculate median
                median = np.median(data)

                # Calculate mode
                mode_result = stats.mode(data)
                mode = mode_result.mode[0] if not mode_result.mode.empty else np.nan

                # Calculate variance
                variance = np.var(data, ddof=1)  # Sample variance

                # Store the results in the dictionary
                results[feature] = {
                    'mean': mean,
                    'median': median,
                    'mode': mode,
                    'variance': variance
                }
            else:
                results[feature] = {
                    'mean': np.nan,
                    'median': np.nan,
                    'mode': np.nan,
                    'variance': np.nan
                }

        return results

    except Exception as e:
        return "Invalid input"