import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = "Merged Data_31.xlsx"
data = pd.read_excel(path)
latitude = data["Latitude (Radius Radians)"]
longitude = data["Theta Degrees in Left Eye Space"]
area = data["FO_Area"]
area_frac = data["FO_%Area"]
cvh_feret = data["FO_Feret"]
radius = data['Radius (um)']
solidity = data["FO_Solidity"]
ccom = data["CCOM Distance"]
rnd = data['FO_IntDen']
minor = data["FO_Minor"]
major = data["FO_Major"]
num_contacts = data['Number of Contacts']
mean_vessel_dia = data['Mean Vessel Diameter']
min_vessel_dia = data["Min Vessel Diameter"]
max_vessel_dia = data["Max Vessel Diameter"]
fo_round = data["FO_Round"]


sns.set(style="darkgrid")
plt.style.use("bmh")
plt.figure(figsize=(12, 8))
# polynomial fit with degree = 2
model = np.poly1d(np.polyfit(latitude, num_contacts, 1))

# add fitted polynomial line to scatterplot
polyline = np.linspace(-1.5, 0, 200)
# plt.plot(polyline, model(polyline), label='Regression')

plt.scatter(x=fo_round, y=num_contacts, color='purple', label="Cells")
plt.title('Roundness vs Number of Vessels Contacted', fontsize=24)
plt.xlabel("Roundness", fontsize=18)
plt.ylabel("Number of Vessels Contacted", fontsize=18)
plt.legend()
plt.show()
