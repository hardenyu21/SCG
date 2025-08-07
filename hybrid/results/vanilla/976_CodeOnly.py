import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    # Check if the input is 2D
    if records.ndim != 2:
        raise ValueError("Input records must be 2D.")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Shuffle the features
    num_features = records.shape[1]
    shuffled_indices = np.random.permutation(num_features)
    shuffled_records = records[:, shuffled_indices]
    
    # Normalize the values
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(shuffled_records)
    
    # Create shuffled feature names
    feature_names = [f"f{i+1}" for i in range(num_features)]
    np.random.shuffle(feature_names)
    
    # Convert to DataFrame
    df = pd.DataFrame(normalized_records, columns=feature_names)
    
    return df