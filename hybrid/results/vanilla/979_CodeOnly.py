import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Create a DataFrame from the feature array
    df = pd.DataFrame(feature_array, columns=feature_names)
    
    # Shuffle the columns of the DataFrame
    shuffled_columns = np.random.permutation(df.columns)
    shuffled_df = df[shuffled_columns]
    
    # Create a new feature array with the shuffled columns
    shuffled_feature_array = shuffled_df.values
    
    # Initialize the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=seed)
    
    # Train the classifier on the shuffled feature data
    rf_classifier.fit(shuffled_feature_array, target_array)
    
    return rf_classifier