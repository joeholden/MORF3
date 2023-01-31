import os
import pandas as pd
import functools as ft

data_file_1 = "Up to Data Correct Excel Sheets/Consolidated + Distance.xlsx"
data_file_2 = "Up to Data Correct Excel Sheets/Transposed Combined Diameters.xlsx"

df1 = pd.read_excel(data_file_1)
df2 = pd.read_excel(data_file_2)

print(df1.shape, df2.shape)

merged_data = ft.reduce(lambda left, right: pd.merge(left, right, on="Cell Identifier"), [df1, df2])
merged_data.to_excel('Merged Data_31.xlsx', index=False)
print(merged_data.shape)
