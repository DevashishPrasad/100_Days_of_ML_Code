import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("breast-cancer.data")
tumor_size = np.asarray(df["30-34"])
age = np.asarray(df["30-39"])
events = np.asarray(df["no-recurrence-events"])

tsize1 = []
tsize2 = []
age1 = []
age2 = []

for i in range(len(events)):
    if (events[i] == "no-recurrence-events"):
        events[i] = 1
    else:
        events[i] = 0

for i in range(len(tumor_size)):
    tumor_size[i] = int(tumor_size[i].split("-")[0])
    tumor_size[i] += 2

for i in range(len(age)):
    age[i] = int(age[i].split("-")[0])
    age[i] += 5

for i in range(len(events)):
    if(events[i] == 0):
        tsize1.append(tumor_size[i])
        age1.append(age[i])
    else:  
        tsize2.append(tumor_size[i])
        age2.append(age[i])

plt.scatter(tsize1, age1, Color="red", Label="no-recurrence-events")
plt.scatter(tsize2, age2, Color="blue", Label="recurrence-events")
plt.xlabel("Tumor size")
plt.ylabel("Age")
plt.title("Breast Cance events")
plt.legend()
plt.show()
