import pandas as pd
import os
import re

excel_dir = "C:/Users/Acer/Desktop/All IJ Logs/full outline/"
regex_pattern = r"(\d+) (\w+)_full"


def consolidate_all_ij(path, pattern=r"(\d+) (\w+)_full"):
    """

    """

    all_rows = []
    for root, dirs, files in os.walk(path):
        for file in files:
            regex_search = re.search(pattern=pattern, string=file)
            animal = regex_search[1]
            side = regex_search[2]
            print(animal, side)
            df = pd.read_excel(os.path.join(root, file))

            cols = list(df.columns)
            for r in range(df.shape[0]):
                row = df.iloc[r, :]
                row = [i for i in row]
                row.append(animal)
                row.append(side)
                row = tuple([i for i in row])
                all_rows.append(row)

    cols.append('Animal_')
    cols.append('Side')

    all_rows = [list(i) for i in all_rows]

    final_df = pd.DataFrame(all_rows, columns=cols)
    final_df = final_df.sort_values(['Animal_', 'Side'], ascending=[True, False])
    final_df = final_df.reset_index()
    final_df = final_df.drop(['index'], axis=1)
    print(final_df)
    final_df.to_excel(excel_dir + 'test_consolidate_IJ.xlsx')

consolidate_all_ij(path=excel_dir)
