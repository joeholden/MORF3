import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = "Consolidated + Distance.xlsx"
data = pd.read_excel(path)
latitude = data["Latitude (Radius Radians)"]
longitude = data["Theta Degrees in Left Eye Space"]
area = data["FO_Area"]
area_frac = data["FO_%Area"]
cvh_feret = data["FO_Feret"]
radius = data['Radius (um)']


def get_category(dp):
    if -3/2 < dp < -9/8:
        return 0
    if -9/8 < dp < -3/4:
        return 2
    if -3/4 < dp < -3/8:
        return 3
    if -3/8 < dp <= 0:
        return 4
    else:
        print(dp)

data['Latitude Categories'] = latitude.map(get_category)
print(data['Latitude Categories'])

sns.set(style="darkgrid")
plt.style.use("bmh")
plt.figure(figsize=(12, 8))

sns.violinplot(data=data, x="Latitude Categories", y="Radius (um)")
plt.show()