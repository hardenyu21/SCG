from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def task_func(l):
    # Convert the input list to a numpy array
    data = np.array(l)
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)
    
    # Extract the first two principal components
    first_component = principal_components[:, 0]
    second_component = principal_components[:, 1]
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(first_component, second_component)
    
    # Set the title and labels
    ax.set_title("PCA Result")
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax