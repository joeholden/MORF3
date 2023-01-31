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
cvh_area = data["CVH_Area"]
area_frac = data["FO_%Area"]
fo_feret = data["FO_Feret"]
radius = data['Radius (um)']
solidity = data["FO_Solidity"]
ccom = data["CCOM Distance"]
rnd = data['FO_Round']


sns.set(style="darkgrid")
plt.style.use("bmh")

sns.histplot(data=solidity, label="Solidity", kde=True, stat='density')

plt.ylabel('Frequency')
plt.xlabel('Solidity')
plt.title('Solidity')
plt.legend()
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# plt.scatter(latitude, solidity, area_frac)
# plt.xlabel("Latitude")
# plt.ylabel("Solidity")
# ax.set_zlabel("GFAP Area Fraction")
# ax.set_zlim(0, 0.02)
# plt.show()