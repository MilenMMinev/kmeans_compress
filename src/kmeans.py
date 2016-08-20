import numpy as np
import random


class KMeans():
    """ A class that implements k-means clustering
        @param number of clusters
        @param number of iterations to approximate centroids"""

    def __init__(self, n_clusters, n_iterations=10):
        self.n_clusters = n_clusters
        self.n_iterations = n_iterations

    def nearest_point(self, point, others):
        others = np.array(others)

        min_distance = 1000

        for p in others:
            distance = np.linalg.norm(p - point)
            if distance < min_distance:
                min_distance = distance
                nearest_color = p

        return nearest_color

        # distance = np.sum((others - point)**2, axis=1)
        # print(distance)
        return 0

    def pick_rand_centers(self, data):
        self.cluster_centers_ = data[np.random.choice(
            range(data.shape[0]), self.n_clusters, replace=False), :]

    def fit(self, data):
        self.pick_rand_centers(data)


    def predict(self, data):
        for i in range(self.n_iterations):
            distances = np.sum(
                (self.cluster_centers_[:, np.newaxis, :] - data) ** 2, axis=2)
            closest = np.argmin(distances, axis=0)

            for i in range(self.n_clusters):
                if len(data[closest == i, :]) != 0:
                    self.cluster_centers_[i, :] = data[closest == i, :].mean(axis=0)
        return closest