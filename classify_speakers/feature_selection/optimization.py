import numpy as np
from typing import Dict, List
from dataclasses import dataclass
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

from benchmarking import mean_square_entropy, mean_square_correlation, inertia


@dataclass
class FeatureSpace:
    n_components: int
    parameter_grid: Dict[str, List]
    explained_variance: np.ndarray
    mean_square_entropy: float
    mean_square_correlation: float
    nearest_neighbour_silhouette: float


def optimize_n_components_plot(X: np.ndarray, y_size: int):
    search_space = np.arange(2, X.shape[1])
    explained_variance = np.zeros(search_space.shape)
    mse = np.zeros(search_space.shape)
    msc = np.zeros(search_space.shape)
    kmi = np.zeros(search_space.shape)
    for i, n_components in enumerate(search_space):
        pca = PCA(n_components=n_components)
        pca.fit(X)
        explained_variance[i] = np.mean(pca.explained_variance_ratio_)
        mse[i] = mean_square_entropy(pca.components_.T)
        msc[i] = mean_square_correlation(pca.components_.T)
        kmi[i] = inertia(pca.components_, y_size)
    plt.figure()
    plt.plot(search_space, explained_variance, label="Explained variance")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(search_space, mse, label="Mean square entropy")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(search_space, msc, label="Mean square correlation")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(search_space, kmi, label="K means inertia")
    plt.legend()
    plt.show()
