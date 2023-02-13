#LAB PP Q6 a
import matplotlib.pyplot as plt
import numpy as np

fow = [i+1 for i in range(10)]
India = [5,35,24,0,99,1,35,15,27,14]
England = [10,55,34,21,2,7,118,29,32,10]

tempIndia = 0
tIndia = []
for i in range(len(India)):
    tempIndia+=India[i]
    tIndia.append(tempIndia)

India = tIndia

tempEngland = 0
tEngland = []
for i in range(len(England)):
    tempEngland+=England[i]
    tEngland.append(tempEngland)

England = tEngland

plt.plot(fow,India, label="India", marker="o")
plt.plot(fow,England, label="England",marker="x")
plt.xlabel("Wickets")
plt.ylabel("Runs")
plt.title("Runs Scored by India and England")
plt.legend()
plt.show()