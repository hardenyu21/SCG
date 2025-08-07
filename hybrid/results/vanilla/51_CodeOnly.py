from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, age: int, height: int):
    # Filter the DataFrame based on the specified 'Age' and 'Height' conditions
    filtered_df = df[(df['Age'] > age) & (df['Height'] > height)]
    
    # Check if the filtered DataFrame has less than 3 columns
    if filtered_df.shape[1] < 3:
        # Add a 'Cluster' column with 0 for each row
        filtered_df['Cluster'] = 0
        ax = None
    else:
        # Perform KMeans clustering on 'Age' and 'Height'
        kmeans = KMeans(n_clusters=3, random_state=0)
        filtered_df['Cluster'] = kmeans.fit_predict(filtered_df[['Age', 'Height']])
        
        # Plot the scatter plot
        fig, ax = plt.subplots()
        scatter = ax.scatter(filtered_df['Age'], filtered_df['Height'], c=filtered_df['Cluster'], cmap='viridis')
        ax.set_xlabel('Age')
        ax.set_ylabel('Height')
        ax.set_title('KMeans Clustering based on Age and Height')
        plt.colorbar(scatter, ax=ax, label='Cluster')
    
    return filtered_df, ax