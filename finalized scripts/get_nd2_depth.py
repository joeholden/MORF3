import nd2
import pandas as pd
import os

z_depths_for_files = []
img_path_root = r"C:\Users\Acer\Desktop\MORF Disease Paper\STZ 8 WK COHORT 2 IMAGES\Images\3368 RE".replace("\\", os.sep)


def get_nd2_metadata(path_to_nd2):
    with nd2.ND2File(path_to_nd2) as f:
        depth_z = f.metadata.contents.frameCount
        print(depth_z)
        filename = os.path.basename(path_to_nd2)
        z_depths_for_files.append((filename, depth_z))


for root, dirs, files in os.walk(img_path_root):
    for file in files:
        try:
            enclosing_dir = os.path.split(os.path.dirname(os.path.join(root, file)))[-1]
            # inner gets the absolute path of parent directory and
            # the outer splits off the last directory in that path or the enclosing folder
            if enclosing_dir == 'single':
                get_nd2_metadata(path_to_nd2=os.path.join(root, file))
        except Exception as e:
            print(e)

z_depths = pd.Series([i[1] for i in z_depths_for_files])
filenames = pd.Series([i[0] for i in z_depths_for_files])

df = pd.concat([filenames, z_depths], axis=1)
print(df.head())
df.to_excel("1.xlsx")
