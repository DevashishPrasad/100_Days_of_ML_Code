"""This program uses Sklearn iris dataset and performs ogistic regression 
Created by Devashish Krishna Prasad """
print(__doc__)
from sklearn import datasets
import matplotlib.pyplot as plt

# import some data to play with
iris = datasets.load_iris()
X = iris.data[0:100, :2]  # we only take the first two features.
Y = iris.target[0:100]

plt.title("Iris Flower")
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.show()
