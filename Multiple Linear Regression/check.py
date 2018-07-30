# Here we check collinearity between various features
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_excel("data.xls")

# x1 = np.asmatrix(df.X2)
x1 = np.asarray(df.X2)
x2 = np.asarray(df.X3)
y = np.asarray(df.X1)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(y, x1, x2, color="#0000ff")
ax.set_xlabel('Systolic Blood Pressure')
ax.set_ylabel('Age')
ax.set_zlabel('Weight')
plt.show()

