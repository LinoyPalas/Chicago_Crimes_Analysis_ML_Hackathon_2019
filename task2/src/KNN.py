"""
KNN.py
This file includes implementation of KNN.
"""

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import euclidean_distances
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class Knn:
    def __init__(self, k=600):
        self.k = k
        self.X = None
        self.y = None
        self.classifier = KNeighborsClassifier(n_neighbors=self.k)

    def fit(self, x, y):
        self.classifier = self.classifier.fit(x,y)

    def predict(self, x):
        return self.classifier.predict(x)




