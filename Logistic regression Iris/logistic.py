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
    return gt

def cost(B, X, Y):
    gt = hypo(B, X)
    c = (-Y * np.log(gt) - (1 - Y) * np.log(1 - gt)).mean()
    return c

# import some data to play with
iris = datasets.load_iris()
# we only take the first two features.
X = iris.data[0:100, :2]  
intercept = np.ones(X[:,1].shape)
intercept = np.reshape(intercept,(100,1))
Y = iris.target[0:100]
# convert data in numpy format
X = np.asarray(X)
# add intercept
X = np.concatenate((intercept, X), axis=1)
Y = np.asarray(Y)
Y = np.reshape(Y,(100,1))
B = np.zeros(3)
B = np.reshape(B, (3,1))

# initializing hyperparameters
alpha = 0.1
steps = 100000
N = len(Y)

# gradient descent runner
for i in range(steps):
    c = cost(B, X, Y)
    gt = hypo(B, X)
    # gradient = (X.T.dot(gt - Y)) / N        
    gradient = np.dot(X.T, (gt - Y)) / N        
    # print(gradient.shape)
    B = B - alpha * gradient
    print("Step : {} Cost : {}".format(i,c))

print("B = ")
print(B)

# Actual values to test
# 5.1 3.5 0
# 7   3.2 1

# making a prediction
print("{} {} {}".format(B[0][0],B[1][0],B[2][0]) )
hypo = B[0][0]*1 + B[1][0]*5.1 + B[2][0]*3.5
prediction = 1/(1 + np.exp(-hypo))

print(prediction)

plt.title("Iris Flower")
plt.scatter(X[:, 1], X[:, 2], c=Y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.show()
