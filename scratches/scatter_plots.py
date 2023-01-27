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

sns.set(style="darkgrid")
plt.style.use("bmh")
plt.figure(figsize=(12, 8))
# polynomial fit with degree = 2
model = np.poly1d(np.polyfit(latitude, cvh_feret, 2))

# add fitted polynomial line to scatterplot
polyline = np.linspace(-1.5, 0, 200)
# plt.plot(polyline, model(polyline), label='Regression')

plt.scatter(x=latitude, y=radius, color='purple', label="Cells")
plt.title('Feret Diameter by Distance from ONH', fontsize=24)
plt.xlabel("Latitude (radians)", fontsize=18)
plt.ylabel("Feret Diameter (um)", fontsize=18)
plt.legend()
plt.show()
