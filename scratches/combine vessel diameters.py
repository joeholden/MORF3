import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

data = {}
combined_df = pd.DataFrame()
print(combined_df.shape)

parent_dir = "C:/Users/joema/Desktop/Combine Vessel Diameters/"
for root, dirs, files in os.walk(parent_dir):
    for file in files:
        df = pd.read_excel(os.path.join(root, file), index_col="Unnamed: 0")
        if combined_df.shape == (0, 0):
            combined_df = df
        else:
            combined_df = pd.concat([combined_df, df], axis=1)

# print(combined_df.shape)
bad_cols = []
big_max = 0
for col_name in combined_df.columns:
    c = combined_df[col_name]
    truth_table = [True if i > 45 else False for i in c]
    if set(truth_table) != {False}:
        bad_cols.append(col_name)
print(bad_cols)
combined_df = combined_df.drop(bad_cols, axis=1)
combined_df.to_excel("Combined Vessel Diameters.xlsx")
combined_df.T.to_excel("Transposed Combined Diameters.xlsx")

# valz = []
# for i in combined_df.values:
#     for j in i:
#         valz.append(j)
# s = pd.Series(valz)

# fig = plt.figure(figsize=(12,8))
# sns.set(style="darkgrid")
# plt.style.use("bmh")
# sns.histplot(s, kde=True, stat='density', label="Diameters")
#
# plt.title("Size of Vessels Contacted by Astrocytes", fontsize=24)
# plt.xlabel("Vessel Diameter", fontsize=18)
# plt.ylabel("Frequency of Astrocyte Contacts", fontsize=18)
# plt.legend()
# plt.show()
# print(min(s), max(s))

# Get histogram of frequency of contacts per astrocyte
counts = []
for col_name in combined_df.columns:
    c = combined_df[col_name]
    individual_cell_contacts = []
    for i in c:
        if not pd.isna(i):
            individual_cell_contacts.append(i)
    counts.append(len(individual_cell_contacts))

fig = plt.figure(figsize=(12,8))
sns.set(style="darkgrid")
plt.style.use("bmh")

sns.histplot(counts, stat="probability", label="Number of Contacts")
plt.title("Number of Unique Vessels Contacted", fontsize=24)
plt.xlabel("Unique Contacts", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.xlim(0, 7)
plt.legend()
plt.show()
