import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("data.xls")

x1 = np.asmatrix(df.X2)
x2 = np.asarray(df.X3)
y = np.asarray(df.X1)

# y = t0 + t1x1 + t2x2
print(x1)
print(x2)
print(y)
