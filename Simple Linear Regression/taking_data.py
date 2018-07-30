import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("data.xls")

x = np.asarray(df.X)
y = np.asarray(df.Y)

plt.scatter(x,y)

plt.show()
