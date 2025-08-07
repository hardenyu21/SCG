import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, save_plot=False, plot_path=None):
    # Unzip the list of objects and their 3D coordinates
    objects, coordinates_3d = zip(*data)
    coordinates_3d = np.array(coordinates_3d)

    # Apply PCA to reduce dimensionality to 2D
    pca = PCA(n_components=2)
    coordinates_2d = pca.fit_transform(coordinates_3d)

    # Create a plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1])

    # Annotate each point with the corresponding object name
    for i, obj in enumerate(objects):
        ax.annotate(obj, (coordinates_2d[i, 0], coordinates_2d[i, 1]))

    # Check if save_plot is True and plot_path is provided
    if save_plot:
        if plot_path is None:
            raise ValueError("If save_plot is True, plot_path must be provided.")
        plt.savefig(plot_path)
        plt.close(fig)
        return coordinates_2d
    else:
        return coordinates_2d, ax