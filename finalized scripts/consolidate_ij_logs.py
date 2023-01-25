import pandas as pd
import os
import re

log_dir = "C:/Users/Acer/PycharmProjects/MORF3/DATA/3237 RE/Excel Sheets/IJ Polygon Logs/"
regex_pattern = r"STD_C2-(\d+)"
IDENT = "3237 RE"


def consolidate_logsheets(path, output_folder, identifier, pattern=r"STD_C2-(\d+)"):
    """
    Parses a folder of IJ logs and consolidates all the dataframes so there are no duplicates.
    An additional column is added for animal number.
    :param path: path to directory with all the IJ logs
    :param pattern: regex pattern to find animal number
    :param output_folder: path to output directory
    :param identifier: eg. animal '3233 LE'
    :return: None
    """

    all_rows = []
    for root, dirs, files in os.walk(path):
        for file in files:
            df = pd.read_csv(os.path.join(root, file))
            cols = list(df.columns)
            for r in range(df.shape[0]):
                row = df.iloc[r, :]

                animal = re.search(pattern=pattern, string=row['Label'])[1]
                row = [i for i in row]
                row.append(int(animal))
                row = tuple([i for i in row])
                all_rows.append(row)

    cols.append('Animal')
    all_rows = set(all_rows)
    all_rows = [list(i) for i in all_rows]
    final_df = pd.DataFrame(all_rows, columns=cols)
    final_df = final_df.sort_values(['Animal', 'Area'], ascending=[True, False])
    final_df = final_df.reset_index()
    try:
        final_df = final_df.drop([' ', 'index'], axis=1)
    except KeyError:
        final_df = final_df.drop(['index'], axis=1)

    final_df.to_excel(f'{output_folder}/{identifier}_consolidated.xlsx')

    # df is sorted now by animal number and by area. Convex hull
    # always has larger area. Separate out both data frames and save.
    convex_hull = final_df.iloc[::2, :]
    full_outline = final_df.iloc[1::2, :]
    convex_hull.to_excel(f'{output_folder}/{identifier}_convex_hull.xlsx')
    full_outline.to_excel(f'{output_folder}/{identifier}_full_outline.xlsx')


consolidate_logsheets(path=log_dir, output_folder=log_dir, identifier=IDENT)