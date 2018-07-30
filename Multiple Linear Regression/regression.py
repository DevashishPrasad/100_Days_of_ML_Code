import pandas as pd
import numpy as np

def runner(x, y, b, alpha, iterations):
    N = len(x1)
    cost = []
    loss = 0
    for i in range(iterations):
        loss = (b.T.dot(x)) - y
        gradient = (x.dot(loss.T)) / N   
        b = b - alpha * gradient
        cost = np.sum(np.power(loss,2))/(N * 2)
        print("STEP " + str(i) + " : cost - " + str(cost))
    return b, cost
    
df = pd.read_excel("data.xls")

x1 = np.array(df.X2)
x2 = np.array(df.X3)
N = len(x1)
x0 = np.ones(N)
x = np.array([x0,x1,x2])
y = np.array(df.X1)

b = np.matrix([[0],[0],[0]])
print(b.shape)
alpha = 0.00001
iterations = 1000000

b, cost = runner(x, y, b, alpha, iterations)

print("b = " + str(b) )
print("cost = " + str(cost))
