import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('Merged Data_31.xlsx')
print(df.columns)
# df1 = df.drop(['Side', 'FO_Side', 'CVH_Side', 'Region', 'FO_Label',
#          'CVH_Label', 'Cell Identifier',
#               'FO_MinThr', 'FO_Mode', 'FO_Min', 'FO_Median',
#               'CVH_MinThr', 'CVH_Mode', 'CVH_Min', 'CVH_Median',
#               'CVH_Animal', 'CVH_Cell Number', 'CVH_Max', 'CVH_Slice', 'CVH_Solidity',
#               'FO_Animal', 'FO_Cell Number', 'FO_Max', 'FO_Slice', 'FO_Solidity',
#               'FO_MaxThr', 'CVH_MaxThr', 'Animal', 'Cell Number'], axis=1)
#
# df1 = df.apply(pd.to_numeric)
# df1 = df.astype(float)

cleaned_data = df[[
    "Latitude (Radius Radians)",
    "Theta Degrees in Left Eye Space",
    "FO_Area",
    "FO_Perim.",
    "FO_Major",
    "FO_Minor",
    "FO_Circ.",
    "FO_Feret",
    "FO_%Area",
    "FO_Round",
    "FO_Solidity",
    "CVH_Area",
    "CVH_Perim.",
    "CVH_Feret",
    "Radius (um)",
    "CCOM Distance",
    "Mean Vessel Diameter",
    "Min Vessel Diameter",
    "Max Vessel Diameter",
    "Number of Contacts"
]]

sns_plot = sns.clustermap(cleaned_data.corr(), cmap="seismic")
plt.savefig('Dendrogram HM.png', dpi=300)
plt.show()
