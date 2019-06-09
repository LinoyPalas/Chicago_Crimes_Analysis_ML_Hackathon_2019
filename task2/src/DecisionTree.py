"""
This file includes implementation of Decision Tree.
"""
from sklearn import tree

class Decision_Tree:
    def __init__(self):
        self.X = None
        self.y = None
        self.classifier = tree.DecisionTreeClassifier()

    def fit(self, x, y):
        self.classifier = self.classifier.fit(x, y)

    def predict(self, x):
        return self.classifier.predict(x)
