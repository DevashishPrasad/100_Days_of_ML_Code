import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def runner(x, y, b, alpha, iterations):
    N = len(x1)
    for i in range(iterations):
        loss = (b.T.dot(x)) - y
        gradient = (x.T.dot(loss)) / N   
        b = b - alpha * gradient
        cost = ((b.T.dot(x) - y) ** 2)/(N * 2)
    return b, cost
    


df = pd.read_excel("data.xls")

x1 = np.array(df.X2)
x2 = np.array(df.X3)
N = len(x1)
x0 = np.ones(N)
x = np.array([x0,x1,x2])
y = np.array(df.X1)

# our hypothesis function will be
# y = bT.x

b = np.matrix([[0],[0],[0]])
print(b.shape)
alpha = 0.01
iterations = 1000

b, cost = runner(x, y, b, alpha, iterations)

print("b = " + str(b) )
print("cost = " + str(cost))
