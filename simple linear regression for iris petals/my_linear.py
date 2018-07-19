import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def runner(m_current, b_current, alpha, iterations, x, y):
    b_gradient = 0
    m_gradient = 0
    N = len(x)
    cost = 1
    for i in range(iterations):
        b_gradient = 0
        m_gradient = 0
        cost = 0
        for j in range(N):
            b_gradient += -(2/N) * (y[j] - ((m_current * x[j]) + b_current))
            m_gradient += -(2/N) * x[j] * (y[j] - ((m_current * x[j]) + b_current))
        b_current = b_current - (alpha * b_gradient)
        m_current = m_current - (alpha * m_gradient)

        for j in range(N):
            cost += ( y[j] - (m_current * x[j] + b_current) ) ** 2
        print("loss = " + cost)
    return m_current, b_current, cost/N

df = pd.read_excel("data.xls")

x = np.asarray(df.X)
y = np.asarray(df.Y)

alpha = 0.0001
iterations = 1000

# y = mx + b

m_current = 0
b_current = 0

m_current, b_current, cost = runner(m_current, b_current, alpha, iterations, x, y)

print("m = {}".format(m_current))
print("b = {}".format(b_current))
print("cost = {}".format(cost))

x1 = np.linspace(0, 8, 2)
y1 = m_current * (x1) + b_current

plt.plot(x1, y1)
plt.scatter(x,y)

plt.show()
