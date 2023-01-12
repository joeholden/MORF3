import pandas as pd
import os
import re

log_dir = "IJ Polygon Logs"
regex_pattern = r"STD_C2-(\d+)"


def consolidate_logsheets(path, pattern, output_folder, identifier):
    all_rows = []

    for root, dirs, files in os.walk(path):
        for file in files:
            df = pd.read_csv(os.path.join(root, file))
            cols = list(df.columns)
            for r in range(df.shape[0]):
                row = df.iloc[r, :]
                animal = re.search(pattern=pattern, string=row[1])[1]
                row = [i for i in row]
                row.append(int(animal))
                row = tuple([i for i in row])
                all_rows.append(row)

    cols.append('Animal')
    all_rows = set(all_rows)
    all_rows = [list(i) for i in all_rows]
    final_df = pd.DataFrame(all_rows, columns=cols)
    final_df = final_df.sort_values('Animal')
    final_df = final_df.reset_index()
    final_df = final_df.drop([' ', 'index'], axis=1)

    final_df.to_excel(f'{output_folder}/{identifier}_consolidated.xlsx')


consolidate_logsheets(path=log_dir, pattern=regex_pattern, output_folder="IJ Polygon Logs", identifier='3233 RE')