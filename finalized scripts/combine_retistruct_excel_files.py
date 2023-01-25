import pandas as pd
import os
import re

excel_dir = "C:/Users/Acer/PycharmProjects/MORF3/DATA/RETISTRUCT/Cell Point Assignment/"
regex_pattern = r"(\d+)_(\w+)_"


def consolidate_retistruct(path, pattern=r"(\d+)_(\w+)_"):
    """

    """

    all_rows = []
    for root, dirs, files in os.walk(path):
        for file in files:
            regex_search = re.search(pattern=pattern, string=file)
            animal = regex_search[1]
            side = regex_search[2]
            df = pd.read_excel(os.path.join(root, file))

            cols = list(df.columns)
            for r in range(df.shape[0]):
                row = df.iloc[r, :]
                row = [i for i in row]
                row.append(int(animal))
                row.append(side)
                row = tuple([i for i in row])
                all_rows.append(row)

    cols.append('Animal')
    cols.append('Side')

    all_rows = [list(i) for i in all_rows]

    final_df = pd.DataFrame(all_rows, columns=cols)
    final_df = final_df.sort_values(['Animal', 'Side'], ascending=[True, False])
    final_df = final_df.reset_index()
    final_df = final_df.drop(['index'], axis=1)
    print(final_df)
    final_df.to_excel('test_consolidate.xlsx')

consolidate_retistruct(path=excel_dir)