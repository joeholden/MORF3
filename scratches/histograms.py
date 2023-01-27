import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "Consolidated + Distance.xlsx"
data = pd.read_excel(path)
data1 = data['FO_AR']
# data2 = data['CVH_Circ.']

sns.set(style="darkgrid")
plt.style.use("bmh")

sns.histplot(data=data1, label="FO", kde=True, stat='density')
# sns.histplot(data=data2, label="CVH", kde=True, stat='density')
# plt.ylabel('Frequency')
# plt.xlabel('Density')
plt.title('Histogram')
plt.legend()
plt.show()
