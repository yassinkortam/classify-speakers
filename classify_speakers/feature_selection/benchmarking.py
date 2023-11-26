import numpy as np
from scipy.stats import entropy
from sklearn.cluster import KMeans


def mean_square_entropy(X: np.ndarray):
    """
    Computes the mean square entropy of the features of X.
    """
    probability_distribution = np.abs(X) / np.sum(np.abs(X), axis=0)
    entropies = np.apply_along_axis(entropy, 0, probability_distribution)
    return np.mean(entropies**2)


def mean_square_correlation(X: np.ndarray):
    """
    Computes the mean square correlation of the features of X.
    """
    correlation_matrix = np.corrcoef(X, rowvar=False)
    return np.mean(correlation_matrix**2)


def inertia(X: np.ndarray, n: int = 2):
    """
    Computes the k means silhouette score of the features of X.
    """
    kmeans = KMeans(n_clusters=n, random_state=0, n_init="auto")
    kmeans.fit(X)
    return kmeans.inertia_
