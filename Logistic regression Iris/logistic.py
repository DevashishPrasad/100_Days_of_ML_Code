"""This program uses Sklearn iris dataset and performs 
Logistic regression to predict  type of flower
Created by Devashish Krishna Prasad """
print(__doc__)
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

def hypo(B, X):
    ht = X.dot(B)
    gt = 1/(1 + np.exp(-ht))
    # print(B.shape)
    return gt

def cost(B, X, Y):
    gt = hypo(B, X)
    c = (-Y * np.log(gt) - (1 - Y) * np.log(1 - gt)).mean()
    return c

# import some data to play with
iris = datasets.load_iris()
# we only take the first two features.
X = iris.data[0:100, :2]  
Y = iris.target[0:100]
# convert data in numpy format
X = np.asarray(X)
Y = np.asarray(Y)
B = np.matrix([[0],[0]])
print(B.shape)
# initializing hyperparameters
alpha = 0.001
steps = 1000
N = len(Y)

# gradient descent runner
for i in range(steps):
    c = cost(B, X, Y)
    gt = hypo(B, X)
    gradient = (X.T.dot(gt - Y)) / N        
    B = B - alpha * gradient
    print((gt - Y).shape)
    # print(c)

print("B = ")
print(B)
# plt.title("Iris Flower")
# plt.scatter(X[:, 0], X[:, 1], c=Y)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')


plt.show()
