from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_column):
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Initialize and train the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X, y)
    
    # Get feature importances
    feature_importances = rf_classifier.feature_importances_
    
    # Create a DataFrame for feature importances
    feature_importance_df = pd.DataFrame({
        'Feature': X.columns,
        'Importance': feature_importances
    })
    
    # Sort the DataFrame by importance in descending order
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    
    # Plot the feature importances
    plt.figure(figsize=(10, 8))
    ax = sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
    ax.set_xlabel('Feature Importance Score')
    ax.set_ylabel('Features')
    ax.set_title('Visualizing Important Features')
    
    # Show the plot
    plt.show()
    
    return rf_classifier, ax