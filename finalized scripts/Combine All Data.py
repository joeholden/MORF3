import os
import pandas as pd
import functools as ft


retistruct_data_path = "C:/Users/Acer/PycharmProjects/MORF3/" \
                       "DATA/RETISTRUCT/Consolidated RETISTRUCT Cell Information.xlsx"
convex_hull_data_path = "C:/Users/Acer/PycharmProjects/MORF3/" \
                        "DATA/All IJ Logs/convex hull/Convex Hull Consolidated Data.xlsx"
full_outline_data_path = "C:/Users/Acer/PycharmProjects/MORF3/" \
                        "DATA/All IJ Logs/full outline/Full Outline Consolidated.xlsx"

retistruct_df = pd.read_excel(retistruct_data_path)
convex_hull_df = pd.read_excel(convex_hull_data_path)
full_outline_df = pd.read_excel(full_outline_data_path)

retistruct_df['Cell Identifier'] = retistruct_df['Animal'].astype(str) + "_" + \
                                   retistruct_df['Side'].astype(str) + "_" + \
                                   retistruct_df['Cell Number'].astype(str)
convex_hull_df['Cell Identifier'] = convex_hull_df['Animal'].astype(str) + "_" + \
                                    convex_hull_df['Side'].astype(str) + "_" + \
                                    convex_hull_df['Cell Number'].astype(str)
full_outline_df['Cell Identifier'] = full_outline_df['Animal'].astype(str) + "_" + \
                                     full_outline_df['Side'].astype(str) + "_" + \
                                     full_outline_df['Cell Number'].astype(str)

# true_count = 0
# false_count = 0
# other = 0
# for value in retistruct_df['Cell Identifier']:
#     cv_presence = convex_hull_df.isin([value]).any().any()
#     full_presence = full_outline_df.isin([value]).any().any()
#     if (cv_presence, full_presence) == (False, False):
#         false_count += 1
#     if (cv_presence, full_presence) == (True, True):
#         true_count += 1
#     if (cv_presence, full_presence) != (True, True) and (cv_presence, full_presence) != (False, False):
#         other += 1

# print(f"Total Number of Cells Fully Quantified: {true_count}\n"
#       f"Total Number of Cells With Coordinates but Missing Data: {false_count}\n"
#       f"Total Number of Data Errors: {other}")

# Rename Columns with prefix for Convex Hull (CVH) or Full Outline (FO)

new_cvh_columns = ['CVH_' + i for i in convex_hull_df.columns if i != 'Cell Identifier']
new_fo_columns = ['FO_' + i for i in full_outline_df.columns if i != 'Cell Identifier']
new_cvh_columns.append('Cell Identifier')
new_fo_columns.append('Cell Identifier')

convex_hull_df.set_axis(new_cvh_columns, axis=1, inplace=True)
full_outline_df.set_axis(new_fo_columns, axis=1, inplace=True)

all_dataframes = [retistruct_df, full_outline_df, convex_hull_df]
merged_data = ft.reduce(lambda left, right: pd.merge(left, right, on="Cell Identifier"), all_dataframes)

merged_data.to_excel('Merged Data.xlsx', index=False)