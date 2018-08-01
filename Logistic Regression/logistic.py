import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.raw", header=None)
arr = np.asarray(data)

type1 = []
neighbour1 = []
satisfaction1 = []

type2 = []
neighbour2 = []
satisfaction2 = []

print("Type Neighbour Satisfaction")
# Getting data
for i in range(36):
    s = str(arr[i]).split("       ")
    if(i<18):
        type1.append(s[1].strip()) 
        neighbour1.append(s[3].strip())
        satisfaction1.append(s[4].strip())
        print(type1[i] + " " + neighbour1[i] + " " + satisfaction1[i])
    else:
        type2.append(s[1].strip()) 
        neighbour2.append(s[3].strip())
        satisfaction2.append(s[4].strip())
        print(type2[i-18] +  " " + neighbour2[i-18] + " " + satisfaction2[i-18])

plt.scatter(neighbour1, satisfaction1, Color="red")
plt.scatter(neighbour2, satisfaction2, Color="blue")
plt.xlabel("Neighbour conact")
plt.ylabel("House satisfaction")
plt.title("House Conditions in Copenhagen")
plt.legend()
plt.show()

