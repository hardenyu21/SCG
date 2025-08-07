import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def task_func():
    # Load the iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target
    iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    # Set the global font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Create a pair plot
    pair_plot = sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"])

    # Set the title of the plot
    pair_plot.fig.suptitle('Iris Dataset Pair Plot', y=1.02)

    # Set labels for each feature on the axes
    for ax in pair_plot.axes.flat:
        if ax is not None:
            ax.set_xlabel(ax.get_xlabel(), fontsize=10)
            ax.set_ylabel(ax.get_ylabel(), fontsize=10)

    # Return the matplotlib Figure object
    return pair_plot.fig

# Example usage
if __name__ == "__main__":
    fig = task_func()
    plt.show()